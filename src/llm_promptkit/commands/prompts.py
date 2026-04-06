"""Prompts command for promptkit."""

from pathlib import Path

from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax
from rich.table import Table

from ..builder import PromptBuilder
from ..console import console
from ..utils import CHARS_PER_TOKEN, copy_to_clipboard, get_models_with_prompts, get_prompt_files, get_prompts_dir


def interactive_prompts():
    """Interactive prompt selector with back navigation."""
    prompts_dir = get_prompts_dir()
    model_dir = prompts_dir / "model-optimized"

    if not model_dir.exists():
        console.print("[red]Model-optimized prompts directory not found.[/red]")
        return

    console.print(Panel.fit("Prompt Selector", style="bold magenta"))
    console.print("[dim]Enter number to select, 'b' to go back, 'q' to quit[/dim]")

    while True:
        # Step 1: Select provider (only those with models that have prompts)
        providers = []
        for p in sorted(model_dir.iterdir()):
            if p.is_dir():
                models_with_prompts = len(get_models_with_prompts(p))
                if models_with_prompts > 0:
                    providers.append((p.name, models_with_prompts))

        console.print("\n[bold cyan]Select a provider:[/bold cyan]")
        for i, (provider, model_count) in enumerate(providers, 1):
            console.print(f"  [dim]{i}.[/dim] [cyan]{provider}[/cyan] [dim]({model_count} models)[/dim]")

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

        # Step 2: Select model (only those with prompts)
        while True:
            provider_path = model_dir / selected_provider
            models = get_models_with_prompts(provider_path)

            if not models:
                console.print(f"[red]No models with prompts found for {selected_provider}.[/red]")
                break

            console.print(f"\n[bold cyan]Select a model for {selected_provider}:[/bold cyan]")
            for i, (model, prompt_count) in enumerate(models, 1):
                console.print(f"  [dim]{i}.[/dim] [cyan]{model}[/cyan] [dim]({prompt_count} prompts)[/dim]")

            model_choice = Prompt.ask("\nModel").strip().lower()
            if model_choice == "q":
                return
            if model_choice == "b":
                break  # Back to provider selection
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
                    console.print(f"[red]No prompts found for {selected_provider}/{selected_model}.[/red]")
                    break

                console.print(f"\n[bold cyan]Select a prompt for {selected_provider}/{selected_model}:[/bold cyan]")
                for i, pf in enumerate(prompt_files, 1):
                    console.print(f"  [dim]{i}.[/dim] [cyan]{pf.stem}[/cyan]")

                prompt_choice = Prompt.ask("\nPrompt").strip().lower()
                if prompt_choice == "q":
                    return
                if prompt_choice == "b":
                    break  # Back to model selection
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
                console.print(Panel(
                    Syntax(content, "markdown", theme="monokai", word_wrap=True),
                    title=f"{selected_provider}/{selected_model}/{selected_prompt.stem}",
                    border_style="blue"
                ))
                console.print(f"\n[dim]Estimated tokens: ~{len(content) // CHARS_PER_TOKEN}[/dim]")

                # Copy option
                copy_choice = Prompt.ask("\nCopy to clipboard? [y/n/q]", default="n").strip().lower()
                if copy_choice == "q":
                    return
                if copy_choice == "y":
                    if copy_to_clipboard(content):
                        console.print("[green]Copied to clipboard![/green]")
                    else:
                        console.print("[yellow]No clipboard tool found (install xclip or xsel).[/yellow]")

                # After showing prompt, ask what to do next
                next_action = Prompt.ask("\n[dim]Press Enter to select another prompt, 'b' for back, 'q' to quit[/dim]", default="").strip().lower()
                if next_action == "q":
                    return
                if next_action == "b":
                    break


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
