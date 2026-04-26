"""
Pattern registry — single source of truth for prompt patterns.

Patterns are stored as .md files under llm_promptkit/patterns/<category>/<name>.md.
Each file has a title line (# ...), optional metadata, and the pattern template body.
"""

from importlib import resources
from pathlib import Path
from typing import List, Tuple


def _get_patterns_package() -> Path:
    """Resolve the patterns directory using importlib.resources."""
    # Python 3.9+: use files() API
    ref = resources.files("llm_promptkit") / "patterns"
    # resources.files returns a Traversable; convert to Path for convenience
    return Path(str(ref))


def get_patterns_dir() -> Path:
    """Get the patterns directory path."""
    return _get_patterns_package()


def list_pattern_names() -> List[str]:
    """List all available pattern names (slug format, e.g. 'chain-of-thought')."""
    patterns_dir = _get_patterns_package()
    names = []
    if not patterns_dir.is_dir():
        return names
    for category_dir in sorted(patterns_dir.iterdir()):
        if category_dir.is_dir() and not category_dir.name.startswith("_"):
            for md_file in sorted(category_dir.iterdir()):
                if md_file.suffix == ".md" and not md_file.name.startswith("README"):
                    names.append(md_file.stem)
    return names


def list_patterns_with_categories() -> List[Tuple[str, str]]:
    """List patterns as (name, category) tuples."""
    patterns_dir = _get_patterns_package()
    result = []
    if not patterns_dir.is_dir():
        return result
    for category_dir in sorted(patterns_dir.iterdir()):
        if category_dir.is_dir() and not category_dir.name.startswith("_"):
            for md_file in sorted(category_dir.iterdir()):
                if md_file.suffix == ".md" and not md_file.name.startswith("README"):
                    result.append((md_file.stem, category_dir.name))
    return result


def read_pattern(name: str) -> str:
    """Read a pattern's template text by name.

    The template is the body of the .md file after the title line (# ...),
    with category metadata lines (**Category:** ...) stripped.
    """
    patterns_dir = _get_patterns_package()
    if not patterns_dir.is_dir():
        raise ValueError(f"Patterns directory not found: {patterns_dir}")

    # Search for the pattern in any category subdirectory
    for category_dir in patterns_dir.iterdir():
        if category_dir.is_dir() and not category_dir.name.startswith("_"):
            candidate = category_dir / f"{name}.md"
            if candidate.is_file():
                return _parse_pattern_body(candidate)

    available = ", ".join(list_pattern_names())
    raise ValueError(f"Unknown pattern '{name}'. Available: {available}")


def _parse_pattern_body(path: Path) -> str:
    """Extract the pattern template from a .md file.

    Strips:
    - Title line (# Pattern Name)
    - Category line (**Category:** ...)
    - Leading blank lines after metadata
    """
    lines = path.read_text(encoding="utf-8").splitlines()
    body_lines = []
    past_metadata = False
    for line in lines:
        # Skip title line
        if line.startswith("# ") and not past_metadata:
            continue
        # Skip category metadata
        if line.startswith("**Category:**") and not past_metadata:
            continue
        # First non-metadata, non-blank line signals start of body
        if not past_metadata and line.strip():
            past_metadata = True
            body_lines.append(line)
        elif past_metadata:
            body_lines.append(line)
    return "\n".join(body_lines).strip()


def get_pattern_description(name: str) -> str:
    """Get the first line of a pattern as a short description."""
    content = read_pattern(name)
    first_line = content.split("\n")[0]
    return first_line[:80]
