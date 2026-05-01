"""Shared helpers for CLI commands."""

import subprocess
from importlib import resources
from pathlib import Path
from typing import List, Tuple

from rich.console import Console

from llm_promptkit.config import get_config

console = Console()

CHARS_PER_TOKEN = 4  # ~4 chars per token for English text


def get_prompts_dir() -> Path:
    """Get the prompts directory path from package resources."""
    package_prompts = Path(str(resources.files("llm_promptkit").joinpath("prompts")))
    if package_prompts.exists():
        return package_prompts
    # Local repo fallback
    cwd_prompts = Path.cwd() / "prompts"
    if cwd_prompts.exists():
        return cwd_prompts
    return package_prompts


def get_all_prompt_dirs() -> List[Path]:
    """Get all prompt directories: user dirs first, then built-in.

    User dirs take priority over built-in (same-name files override).
    """
    dirs = []
    config = get_config()
    # User dirs first (higher priority)
    for d in config.extra_prompt_dirs:
        if d.is_dir():
            dirs.append(d)
    # Built-in last
    builtin = get_prompts_dir()
    if builtin not in dirs:
        dirs.append(builtin)
    return dirs


def is_prompt_file(path: Path) -> bool:
    """Check if a file is a prompt (not README)."""
    return path.suffix == ".md" and path.stem.lower() != "readme"


def get_prompt_files(directory: Path) -> List[Path]:
    """Get all prompt files in a directory."""
    return sorted([p for p in directory.glob("*.md") if is_prompt_file(p)])


def count_prompts(directory: Path) -> int:
    """Count prompt files in a directory."""
    return len(get_prompt_files(directory))


def get_models_with_prompts(provider_path: Path) -> List[Tuple[str, int]]:
    """Get models that have actual prompts."""
    models = []
    for m in sorted(provider_path.iterdir()):
        if m.is_dir():
            prompt_count = count_prompts(m)
            if prompt_count > 0:
                models.append((m.name, prompt_count))
    return models


def copy_to_clipboard(text: str) -> bool:
    """Copy text to clipboard. Returns True on success."""
    commands = [
        ["xclip", "-selection", "clipboard"],
        ["xsel", "--clipboard", "--input"],
        ["pbcopy"],
    ]
    for cmd in commands:
        try:
            process = subprocess.Popen(cmd, stdin=subprocess.PIPE)
            process.communicate(text.encode())
            if process.returncode == 0:
                return True
        except FileNotFoundError:
            continue
    return False
