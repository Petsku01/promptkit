"""
Pattern registry — single source of truth for prompt patterns.

Patterns are stored as .md files under llm_promptkit/patterns/<category>/<name>.md.
Each file has a title line (# ...), optional metadata, and the pattern template body.
"""

from functools import lru_cache
from importlib import resources
from pathlib import Path
from typing import Tuple


class PromptKitError(Exception):
    """Base exception for llm-promptkit."""


class PatternNotFoundError(PromptKitError, LookupError):
    """Raised when a pattern name cannot be found in the registry."""


class PatternLoadError(PromptKitError):
    """Raised when a pattern file cannot be loaded or parsed."""


def _resolve_patterns_dir() -> Path:
    """Resolve the patterns directory using importlib.resources.

    Uses importlib.resources which is zip-safe and works with
    installed packages, not just development layouts.
    """
    ref = resources.files("llm_promptkit") / "patterns"
    path = Path(str(ref))
    if not path.is_dir():
        raise PatternLoadError(f"Patterns directory not found: {path}")
    return path


def get_patterns_dir() -> Path:
    """Get the patterns directory path."""
    return _resolve_patterns_dir()


@lru_cache(maxsize=1)
def list_pattern_names() -> Tuple[str, ...]:
    """List all available pattern names (slug format, e.g. 'chain-of-thought').

    Returns a tuple to prevent accidental mutation of the cached result.
    """
    patterns_dir = _resolve_patterns_dir()
    names = []
    for category_dir in sorted(patterns_dir.iterdir()):
        if category_dir.is_dir() and not category_dir.name.startswith("_"):
            for md_file in sorted(category_dir.iterdir()):
                if md_file.suffix == ".md" and not md_file.name.startswith("README"):
                    names.append(md_file.stem)
    return tuple(names)


def invalidate_pattern_cache():
    """Clear the pattern registry caches.

    Call this after installing or removing pattern files,
    e.g. during plugin setup or testing.
    """
    list_pattern_names.cache_clear()
    list_patterns_with_categories.cache_clear()


@lru_cache(maxsize=32)
def list_patterns_with_categories() -> Tuple[Tuple[str, str], ...]:
    """List patterns as (name, category) tuples.

    Returns a tuple to prevent accidental mutation of the cached result.
    """
    patterns_dir = _resolve_patterns_dir()
    result = []
    for category_dir in sorted(patterns_dir.iterdir()):
        if category_dir.is_dir() and not category_dir.name.startswith("_"):
            for md_file in sorted(category_dir.iterdir()):
                if md_file.suffix == ".md" and not md_file.name.startswith("README"):
                    result.append((md_file.stem, category_dir.name))
    return tuple(result)


def read_pattern(name: str) -> str:
    """Read a pattern's template text by name.

    The template is the body of the .md file after the title line (# ...),
    with category metadata lines (**Category:** ...) stripped.

    Raises:
        PatternNotFoundError: If the pattern name is not in the registry.
        PatternLoadError: If the pattern file cannot be read or parsed.
    """
    patterns_dir = _resolve_patterns_dir()

    for category_dir in patterns_dir.iterdir():
        if category_dir.is_dir() and not category_dir.name.startswith("_"):
            candidate = category_dir / f"{name}.md"
            if candidate.is_file():
                try:
                    return _parse_pattern_body(candidate)
                except Exception as e:
                    raise PatternLoadError(f"Failed to read pattern '{name}': {e}") from e

    available = ", ".join(list_pattern_names())
    raise PatternNotFoundError(f"Unknown pattern '{name}'. Available: {available}")


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
        if line.startswith("# ") and not past_metadata:
            continue
        if line.startswith("**Category:**") and not past_metadata:
            continue
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
