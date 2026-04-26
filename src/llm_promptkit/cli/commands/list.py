"""List available prompt patterns."""

import typer

from llm_promptkit.helpers import console
from llm_promptkit.patterns._registry import list_patterns_with_categories, read_pattern


def list_command():
    """List available patterns."""
    header = typer.style("Available Prompt Patterns", bold=True)
    console.print(f"\n{header}\n")

    for name, category in list_patterns_with_categories():
        description = read_pattern(name).split("\n")[0][:60]
        console.print(f"  [cyan]{name}[/cyan]  [green]{description}[/green]")
