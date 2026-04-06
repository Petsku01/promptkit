"""Prompts command for promptkit."""

from pathlib import Path

from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax
from rich.table import Table

from ..builder import PromptBuilder
from ..console import console
from ..utils import CHARS_PER_TOKEN, copy_to_clipboard, get_models_with_prompts, get_prompt_files, get_prompts_dir


from .prompts_state_machine import run_interactive_prompts


def interactive_prompts():
    """Interactive prompt selector with back navigation (state machine version)."""
    from ..utils import get_prompts_dir
    prompts_dir = get_prompts_dir()
    model_dir = prompts_dir / "model-optimized"
    run_interactive_prompts(model_dir)


def list_providers():
    """List available model providers (only those with prompts)."""
    prompts_dir = get_prompts_dir()
    model_dir = prompts_dir / "model-optimized"

    if not model_dir.exists():
        console.print("[red]Model-optimized prompts directory not found.[/red]")
        console.print(f"[dim]Looking in: {model_dir}[/dim]")
        return

    table = Table(title="Available Providers", show_header=True, header_style="bold magenta")
    table.add_column("Provider", style="cyan")
    table.add_column("Models with Prompts", style="dim")
    table.add_column("Total Prompts", style="dim")

    for provider_path in sorted(model_dir.iterdir()):
        if provider_path.is_dir():
            models = get_models_with_prompts(provider_path)
            total_prompts = sum(count for _, count in models)
            if models:
                table.add_row(
                    provider_path.name,
                    str(len(models)),
                    str(total_prompts)
                )

    console.print(table)


def list_model_prompts(provider: str, model: str = None):
    """List prompts for a specific provider/model."""
    prompts_dir = get_prompts_dir()
    provider_path = prompts_dir / "model-optimized" / provider

    if not provider_path.exists():
        console.print(f"[red]Provider '{provider}' not found.[/red]")
        return

    if model:
        # List prompts for specific model
        model_path = provider_path / model
        if not model_path.exists():
            console.print(f"[red]Model '{model}' not found in '{provider}'.[/red]")
            return

        prompt_files = get_prompt_files(model_path)
        if not prompt_files:
            console.print(f"[yellow]No prompts found for {provider}/{model}.[/yellow]")
            return

        table = Table(
            title=f"Prompts for {provider}/{model}",
            show_header=True,
            header_style="bold magenta"
        )
        table.add_column("Name", style="cyan")
        table.add_column("Size", style="dim")

        for pf in prompt_files:
            size_kb = pf.stat().st_size / 1024
            table.add_row(pf.stem, f"{size_kb:.1f} KB")

        console.print(table)
    else:
        # List all models for provider
        models = get_models_with_prompts(provider_path)
        if not models:
            console.print(f"[yellow]No models with prompts found for {provider}.[/yellow]")
            return

        table = Table(
            title=f"Models for {provider}",
            show_header=True,
            header_style="bold magenta"
        )
        table.add_column("Model", style="cyan")
        table.add_column("Prompt Count", style="dim")

        for model_name, prompt_count in models:
            table.add_row(model_name, str(prompt_count))

        console.print(table)


def show_prompt(provider: str, model: str, name: str):
    """Display a specific prompt."""
    prompts_dir = get_prompts_dir()
    prompt_file = prompts_dir / "model-optimized" / provider / model / f"{name}.md"

    if not prompt_file.exists():
        console.print(f"[red]Prompt not found: {provider}/{model}/{name}[/red]")
        return

    content = prompt_file.read_text()

    console.print(Panel(
        Syntax(content, "markdown", theme="monokai", word_wrap=True),
        title=f"{provider}/{model}/{name}",
        border_style="blue"
    ))

    console.print(f"[dim]Estimated tokens: ~{len(content) // CHARS_PER_TOKEN}[/dim]")


def prompts_command(args):
    """Browse model-optimized prompts."""
    if args.show:
        # Parse path like "openai/gpt-4o/coding"
        parts = args.show.split("/")
        if len(parts) == 3:
            show_prompt(parts[0], parts[1], parts[2])
        elif len(parts) == 2:
            list_model_prompts(parts[0], parts[1])
        else:
            console.print("[red]Invalid path. Use: provider/model/name or provider/model[/red]")
    elif args.model:
        # List prompts for specific model
        if "/" in args.model:
            provider, model = args.model.split("/", 1)
            list_model_prompts(provider, model)
        else:
            # Provider specified, list models
            list_model_prompts(args.model)
    elif args.interactive:
        interactive_prompts()
    else:
        list_providers()
