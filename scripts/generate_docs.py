#!/usr/bin/env python3
"""Generate byte-preserving MkDocs mirrors; --check reports drift without writes.

Prompts retain the existing provider/model filename flattening. Patterns get
individual mirrors under docs/patterns/<category>/; hand-written pattern overview
pages (docs/patterns/*.md) are not generated or removed.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from llm_promptkit.metadata import split_frontmatter

REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_ROOT = REPO_ROOT / "src" / "llm_promptkit"
DOCS_PROMPTS = REPO_ROOT / "docs" / "prompts"
DOCS_PATTERNS = REPO_ROOT / "docs" / "patterns"
CATEGORIES = {
    "code": "Code", "context": "Context", "creative": "Creative", "debug": "Debug",
    "defensive": "Defensive", "education": "Education", "output": "Output",
    "professional": "Professional", "reasoning": "Reasoning", "system": "System",
    "model-optimized": "Model-Optimized",
}


def nav_link(category: str, subcategory: str | None = None) -> str:
    """Canonical Unicode leftwards-arrow navigation."""
    label = CATEGORIES.get(category, category.title())
    if subcategory:
        return f"[← Back to {label} {subcategory.title()}](../index.md)"
    return f"[← Back to {label} Prompts](../index.md)"


def with_navigation(content: bytes, category: str, subcategory: str | None = None) -> bytes:
    """Keep YAML first, then navigation, then the exact source body bytes."""
    _, front, body = split_frontmatter(content)
    return front + nav_link(category, subcategory).encode("utf-8") + b"\n\n" + body


def content_files(kind: str) -> list[Path]:
    return sorted(p for p in (SRC_ROOT / kind).rglob("*.md") if p.name.lower() != "readme.md")


def doc_path(source: Path, kind: str) -> Path:
    relative = source.relative_to(SRC_ROOT / kind)
    parts = relative.parts
    if kind == "prompts" and parts[0] == "model-optimized" and len(parts) == 4:
        relative = Path(parts[0], parts[1], f"{parts[2]}-{parts[3]}")
    return REPO_ROOT / "docs" / kind / relative


def generate_index(category: str, files: list[Path]) -> str:
    """Keep the existing category overview layout."""
    label = CATEGORIES.get(category, category.title())
    lines = [
        f"# {label} Prompts", "", f"Ready-to-use prompts for {label.lower()} tasks.", "",
        "## Browsing Prompts", "", "```bash", f"promptkit prompts --model {category}",
        f'promptkit search "{category}"', "```", "", "## Available Prompts", "",
        "| Prompt | File |", "|--------|------|",
    ]
    for path in sorted(files):
        lines.append(f"| [{path.stem}]({path.name}) | `{path.name}` |")
    return "\n".join(lines + [""])


def render_docs() -> dict[Path, bytes]:
    """Compute the complete managed output in memory, independent of docs state."""
    rendered: dict[Path, bytes] = {}
    groups: dict[Path, list] = {}
    display_names: dict[Path, str] = {}
    for kind in ("prompts", "patterns"):
        for source in content_files(kind):
            parts = source.relative_to(SRC_ROOT / kind).parts
            destination = doc_path(source, kind)
            if destination in rendered:
                raise ValueError(f"Duplicate documentation destination: {destination}")
            subcategory = parts[1] if kind == "prompts" and len(parts) > 2 else None
            rendered[destination] = with_navigation(source.read_bytes(), parts[0], subcategory)
            if kind == "prompts":
                groups.setdefault(destination.parent, []).append(destination)
                display_names[destination] = (
                    f"{parts[2]} {source.stem}" if len(parts) == 4 else source.stem
                )

    for directory, files in sorted(groups.items()):
        relative = directory.relative_to(DOCS_PROMPTS)
        if len(relative.parts) == 1:
            text = generate_index(relative.parts[0], files)
        else:
            label = directory.name.replace("-", " ").title()
            lines = [f"# {label}", "", f"Model-optimized prompts for {label.lower()}.", "",
                     "| Prompt | File |", "|--------|------|"]
            for path in files:
                lines.append(f"| [{display_names[path]}]({path.name}) | `{path.name}` |")
            text = "\n".join(lines + [""])
        rendered[directory / "index.md"] = text.encode("utf-8")

    model_dirs = sorted(d for d in groups if d.parent == DOCS_PROMPTS / "model-optimized")
    lines = ["# Model-Optimized Prompts", "",
             "Prompts optimized for specific LLM providers and models.", "", "## Categories", "",
             "| Category | Prompts |", "|----------|--------|"]
    for directory in model_dirs:
        label = directory.name.replace("-", " ").title()
        lines.append(f"| [{label}]({directory.name}/index.md) | {len(groups[directory])} |")
    rendered[DOCS_PROMPTS / "model-optimized/index.md"] = "\n".join(lines + [""]).encode()

    lines = ["# Prompts", "", "Browse ready-to-use prompts organized by category.", "",
             "## Categories", "", "| Category | Prompts |", "|----------|--------|"]
    for category, label in CATEGORIES.items():
        count = sum(len(files) for directory, files in groups.items()
                    if directory.relative_to(DOCS_PROMPTS).parts[0] == category)
        if count:
            lines.append(f"| [{label}]({category}/index.md) | {count} |")
    rendered[DOCS_PROMPTS / "index.md"] = "\n".join(lines + [""]).encode()
    return rendered


def sync_docs(expected: dict[Path, bytes], *, check: bool, roots: list[Path]) -> int:
    """Return 1 for check-mode drift; otherwise apply exact writes and removals."""
    actual = set()
    for root in roots:
        for path in root.rglob("*.md"):
            # Preserve hand-written pattern overviews, manage only nested mirrors.
            if root == DOCS_PATTERNS and path.parent == root:
                continue
            actual.add(path)
    changed = [path for path, content in expected.items()
               if not path.is_file() or path.read_bytes() != content]
    orphans = sorted(actual - expected.keys())
    if check:
        for path in sorted(changed):
            print(f"Drift (missing or changed): {path}")
        for path in orphans:
            print(f"Drift (orphan): {path}")
        return int(bool(changed or orphans))
    for path in changed:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(expected[path])
    for path in orphans:
        path.unlink()
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Exit 1 on drift; do not write files")
    args = parser.parse_args(argv)
    result = sync_docs(render_docs(), check=args.check, roots=[DOCS_PROMPTS, DOCS_PATTERNS])
    count = sum(len(content_files(kind)) for kind in ("prompts", "patterns"))
    print(f"{count} content mirrors {'checked' if args.check else 'synced'}; drift={result}")
    return result


if __name__ == "__main__":
    raise SystemExit(main())
