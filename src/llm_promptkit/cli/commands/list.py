"""List available patterns and their categories."""

from typing import Optional, Sequence, Tuple

import typer
from rich.table import Table

from llm_promptkit.config import get_config
from llm_promptkit.helpers import console
from llm_promptkit.patterns._registry import (
    get_pattern_source,
    list_patterns_with_categories,
)


def list_command(
    category: Optional[str] = typer.Option(None, "--category", "-c", help="Filter by category"),
    sources: bool = typer.Option(
        False, "--sources", "-s", help="Show source (custom/built-in) for each pattern"
    ),
):
    """List available prompt patterns."""
    if category:
        filtered = [
            (name, cat) for name, cat in list_patterns_with_categories() if cat == category
        ]
        if not filtered:
            console.print(f"[yellow]No patterns found in category '{category}'.[/yellow]")
            console.print(
                f"[dim]Available categories: {', '.join(sorted(set(cat for _, cat in list_patterns_with_categories())))}[/dim]"
            )
            return
        _print_patterns(filtered, show_sources=sources)
    else:
        _print_patterns(list_patterns_with_categories(), show_sources=sources)

    config = get_config()
    if config.extra_pattern_dirs:
        console.print(
            f"\n[dim]Custom pattern dirs: {', '.join(str(d) for d in config.extra_pattern_dirs)}[/dim]"
        )


def _print_patterns(
    patterns: Sequence[Tuple[str, str]], show_sources: bool = False
) -> None:
    """Print patterns in a table."""
    if not patterns:
        console.print("[yellow]No patterns found.[/yellow]")
        return

    table = Table(
        title="Available Patterns",
        show_header=True,
        header_style="bold magenta",
    )
    if show_sources:
        table.add_column("Pattern", style="cyan")
        table.add_column("Category", style="green")
        table.add_column("Source", style="yellow")
        for name, cat in patterns:
            source = get_pattern_source(name)
            tag = f"\\[{source}]"
            table.add_row(name, cat, tag)
    else:
        table.add_column("Pattern", style="cyan")
        table.add_column("Category", style="green")
        for name, cat in patterns:
            table.add_row(name, cat)

    console.print(table)
    console.print(
        f"\n[dim]{len(patterns)} patterns available. "
        f"Use --category to filter, --sources to show origin.[/dim]"
    )
