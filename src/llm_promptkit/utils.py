"""Shared utility functions and constants for promptkit."""

from importlib import resources
from pathlib import Path
import subprocess
from typing import List, Tuple

# Constants
CHARS_PER_TOKEN = 4  # Rough estimate for token counting

# Doctor Command Constants
VAGUE_PHRASES = [
    "make it good",
    "do it well",
    "as best as you can",
    "stuff",
    "things",
    "as soon as possible",
    "asap",
    "etc",
    "and so on",
    "whatever you think",
]
ROLE_PHRASES = [
    "you are a",
    "you are an",
    "role:",
    "persona:",
    "act as",
    "system:",
    "<role>",
    "<system_prompt>",
    "<persona>",
]
VERBOSE_PHRASES = [
    "please could you",
    "i would like you to",
    "if you don't mind",
    "can you please",
    "please",
    "thank you",
    "thanks",
    "kindly",
]
FORMAT_PHRASES = ["format", "json", "markdown", "output:", "structure", "return as"]
EXAMPLE_PHRASES = ["example:", "example", "e.g.", "for instance", "few-shot", "here is an example"]
NEGATIVE_PHRASES = ["don't", "do not", "never", "avoid", "must not", "stop"]


def get_prompts_dir() -> Path:
    """Get the prompts directory path."""
    package_prompts = Path(str(resources.files("llm_promptkit").joinpath("prompts")))
    if package_prompts.exists():
        return package_prompts

    # Local repo fallback
    cwd_prompts = Path.cwd() / "prompts"
    if cwd_prompts.exists():
        return cwd_prompts
    return package_prompts


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
