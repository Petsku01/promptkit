"""List available prompt patterns."""

import typer

from llm_promptkit.builder import PromptBuilder
from llm_promptkit.helpers import console


def list_command():
    """List available patterns."""
    table = typer.style("Available Prompt Patterns", bold=True)
    console.print(f"\n{table}\n")

    for name, description in PromptBuilder.PATTERNS.items():
        first_line = description.split("\n")[0][:60]
        console.print(f"  [cyan]{name}[/cyan]  [green]{first_line}[/green]")
