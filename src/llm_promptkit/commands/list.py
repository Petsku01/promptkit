"""List command for promptkit."""

from rich.table import Table

from ..builder import PromptBuilder
from ..console import console


def list_patterns():
    """List available patterns."""
    table = Table(title="Available Prompt Patterns", show_header=True, header_style="bold magenta")
    table.add_column("Pattern", style="cyan")
    table.add_column("Description", style="green")

    for name, description in PromptBuilder.PATTERNS.items():
        first_line = description.split("\n")[0][:60]
        table.add_row(name, first_line + ("..." if len(description.split("\n")[0]) > 60 else ""))

    console.print(table)
