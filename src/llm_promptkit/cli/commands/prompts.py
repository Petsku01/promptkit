"""Prompts command - browse and view model-optimized prompts."""

from typing import List, Optional

import typer
from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax
from rich.table import Table

from llm_promptkit.helpers import (
    CHARS_PER_TOKEN,
    console,
    copy_to_clipboard,
    get_all_prompt_dirs,
    get_models_with_prompts,
    get_prompt_files,
    get_prompts_dir,
)


def prompts_command(
    model: Optional[str] = typer.Option(
        None, "--model", "-m", help="Provider or provider/model (e.g., openai or openai/gpt-4o)"
    ),
    show: Optional[str] = typer.Option(
        None, "--show", "-s", help="Show prompt content (e.g., openai/gpt-4o/coding)"
    ),
    interactive: bool = typer.Option(
        False, "--interactive", "-i", help="Interactive selection mode"
    ),
):
    """Browse model-optimized prompts."""
    if interactive:
        _interactive_prompts()
    elif show:
        _show_prompt(show)
    elif model:
        _list_model_prompts(model)
    else:
        _list_providers()


def _find_prompt_file(parts: List[str]) -> Optional[tuple]:
    """Find a prompt file across all prompt directories.

    Returns (filepath, source) or None.
    User directories are checked first.
    """
    all_dirs = get_all_prompt_dirs()
    filename = f"{parts[-1]}.md"
    subpath = "/".join(parts[:-1])

    for prompt_dir in all_dirs:
        source = "custom" if prompt_dir != all_dirs[-1] else "built-in"
        target_dir = prompt_dir / subpath if subpath else prompt_dir
        candidate = target_dir / filename
        if candidate.is_file():
            return (candidate, source)
    return None


def _list_providers():
    """List available model providers (only those with prompts)."""
    # Use built-in for provider listing (user dirs typically don't have model-optimized structure)
    prompts_dir = get_prompts_dir()
    model_dir = prompts_dir / "model-optimized"

    if not model_dir.exists():
        console.print("[red]Model-optimized prompts directory not found.[/red]")
        console.print(f"[dim]Looking in: {model_dir}[/dim]")
        return

    table = Table(title="Available Providers", show_header=True, header_style="bold magenta")
    table.add_column("Provider", style="cyan")
    table.add_column("Models", style="green")

    for provider_path in sorted(model_dir.iterdir()):
        if provider_path.is_dir():
            models = get_models_with_prompts(provider_path)
            if models:
                model_names = [m[0] for m in models]
                table.add_row(
                    provider_path.name,
                    ", ".join(model_names[:4]) + ("..." if len(models) > 4 else ""),
                )

    console.print(table)
    console.print("\n[dim]Use: promptkit prompts --model <provider> to list models[/dim]")
    console.print("[dim]Use: promptkit prompts --model <provider>/<model> to list prompts[/dim]")


def _list_model_prompts(model_path: str):
    """List available prompts for a specific model."""
    prompts_dir = get_prompts_dir()
    parts = model_path.split("/")

    if len(parts) == 1:
        # Just provider - list models
        provider_dir = prompts_dir / "model-optimized" / parts[0]
        if not provider_dir.exists():
            console.print(f"[red]Provider '{parts[0]}' not found.[/red]")
            return

        table = Table(title=f"Models for {parts[0]}", show_header=True, header_style="bold magenta")
        table.add_column("Model", style="cyan")
        table.add_column("Prompts", style="green")

        for model_name, prompt_count in get_models_with_prompts(provider_dir):
            prompts = get_prompt_files(provider_dir / model_name)
            table.add_row(model_name, ", ".join(p.stem for p in prompts))

        console.print(table)
        console.print(
            f"\n[dim]Use: promptkit prompts --model {parts[0]}/<model> to list prompts[/dim]"
        )

    elif len(parts) == 2:
        # Provider/model - list prompts
        full_model_dir = prompts_dir / "model-optimized" / parts[0] / parts[1]
        if not full_model_dir.exists():
            console.print(f"[red]Model '{model_path}' not found.[/red]")
            return

        table = Table(
            title=f"Prompts for {model_path}", show_header=True, header_style="bold magenta"
        )
        table.add_column("Prompt", style="cyan")
        table.add_column("File", style="dim")

        for prompt_file in get_prompt_files(full_model_dir):
            table.add_row(prompt_file.stem, prompt_file.name)

        console.print(table)
        console.print(f"\n[dim]Use: promptkit prompts --show {model_path}/<prompt> to view[/dim]")
    else:
        console.print("[red]Invalid format. Use: provider or provider/model[/red]")


def _show_prompt(prompt_path: str):
    """Show a specific prompt."""
    parts = prompt_path.split("/")

    if len(parts) < 2:
        console.print("[red]Invalid format. Use: provider/model/prompt or category/prompt[/red]")
        console.print("[dim]Example: openai/gpt-4o/coding[/dim]")
        return

    result = _find_prompt_file(parts)
    if result is None:
        console.print(f"[red]Prompt '{prompt_path}' not found.[/red]")
        console.print("[dim]Searched in built-in and custom prompt directories.[/dim]")
        return

    prompt_file, source = result
    content = prompt_file.read_text()
    source_tag = f" [{source}]" if source == "custom" else ""

    console.print(
        Panel(
            Syntax(content, "markdown", theme="monokai", word_wrap=True),
            title=f"{prompt_path}{source_tag}",
            border_style="blue",
        )
    )
    console.print(f"\n[dim]Estimated tokens: ~{len(content) // CHARS_PER_TOKEN}[/dim]")


def _interactive_prompts():
    """Interactive prompt selector with back navigation."""
    prompts_dir = get_prompts_dir()
    model_dir = prompts_dir / "model-optimized"

    if not model_dir.exists():
        console.print("[red]Model-optimized prompts directory not found.[/red]")
        return

    console.print(Panel.fit("Prompt Selector", style="bold magenta"))
    console.print("[dim]Enter number to select, 'b' to go back, 'q' to quit[/dim]")

    while True:
        # Step 1: Select provider
        providers = []
        for p in sorted(model_dir.iterdir()):
            if p.is_dir():
                models_with_prompts = len(get_models_with_prompts(p))
                if models_with_prompts > 0:
                    providers.append((p.name, models_with_prompts))

        console.print("\n[bold cyan]Select a provider:[/bold cyan]")
        for i, (provider, model_count) in enumerate(providers, 1):
            console.print(
                f"  [dim]{i}.[/dim] [cyan]{provider}[/cyan] [dim]({model_count} models)[/dim]"
            )

        provider_choice = Prompt.ask("\nProvider").strip().lower()
        if provider_choice == "q":
            return
        if provider_choice == "b":
            console.print("[dim]Already at top level.[/dim]")
            continue
        try:
            provider_idx = int(provider_choice) - 1
            if provider_idx < 0 or provider_idx >= len(providers):
                console.print("[red]Invalid selection.[/red]")
                continue
            selected_provider = providers[provider_idx][0]
        except ValueError:
            console.print("[red]Enter a number, 'b' for back, or 'q' to quit.[/red]")
            continue

        # Step 2: Select model
        while True:
            provider_path = model_dir / selected_provider
            models = get_models_with_prompts(provider_path)

            if not models:
                console.print(f"[red]No models with prompts found for {selected_provider}.[/red]")
                break

            console.print(f"\n[bold cyan]Select a model for {selected_provider}:[/bold cyan]")
            for i, (model, prompt_count) in enumerate(models, 1):
                console.print(
                    f"  [dim]{i}.[/dim] [cyan]{model}[/cyan] [dim]({prompt_count} prompts)[/dim]"
                )

            model_choice = Prompt.ask("\nModel").strip().lower()
            if model_choice == "q":
                return
            if model_choice == "b":
                break
            try:
                model_idx = int(model_choice) - 1
                if model_idx < 0 or model_idx >= len(models):
                    console.print("[red]Invalid selection.[/red]")
                    continue
                selected_model = models[model_idx][0]
            except ValueError:
                console.print("[red]Enter a number, 'b' for back, or 'q' to quit.[/red]")
                continue

            # Step 3: Select prompt
            while True:
                model_path = provider_path / selected_model
                prompt_files = get_prompt_files(model_path)

                if not prompt_files:
                    console.print(
                        f"[red]No prompts found for {selected_provider}/{selected_model}.[/red]"
                    )
                    break

                console.print(
                    f"\n[bold cyan]Select a prompt for {selected_provider}/{selected_model}:[/bold cyan]"
                )
                for i, pf in enumerate(prompt_files, 1):
                    console.print(f"  [dim]{i}.[/dim] [cyan]{pf.stem}[/cyan]")

                prompt_choice = Prompt.ask("\nPrompt").strip().lower()
                if prompt_choice == "q":
                    return
                if prompt_choice == "b":
                    break
                try:
                    prompt_idx = int(prompt_choice) - 1
                    if prompt_idx < 0 or prompt_idx >= len(prompt_files):
                        console.print("[red]Invalid selection.[/red]")
                        continue
                    selected_prompt = prompt_files[prompt_idx]
                except ValueError:
                    console.print("[red]Enter a number, 'b' for back, or 'q' to quit.[/red]")
                    continue

                # Show the selected prompt
                content = selected_prompt.read_text()
                console.print("\n")
                console.print(
                    Panel(
                        Syntax(content, "markdown", theme="monokai", word_wrap=True),
                        title=f"{selected_provider}/{selected_model}/{selected_prompt.stem}",
                        border_style="blue",
                    )
                )
                console.print(f"\n[dim]Estimated tokens: ~{len(content) // CHARS_PER_TOKEN}[/dim]")

                # Copy option
                copy_choice = (
                    Prompt.ask("\nCopy to clipboard? [y/n/q]", default="n").strip().lower()
                )
                if copy_choice == "q":
                    return
                if copy_choice == "y":
                    if copy_to_clipboard(content):
                        console.print("[green]Copied to clipboard![/green]")
                    else:
                        console.print(
                            "[yellow]No clipboard tool found (install xclip or xsel).[/yellow]"
                        )

                # Next action
                next_action = (
                    Prompt.ask(
                        "\n[dim]Press Enter to select another prompt, 'b' for back, 'q' to quit[/dim]",
                        default="",
                    )
                    .strip()
                    .lower()
                )
                if next_action == "q":
                    return
                if next_action == "b":
                    break
