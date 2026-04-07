"""Shared utility functions for promptkit."""

import subprocess

CHARS_PER_TOKEN = 4  # Rough estimate for token counting


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
