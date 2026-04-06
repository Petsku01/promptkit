"""State machine for interactive prompts selection."""

from enum import Enum, auto
from pathlib import Path
from typing import Optional, Tuple

from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax

from ..console import console
from ..utils import CHARS_PER_TOKEN, copy_to_clipboard, get_models_with_prompts, get_prompt_files


class PromptsState(Enum):
    """States for the interactive prompts state machine."""
    SELECT_PROVIDER = auto()
    SELECT_MODEL = auto()
    SELECT_PROMPT = auto()
    VIEW_PROMPT = auto()
    EXIT = auto()


class PromptsContext:
    """Context object carrying state between transitions."""
    
    def __init__(self, model_dir: Path):
        self.model_dir = model_dir
        self.provider: Optional[str] = None
        self.model: Optional[str] = None
        self.prompt_file: Optional[Path] = None
        self.selected_provider_path: Optional[Path] = None
        self.selected_model_path: Optional[Path] = None


def select_provider(context: PromptsContext) -> Tuple[PromptsState, PromptsContext]:
    """State: Select a provider."""
    providers = []
    for p in sorted(context.model_dir.iterdir()):
        if p.is_dir():
            models_with_prompts = len(get_models_with_prompts(p))
            if models_with_prompts > 0:
                providers.append((p.name, models_with_prompts))
    
    if not providers:
        console.print("[red]No providers with prompts found.[/red]")
        return PromptsState.EXIT, context
    
    console.print("\n[bold cyan]Select a provider:[/bold cyan]")
    for i, (provider, model_count) in enumerate(providers, 1):
        console.print(f"  [dim]{i}.[/dim] [cyan]{provider}[/cyan] [dim]({model_count} models)[/dim]")
    
    provider_choice = Prompt.ask("\nProvider").strip().lower()
    
    if provider_choice == "q":
        return PromptsState.EXIT, context
    if provider_choice == "b":
        console.print("[dim]Already at top level.[/dim]")
        return PromptsState.SELECT_PROVIDER, context
    
    try:
        provider_idx = int(provider_choice) - 1
        if provider_idx < 0 or provider_idx >= len(providers):
            console.print("[red]Invalid selection.[/red]")
            return PromptsState.SELECT_PROVIDER, context
        context.provider = providers[provider_idx][0]
        context.selected_provider_path = context.model_dir / context.provider
        return PromptsState.SELECT_MODEL, context
    except ValueError:
        console.print("[red]Enter a number, 'b' for back, or 'q' to quit.[/red]")
        return PromptsState.SELECT_PROVIDER, context


def select_model(context: PromptsContext) -> Tuple[PromptsState, PromptsContext]:
    """State: Select a model."""
    if not context.selected_provider_path:
        return PromptsState.SELECT_PROVIDER, context
    
    models = get_models_with_prompts(context.selected_provider_path)
    
    if not models:
        console.print(f"[red]No models with prompts found for {context.provider}.[/red]")
        return PromptsState.SELECT_PROVIDER, context
    
    console.print(f"\n[bold cyan]Select a model for {context.provider}:[/bold cyan]")
    for i, (model, prompt_count) in enumerate(models, 1):
        console.print(f"  [dim]{i}.[/dim] [cyan]{model}[/cyan] [dim]({prompt_count} prompts)[/dim]")
    
    model_choice = Prompt.ask("\nModel").strip().lower()
    
    if model_choice == "q":
        return PromptsState.EXIT, context
    if model_choice == "b":
        return PromptsState.SELECT_PROVIDER, context
    
    try:
        model_idx = int(model_choice) - 1
        if model_idx < 0 or model_idx >= len(models):
            console.print("[red]Invalid selection.[/red]")
            return PromptsState.SELECT_MODEL, context
        context.model = models[model_idx][0]
        context.selected_model_path = context.selected_provider_path / context.model
        return PromptsState.SELECT_PROMPT, context
    except ValueError:
        console.print("[red]Enter a number, 'b' for back, or 'q' to quit.[/red]")
        return PromptsState.SELECT_MODEL, context


def select_prompt(context: PromptsContext) -> Tuple[PromptsState, PromptsContext]:
    """State: Select a specific prompt."""
    if not context.selected_model_path:
        return PromptsState.SELECT_MODEL, context
    
    prompt_files = get_prompt_files(context.selected_model_path)
    
    if not prompt_files:
        console.print(f"[red]No prompts found for {context.provider}/{context.model}.[/red]")
        return PromptsState.SELECT_MODEL, context
    
    console.print(f"\n[bold cyan]Select a prompt for {context.provider}/{context.model}:[/bold cyan]")
    for i, pf in enumerate(prompt_files, 1):
        console.print(f"  [dim]{i}.[/dim] [cyan]{pf.stem}[/cyan]")
    
    prompt_choice = Prompt.ask("\nPrompt").strip().lower()
    
    if prompt_choice == "q":
        return PromptsState.EXIT, context
    if prompt_choice == "b":
        return PromptsState.SELECT_MODEL, context
    
    try:
        prompt_idx = int(prompt_choice) - 1
        if prompt_idx < 0 or prompt_idx >= len(prompt_files):
            console.print("[red]Invalid selection.[/red]")
            return PromptsState.SELECT_PROMPT, context
        context.prompt_file = prompt_files[prompt_idx]
        return PromptsState.VIEW_PROMPT, context
    except ValueError:
        console.print("[red]Enter a number, 'b' for back, or 'q' to quit.[/red]")
        return PromptsState.SELECT_PROMPT, context


def view_prompt(context: PromptsContext) -> Tuple[PromptsState, PromptsContext]:
    """State: View selected prompt and handle post-view actions."""
    if not context.prompt_file:
        return PromptsState.SELECT_PROMPT, context
    
    content = context.prompt_file.read_text()
    
    console.print("\n")
    console.print(Panel(
        Syntax(content, "markdown", theme="monokai", word_wrap=True),
        title=f"{context.provider}/{context.model}/{context.prompt_file.stem}",
        border_style="blue"
    ))
    console.print(f"\n[dim]Estimated tokens: ~{len(content) // CHARS_PER_TOKEN}[/dim]")
    
    # Copy option
    copy_choice = Prompt.ask("\nCopy to clipboard? [y/n/q]", default="n").strip().lower()
    if copy_choice == "q":
        return PromptsState.EXIT, context
    if copy_choice == "y":
        if copy_to_clipboard(content):
            console.print("[green]Copied to clipboard![/green]")
        else:
            console.print("[yellow]No clipboard tool found (install xclip or xsel).[/yellow]")
    
    # Next action
    next_action = Prompt.ask(
        "\n[dim]Press Enter to select another prompt, 'b' for back, 'q' to quit[/dim]",
        default=""
    ).strip().lower()
    
    if next_action == "q":
        return PromptsState.EXIT, context
    if next_action == "b":
        return PromptsState.SELECT_PROMPT, context
    
    # Default: stay in view mode (can view same prompt again or select new)
    return PromptsState.SELECT_PROMPT, context


def run_interactive_prompts(model_dir: Path) -> None:
    """Run the interactive prompts state machine."""
    if not model_dir.exists():
        console.print("[red]Model-optimized prompts directory not found.[/red]")
        return
    
    console.print(Panel.fit("Prompt Selector", style="bold magenta"))
    console.print("[dim]Enter number to select, 'b' to go back, 'q' to quit[/dim]")
    
    context = PromptsContext(model_dir)
    state = PromptsState.SELECT_PROVIDER
    
    while state != PromptsState.EXIT:
        if state == PromptsState.SELECT_PROVIDER:
            state, context = select_provider(context)
        elif state == PromptsState.SELECT_MODEL:
            state, context = select_model(context)
        elif state == PromptsState.SELECT_PROMPT:
            state, context = select_prompt(context)
        elif state == PromptsState.VIEW_PROMPT:
            state, context = view_prompt(context)
        else:
            break
