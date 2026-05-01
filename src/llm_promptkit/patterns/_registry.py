"""Pattern registry — single source of truth for prompt patterns."""

from functools import lru_cache
from importlib import resources
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from llm_promptkit.config import get_config


class PromptKitError(Exception):
    """Base exception for llm-promptkit."""


class PatternNotFoundError(PromptKitError, LookupError):
    """Raised when a pattern name cannot be found in the registry."""


class PatternLoadError(PromptKitError):
    """Raised when a pattern file cannot be loaded or parsed."""


def _resolve_patterns_dir() -> Path:
    """Resolve patterns directory via importlib.resources (zip-safe)."""
    ref = resources.files("llm_promptkit") / "patterns"
    path = Path(str(ref))
    if not path.is_dir():
        raise PatternLoadError(f"Patterns directory not found: {path}")
    return path


def _get_pattern_dirs() -> List[Path]:
    """Get all pattern directories: user dirs first, then built-in."""
    dirs = []
    config = get_config()
    # User dirs first (higher priority)
    for d in config.extra_pattern_dirs:
        if d.is_dir():
            dirs.append(d)
    # Built-in last
    builtin = _resolve_patterns_dir()
    if builtin not in dirs:
        dirs.append(builtin)
    return dirs


def _scan_pattern(name: str, dirs: List[Path]) -> Optional[Tuple[Path, str]]:
    """Scan directories for a pattern by name.

    Returns (path, source_tag) if found, None otherwise.
    User dirs are scanned first, giving them priority.
    """
    for pattern_dir in dirs:
        for category_dir in sorted(pattern_dir.iterdir()):
            if category_dir.is_dir() and not category_dir.name.startswith("_"):
                candidate = category_dir / f"{name}.md"
                if candidate.is_file():
                    source = "custom" if pattern_dir != dirs[-1] else "built-in"
                    return (candidate, source)
        # Also check flat files (no category subdirectory)
        for md_file in sorted(pattern_dir.glob("*.md")):
            if md_file.stem == name and not md_file.name.startswith("README"):
                source = "custom" if pattern_dir != dirs[-1] else "built-in"
                return (md_file, source)
    return None


@lru_cache(maxsize=1)
def list_pattern_names() -> Tuple[str, ...]:
    """List available pattern names as an immutable tuple."""
    names = set()
    for pattern_dir in _get_pattern_dirs():
        for category_dir in sorted(pattern_dir.iterdir()):
            if category_dir.is_dir() and not category_dir.name.startswith("_"):
                for md_file in sorted(category_dir.iterdir()):
                    if md_file.suffix == ".md" and not md_file.name.startswith("README"):
                        names.add(md_file.stem)
        for md_file in sorted(pattern_dir.glob("*.md")):
            if not md_file.name.startswith("README"):
                names.add(md_file.stem)
    return tuple(sorted(names))


def invalidate_pattern_cache() -> None:
    """Clear pattern registry caches."""
    if hasattr(list_pattern_names, 'cache_clear'):
        list_pattern_names.cache_clear()
    if hasattr(list_patterns_with_categories, 'cache_clear'):
        list_patterns_with_categories.cache_clear()
    if hasattr(read_pattern, 'cache_clear'):
        read_pattern.cache_clear()


@lru_cache(maxsize=32)
def list_patterns_with_categories() -> Tuple[Tuple[str, str], ...]:
    """List patterns as (name, category) tuples.

    Custom patterns that override built-ins show their custom category.
    Custom patterns in flat files show 'custom' as category.
    Built-in patterns show their directory category.
    """
    seen: Dict[str, Tuple[str, str]] = {}
    for pattern_dir in _get_pattern_dirs():
        for category_dir in sorted(pattern_dir.iterdir()):
            if category_dir.is_dir() and not category_dir.name.startswith("_"):
                for md_file in sorted(category_dir.iterdir()):
                    if md_file.suffix == ".md" and not md_file.name.startswith("README"):
                        # Only add if not already seen (user dirs come first)
                        if md_file.stem not in seen:
                            seen[md_file.stem] = (md_file.stem, category_dir.name)
        for md_file in sorted(pattern_dir.glob("*.md")):
            if not md_file.name.startswith("README"):
                if md_file.stem not in seen:
                    seen[md_file.stem] = (md_file.stem, "custom")
    return tuple(sorted(seen.values()))


def get_pattern_source(name: str) -> str:
    """Return 'custom' or 'built-in' for a pattern."""
    result = _scan_pattern(name, _get_pattern_dirs())
    if result is None:
        return "unknown"
    return result[1]


@lru_cache(maxsize=32)
def read_pattern(name: str) -> str:
    """Read a pattern's template text by name.

    Raises PatternNotFoundError if name not found,
    PatternLoadError if file cannot be read.

    Custom patterns take priority over built-in patterns.
    """
    dirs = _get_pattern_dirs()
    result = _scan_pattern(name, dirs)

    if result is None:
        available = ", ".join(list_pattern_names())
        raise PatternNotFoundError(f"Unknown pattern '{name}'. Available: {available}")

    path, _source = result
    try:
        return _parse_pattern_body(path)
    except (OSError, UnicodeDecodeError) as e:
        raise PatternLoadError(f"Failed to read pattern '{name}': {e}") from e


def _parse_pattern_body(path: Path) -> str:
    """Extract pattern template from .md, stripping title and category metadata."""
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
    """First line of a pattern as a short description (max 80 chars)."""
    content = read_pattern(name)
    first_line = content.split("\n")[0]
    return first_line[:80]
