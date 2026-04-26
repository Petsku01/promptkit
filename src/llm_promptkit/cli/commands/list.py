"""List available prompt patterns."""

import typer

from llm_promptkit.helpers import console
from llm_promptkit.patterns._registry import get_pattern_description, list_patterns_with_categories


def list_command():
    """List available patterns."""
    header = typer.style("Available Prompt Patterns", bold=True)
    console.print(f"\n{header}\n")

    for name, category in list_patterns_with_categories():
        description = get_pattern_description(name)
        console.print(f"  [cyan]{name}[/cyan]  [green]{description}[/green]")
