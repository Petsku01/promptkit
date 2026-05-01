#!/usr/bin/env python3
"""Generate docs/prompts/ from src/llm_promptkit/prompts/ for MkDocs.

Usage:
    python scripts/generate_docs.py

This script:
1. Syncs docs/prompts/ with src/llm_promptkit/prompts/
2. Adds MkDocs navigation headers ([← Back to ...])
3. Generates index.md files for each category
4. Removes docs files that no longer exist in src/
5. Cleans up stale files in docs/ that have no src/ counterpart
"""

import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_PROMPTS = REPO_ROOT / "src" / "llm_promptkit" / "prompts"
DOCS_PROMPTS = REPO_ROOT / "docs" / "prompts"

# Categories under model-optimized that are flat (no model subdirs)
FLAT_CATEGORIES = {
    "advanced-techniques", "agentic", "benchmarks", "evaluation",
    "few-shot", "roles", "safety", "system-prompts", "use-cases",
}

CATEGORIES = {
    "code": "Code",
    "context": "Context",
    "creative": "Creative",
    "debug": "Debug",
    "defensive": "Defensive",
    "education": "Education",
    "output": "Output",
    "professional": "Professional",
    "reasoning": "Reasoning",
    "system": "System",
    "model-optimized": "Model-Optimized",
}


def nav_link(category: str, subcategory: str | None = None) -> str:
    """Generate [← Back to ...] nav link for MkDocs."""
    if subcategory:
        label = CATEGORIES.get(category, category.title())
        return f"[← Back to {label} {subcategory.title()}](../index.md)"
    label = CATEGORIES.get(category, category.title())
    return f"[← Back to {label} Prompts](../index.md)"


def generate_index(category: str, files: list[Path]) -> str:
    """Generate index.md for a category with a table of prompts."""
    label = CATEGORIES.get(category, category.title())
    lines = [
        f"# {label} Prompts",
        "",
        f"Ready-to-use prompts for {label.lower()} tasks.",
        "",
        "## Browsing Prompts",
        "",
        "```bash",
        f"promptkit prompts --model {category}",
        f'promptkit search "{category}"',
        "```",
        "",
        "## Available Prompts",
        "",
        "| Prompt | File |",
        "|--------|------|",
    ]
    for f in sorted(files):
        name = f.stem
        lines.append(f"| [{name}]({f.name}) | `{f.name}` |")
    lines.append("")
    return "\n".join(lines)


def sync_category(category: str) -> int:
    """Sync a non-model-optimized category. Returns count of synced files."""
    src_dir = SRC_PROMPTS / category
    docs_dir = DOCS_PROMPTS / category
    if not src_dir.exists():
        return 0

    docs_dir.mkdir(parents=True, exist_ok=True)

    # Get all .md files from src (excluding README.md)
    src_files = [f for f in src_dir.iterdir() if f.suffix == ".md" and f.name != "README.md"]
    synced = 0

    for src_file in src_files:
        # Read src content
        content = src_file.read_text(encoding="utf-8")

        # Add nav link at top
        docs_content = nav_link(category) + "\n\n" + content

        # Write to docs
        dest = docs_dir / src_file.name
        dest.write_text(docs_content, encoding="utf-8")
        synced += 1

    # Generate index.md
    index_content = generate_index(category, src_files)
    (docs_dir / "index.md").write_text(index_content, encoding="utf-8")

    # Remove docs files that no longer exist in src
    for docs_file in docs_dir.iterdir():
        if docs_file.name == "index.md":
            continue
        if docs_file.suffix == ".md":
            src_equiv = src_dir / docs_file.name
            if not src_equiv.exists():
                docs_file.unlink()
                print(f"  Removed orphan: {docs_file.relative_to(REPO_ROOT)}")

    return synced


def sync_flat_subcategory(parent: str, subcat: str) -> int:
    """Sync a flat subcategory (files directly, no model dirs).

    E.g. model-optimized/agentic/orchestration.md -> stays as agentic/orchestration.md
    """
    src_dir = SRC_PROMPTS / parent / subcat
    docs_dir = DOCS_PROMPTS / parent / subcat
    if not src_dir.exists():
        return 0

    docs_dir.mkdir(parents=True, exist_ok=True)

    src_files = [f for f in src_dir.iterdir() if f.suffix == ".md" and f.name != "README.md"]
    synced = 0

    for src_file in src_files:
        content = src_file.read_text(encoding="utf-8")
        docs_content = nav_link(parent, subcat) + "\n\n" + content
        dest = docs_dir / src_file.name
        dest.write_text(docs_content, encoding="utf-8")
        synced += 1

    # Generate index.md
    label = subcat.replace("-", " ").title()
    lines = [
        f"# {label}",
        "",
        f"Model-optimized prompts for {label.lower()}.",
        "",
        "| Prompt | File |",
        "|--------|------|",
    ]
    for f in sorted(src_files):
        lines.append(f"| [{f.stem}]({f.name}) | `{f.name}` |")
    lines.append("")
    (docs_dir / "index.md").write_text("\n".join(lines), encoding="utf-8")

    # Remove orphans
    for docs_file in docs_dir.iterdir():
        if docs_file.name == "index.md":
            continue
        if docs_file.suffix == ".md":
            src_equiv = src_dir / docs_file.name
            if not src_equiv.exists():
                docs_file.unlink()
                print(f"  Removed orphan: {docs_file.relative_to(REPO_ROOT)}")

    return synced


def sync_model_optimized() -> int:
    """Sync model-optimized prompts.

    Provider subdirs (anthropic, openai, etc.) have model subdirs:
        anthropic/claude-3-haiku/analysis.md -> anthropic/claude-3-haiku-analysis.md

    Flat subdirs (agentic, few-shot, etc.) keep their structure:
        agentic/orchestration.md -> agentic/orchestration.md
    """
    src_dir = SRC_PROMPTS / "model-optimized"
    docs_dir = DOCS_PROMPTS / "model-optimized"
    docs_dir.mkdir(parents=True, exist_ok=True)
    synced = 0

    # Process each subdirectory
    for subdir in src_dir.iterdir():
        if not subdir.is_dir():
            continue
        subcat_name = subdir.name

        if subcat_name in FLAT_CATEGORIES:
            # Flat subcategory: keep structure as-is
            count = sync_flat_subcategory("model-optimized", subcat_name)
            synced += count
            print(f"  model-optimized/{subcat_name}: {count} files synced (flat)")
        else:
            # Provider subcategory: flatten model dirs into single-level files
            # e.g. anthropic/claude-3-haiku/analysis.md -> anthropic/claude-3-haiku-analysis.md
            count = sync_provider_subcategory(subcat_name)
            synced += count
            print(f"  model-optimized/{subcat_name}: {count} files synced (provider)")

    # Top-level model-optimized index
    all_dirs = sorted([d for d in docs_dir.iterdir() if d.is_dir()],
                       key=lambda d: d.name)
    lines = [
        "# Model-Optimized Prompts",
        "",
        "Prompts optimized for specific LLM providers and models.",
        "",
        "## Categories",
        "",
        "| Category | Prompts |",
        "|----------|--------|",
    ]
    for d in all_dirs:
        count = len([f for f in d.rglob("*.md") if f.name != "index.md"])
        label = d.name.replace("-", " ").title()
        lines.append(f"| [{label}]({d.name}/index.md) | {count} |")
    lines.append("")
    (docs_dir / "index.md").write_text("\n".join(lines), encoding="utf-8")

    return synced


def sync_provider_subcategory(provider: str) -> int:
    """Sync a provider subcategory with model subdirs.

    e.g. anthropic/claude-3-haiku/analysis.md -> anthropic/claude-3-haiku-analysis.md
    """
    src_dir = SRC_PROMPTS / "model-optimized" / provider
    docs_dir = DOCS_PROMPTS / "model-optimized" / provider
    docs_dir.mkdir(parents=True, exist_ok=True)
    synced = 0

    # Collect all prompts from model subdirs
    prompts = []  # (display_name, filename, content)
    for model_dir in sorted(src_dir.iterdir()):
        if not model_dir.is_dir():
            continue
        model_name = model_dir.name
        for md_file in sorted(model_dir.iterdir()):
            if md_file.suffix != ".md" or md_file.name == "README.md":
                continue
            task = md_file.stem
            flat_name = f"{model_name}-{task}.md"
            display_name = f"{model_name} {task}"
            content = md_file.read_text(encoding="utf-8")
            docs_content = nav_link("model-optimized", provider) + "\n\n" + content
            dest = docs_dir / flat_name
            dest.write_text(docs_content, encoding="utf-8")
            prompts.append((display_name, flat_name))
            synced += 1

    # Generate index.md
    label = provider.replace("-", " ").title()
    lines = [
        f"# {label}",
        "",
        f"Model-optimized prompts for {label.lower()}.",
        "",
        "| Prompt | File |",
        "|--------|------|",
    ]
    for display_name, flat_name in prompts:
        lines.append(f"| [{display_name}]({flat_name}) | `{flat_name}` |")
    lines.append("")
    (docs_dir / "index.md").write_text("\n".join(lines), encoding="utf-8")

    # Remove orphans: docs files that don't match any src prompt
    for docs_file in docs_dir.iterdir():
        if docs_file.name == "index.md":
            continue
        if docs_file.suffix == ".md":
            # Check if any src model dir produces this filename
            stem = docs_file.stem
            found = False
            for model_dir in src_dir.iterdir():
                if not model_dir.is_dir():
                    continue
                task = stem.replace(model_dir.name + "-", "", 1)
                if task and (model_dir / f"{task}.md").exists():
                    found = True
                    break
            if not found:
                docs_file.unlink()
                print(f"  Removed orphan: {docs_file.relative_to(REPO_ROOT)}")

    return synced


def main():
    total = 0

    # Sync non-model categories
    for cat in CATEGORIES:
        if cat == "model-optimized":
            continue
        count = sync_category(cat)
        total += count
        print(f"  {cat}: {count} files synced")

    # Sync model-optimized
    count = sync_model_optimized()
    total += count

    print(f"\nTotal: {total} files synced")

    # Generate top-level prompts index
    lines = [
        "# Prompts",
        "",
        "Browse ready-to-use prompts organized by category.",
        "",
        "## Categories",
        "",
        "| Category | Prompts |",
        "|----------|--------|",
    ]
    for cat, label in CATEGORIES.items():
        docs_dir = DOCS_PROMPTS / cat
        if docs_dir.exists():
            count = len([f for f in docs_dir.rglob("*.md") if f.name != "index.md"])
            lines.append(f"| [{label}]({cat}/index.md) | {count} |")
    lines.append("")
    (DOCS_PROMPTS / "index.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()