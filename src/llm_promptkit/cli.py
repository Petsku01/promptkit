"""
CLI for prompt-patterns.

Usage:
    prompt-patterns list
    prompt-patterns build --pattern chain-of-thought --task "Review this code"
    prompt-patterns build --interactive
    prompt-patterns prompts
    prompt-patterns prompts --model openai/gpt-4o
    prompt-patterns prompts --show openai/gpt-4o/coding
"""

import argparse
import time
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.progress import track
from rich.prompt import Prompt
from rich.syntax import Syntax
from rich.table import Table

from .builder import PromptBuilder

console = Console()

# Find prompts directory relative to package
def get_prompts_dir() -> Path:
    """Get the prompts directory path."""
    # Try relative to this file (installed package)
    pkg_dir = Path(__file__).parent.parent.parent
    prompts_dir = pkg_dir / "prompts"
    if prompts_dir.exists():
        return prompts_dir
    # Try current working directory
    cwd_prompts = Path.cwd() / "prompts"
    if cwd_prompts.exists():
        return cwd_prompts
    return prompts_dir  # Return default even if not found

def list_patterns():
    """List available patterns."""
    table = Table(title="Available Prompt Patterns", show_header=True, header_style="bold magenta")
    table.add_column("Pattern", style="cyan")
    table.add_column("Description", style="green")

    for name, description in PromptBuilder.PATTERNS.items():
        first_line = description.split("\n")[0][:60]
        table.add_row(name, first_line + ("..." if len(description.split("\n")[0]) > 60 else ""))

    console.print(table)


def build_prompt(args):
    """Build a prompt from arguments."""
    builder = PromptBuilder()

    if args.persona:
        builder.persona(args.persona)

    if args.pattern:
        for pattern in args.pattern:
            builder.pattern(pattern)

    if args.task:
        builder.task(args.task)

    if args.context:
        builder.context(args.context)

    if args.constraint:
        for constraint in args.constraint:
            builder.constraint(constraint)

    # Simulate thinking/processing with progress indicator
    with console.status("[bold green]Building prompt..."):
        time.sleep(0.5)
        prompt = builder.build()

    if args.tokens:
        token_count = builder.estimate_tokens()
        console.print(f"[dim]# Estimated tokens: {token_count}[/dim]")

    if args.output:
        with open(args.output, "w") as f:
            f.write(prompt)
        console.print(f"[bold green]Prompt written to {args.output}[/bold green]")
    else:
        console.print(Panel(prompt, title="Generated Prompt", border_style="blue"))


def interactive_build():
    """Interactive prompt builder."""
    console.print(Panel.fit("Prompt Builder - Interactive Mode", style="bold magenta"))

    builder = PromptBuilder()

    # Persona
    persona = Prompt.ask("Persona (e.g., 'Senior Developer')", default="")
    if persona:
        builder.persona(persona)

    # Patterns
    console.print("\n[bold cyan]Available patterns:[/bold cyan]", ", ".join(PromptBuilder.PATTERNS.keys()))
    patterns_input = Prompt.ask("Patterns (comma-separated)", default="")
    if patterns_input:
        for p in patterns_input.split(","):
            p = p.strip()
            if p:
                try:
                    builder.pattern(p)
                except ValueError as e:
                    console.print(f"[bold red]Warning:[/bold red] {e}")

    # Task
    task = Prompt.ask("\nTask description", default="")
    if task:
        builder.task(task)

    # Context
    context = Prompt.ask("Context (paste code/text)", default="")
    if context:
        builder.context(context)

    # Simulate processing
    for step in track(range(100), description="Generating prompt..."):
        time.sleep(0.005)

    prompt = builder.build()

    console.print("\n")
    console.print(Panel(prompt, title="Generated Prompt", border_style="blue"))
    console.print(f"[dim]Estimated tokens: {builder.estimate_tokens()}[/dim]")


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
                # Count models with actual prompts
                models_with_prompts = 0
                for m in p.iterdir():
                    if m.is_dir():
                        prompt_count = len([pf for pf in m.glob("*.md") if pf.stem.lower() != "readme"])
                        if prompt_count > 0:
                            models_with_prompts += 1
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
            models = []
            for m in sorted(provider_path.iterdir()):
                if m.is_dir():
                    prompt_count = len([p for p in m.glob("*.md") if p.stem.lower() != "readme"])
                    if prompt_count > 0:
                        models.append((m.name, prompt_count))

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
                prompt_files = sorted([p for p in model_path.glob("*.md") if p.stem.lower() != "readme"])

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
                console.print(f"\n[dim]Estimated tokens: ~{len(content) // 4}[/dim]")

                # Copy option
                copy_choice = Prompt.ask("\nCopy to clipboard? [y/n/q]", default="n").strip().lower()
                if copy_choice == "q":
                    return
                if copy_choice == "y":
                    try:
                        import subprocess
                        # Try xclip first, then xsel, then pbcopy (macOS)
                        for cmd in [["xclip", "-selection", "clipboard"], ["xsel", "--clipboard", "--input"], ["pbcopy"]]:
                            try:
                                process = subprocess.Popen(cmd, stdin=subprocess.PIPE)
                                process.communicate(content.encode())
                                if process.returncode == 0:
                                    console.print("[green]Copied to clipboard![/green]")
                                    break
                            except FileNotFoundError:
                                continue
                        else:
                            console.print("[yellow]No clipboard tool found (install xclip or xsel).[/yellow]")
                    except Exception as e:
                        console.print(f"[yellow]Could not copy: {e}[/yellow]")

                # After showing prompt, ask what to do next
                next_action = Prompt.ask("\n[dim]Press Enter to select another prompt, 'b' for back, 'q' to quit[/dim]", default="").strip().lower()
                if next_action == "q":
                    return
                if next_action == "b":
                    break


def list_providers():
    """List available model providers."""
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
            models = [m.name for m in provider_path.iterdir() if m.is_dir()]
            if models:
                table.add_row(
                    provider_path.name,
                    ", ".join(sorted(models)[:4]) + ("..." if len(models) > 4 else "")
                )

    console.print(table)
    console.print("\n[dim]Use: promptkit prompts --model <provider> to list models[/dim]")
    console.print("[dim]Use: promptkit prompts --model <provider>/<model> to list prompts[/dim]")


def list_model_prompts(model_path: str):
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

        for model_subdir in sorted(provider_dir.iterdir()):
            if model_subdir.is_dir():
                prompts = [p.stem for p in model_subdir.glob("*.md") if p.stem.lower() != "readme"]
                table.add_row(model_subdir.name, ", ".join(sorted(prompts)))

        console.print(table)
        console.print(f"\n[dim]Use: promptkit prompts --model {parts[0]}/<model> to list prompts[/dim]")

    elif len(parts) == 2:
        # Provider/model - list prompts
        full_model_dir = prompts_dir / "model-optimized" / parts[0] / parts[1]
        if not full_model_dir.exists():
            console.print(f"[red]Model '{model_path}' not found.[/red]")
            return

        table = Table(title=f"Prompts for {model_path}", show_header=True, header_style="bold magenta")
        table.add_column("Prompt", style="cyan")
        table.add_column("File", style="dim")

        for prompt_file in sorted(full_model_dir.glob("*.md")):
            if prompt_file.stem.lower() != "readme":
                table.add_row(prompt_file.stem, prompt_file.name)

        console.print(table)
        console.print(f"\n[dim]Use: promptkit prompts --show {model_path}/<prompt> to view[/dim]")
    else:
        console.print("[red]Invalid format. Use: provider or provider/model[/red]")


def show_prompt(prompt_path: str):
    """Show a specific prompt."""
    prompts_dir = get_prompts_dir()

    parts = prompt_path.split("/")
    if len(parts) != 3:
        console.print("[red]Invalid format. Use: provider/model/prompt[/red]")
        console.print("[dim]Example: openai/gpt-4o/coding[/dim]")
        return

    provider, model, prompt_name = parts
    prompt_file = prompts_dir / "model-optimized" / provider / model / f"{prompt_name}.md"

    if not prompt_file.exists():
        console.print(f"[red]Prompt '{prompt_path}' not found.[/red]")
        console.print(f"[dim]Looking for: {prompt_file}[/dim]")
        return

    content = prompt_file.read_text()

    # Display with syntax highlighting
    console.print(Panel(
        Syntax(content, "markdown", theme="monokai", word_wrap=True),
        title=f"{provider}/{model}/{prompt_name}",
        border_style="blue"
    ))

    # Show token estimate
    console.print(f"\n[dim]Estimated tokens: ~{len(content) // 4}[/dim]")


def prompts_command(args):
    """Handle prompts subcommand."""
    if args.interactive:
        interactive_prompts()
    elif args.show:
        show_prompt(args.show)
    elif args.model:
        list_model_prompts(args.model)
    else:
        list_providers()


def main():
    parser = argparse.ArgumentParser(
        prog="prompt-patterns",
        description="Build effective LLM prompts from patterns"
    )
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # List command
    subparsers.add_parser("list", help="List available patterns")

    # Build command
    build_parser = subparsers.add_parser("build", help="Build a prompt")
    build_parser.add_argument("--persona", "-p", help="AI persona/role")
    build_parser.add_argument("--pattern", "-P", action="append", help="Pattern to use (can repeat)")
    build_parser.add_argument("--task", "-t", help="Task description")
    build_parser.add_argument("--context", "-c", help="Context (code/text)")
    build_parser.add_argument("--constraint", action="append", help="Constraint (can repeat)")
    build_parser.add_argument("--output", "-o", help="Output file")
    build_parser.add_argument("--tokens", action="store_true", help="Show token estimate")
    build_parser.add_argument("--interactive", "-i", action="store_true", help="Interactive mode")

    # Prompts command
    prompts_parser = subparsers.add_parser("prompts", help="Browse model-optimized prompts")
    prompts_parser.add_argument("--model", "-m", help="Provider or provider/model (e.g., openai or openai/gpt-4o)")
    prompts_parser.add_argument("--show", "-s", help="Show prompt content (e.g., openai/gpt-4o/coding)")
    prompts_parser.add_argument("--interactive", "-i", action="store_true", help="Interactive selection mode")

    args = parser.parse_args()

    if args.command == "list":
        list_patterns()
    elif args.command == "build":
        if args.interactive:
            interactive_build()
        else:
            build_prompt(args)
    elif args.command == "prompts":
        prompts_command(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
