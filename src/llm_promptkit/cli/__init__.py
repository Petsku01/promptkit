"""Promptkit CLI — Build effective LLM prompts from patterns."""

import typer

from llm_promptkit.helpers import (  # noqa: F401
    CHARS_PER_TOKEN,
    console,
    copy_to_clipboard,
    count_prompts,
    get_models_with_prompts,
    get_prompt_files,
    get_prompts_dir,
    is_prompt_file,
)

from .commands.build import _interactive_build as interactive_build  # noqa: F401
from .commands.build import build_command

# Re-exports for backward compatibility with tests
from .commands.build import build_command as build_prompt  # noqa: F401
from .commands.doctor import (  # noqa: F401
    EXAMPLE_PHRASES,
    FORMAT_PHRASES,
    NEGATIVE_PHRASES,
    ROLE_PHRASES,
    VAGUE_PHRASES,
    VERBOSE_PHRASES,
    _has_any_phrase,
    _match_phrase,
    _print_issues,
    doctor_command,
)
from .commands.doctor import doctor_command as doctor_command_fn  # noqa: F401
from .commands.list import list_command
from .commands.list import list_command as list_patterns  # noqa: F401
from .commands.prompts import _interactive_prompts as interactive_prompts  # noqa: F401
from .commands.prompts import _list_model_prompts as list_model_prompts  # noqa: F401
from .commands.prompts import _list_providers as list_providers  # noqa: F401
from .commands.prompts import _show_prompt as show_prompt  # noqa: F401
from .commands.prompts import prompts_command
from .commands.prompts import prompts_command as prompts_command_fn  # noqa: F401
from .commands.search import (
    search_command,
    search_prompts,  # noqa: F401
)
from .commands.search import search_command as search_command_fn  # noqa: F401

app = typer.Typer(
    name="promptkit",
    help="Build effective LLM prompts from patterns.",
    no_args_is_help=True,
)

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
