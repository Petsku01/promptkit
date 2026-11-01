"""Promptkit CLI — Build effective LLM prompts from patterns."""

import typer

from .commands.build import build_command
from .commands.doctor import doctor_command
from .commands.list import list_command
from .commands.prompts import prompts_command
from .commands.search import search_command

app = typer.Typer(
    name="promptkit",
    help="Build effective LLM prompts from patterns.",
    no_args_is_help=True,
)

@app.callback()
def validate_config() -> None:
    """Report configuration errors consistently for every CLI command."""
    from llm_promptkit.config import ConfigError, get_config

    try:
        get_config()
    except ConfigError as exc:
        typer.echo(f"ConfigError: {exc}", err=True)
        raise typer.Exit(code=2) from exc


# Register commands
app.command(name="list")(list_command)
app.command(name="build")(build_command)
app.command(name="prompts")(prompts_command)
app.command(name="search")(search_command)
app.command(name="doctor")(doctor_command)


def main():
    """Entry point for the CLI."""
    app()


if __name__ == "__main__":
    main()
