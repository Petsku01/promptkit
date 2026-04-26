"""Build prompts from patterns and personas."""

from typing import Optional

import typer
from rich.panel import Panel
from rich.prompt import Prompt

from llm_promptkit.builder import PromptBuilder
from llm_promptkit.helpers import console
from llm_promptkit.patterns._registry import PatternNotFoundError, list_pattern_names


def build_command(
    persona: Optional[str] = typer.Option(None, "--persona", "-p", help="AI persona/role"),
    pattern: Optional[list[str]] = typer.Option(
        None, "--pattern", "-P", help="Pattern to use (can repeat)"
    ),
    task: Optional[str] = typer.Option(None, "--task", "-t", help="Task description"),
    context: Optional[str] = typer.Option(None, "--context", "-c", help="Context (code/text)"),
    constraint: Optional[list[str]] = typer.Option(
        None, "--constraint", help="Constraint (can repeat)"
    ),
    output: Optional[str] = typer.Option(None, "--output", "-o", help="Output file"),
    tokens: bool = typer.Option(False, "--tokens", help="Show token estimate"),
    interactive: bool = typer.Option(False, "--interactive", "-i", help="Interactive mode"),
):
    """Build a prompt from patterns and options."""
    if interactive:
        _interactive_build()
        return

    builder = PromptBuilder()

    if persona:
        builder.persona(persona)

    if pattern:
        for p in pattern:
            try:
                builder.pattern(p)
            except (ValueError, PatternNotFoundError) as e:
                console.print(f"[red]Error: {e}[/red]")
                raise typer.Exit(code=1)

    if task:
        builder.task(task)

    if context:
        builder.context(context)

    if constraint:
        for c in constraint:
            builder.constraint(c)

    result = builder.build()

    if tokens:
        token_count = builder.estimate_tokens()
        console.print(f"[dim]# Estimated tokens: {token_count}[/dim]")

    if output:
        with open(output, "w") as f:
            f.write(result)
        console.print(f"[bold green]Prompt written to {output}[/bold green]")
    else:
        console.print(Panel(result, title="Generated Prompt", border_style="blue"))


def _interactive_build():
    """Interactive prompt builder."""
    console.print(Panel.fit("Prompt Builder - Interactive Mode", style="bold magenta"))

    builder = PromptBuilder()

    # Persona
    persona = Prompt.ask("Persona (e.g., 'Senior Developer')", default="")
    if persona:
        builder.persona(persona)

    # Patterns
    console.print(f"\n[bold cyan]Available patterns:[/bold cyan] {', '.join(list_pattern_names())}")
    patterns_input = Prompt.ask("Patterns (comma-separated)", default="")
    if patterns_input:
        for p in patterns_input.split(","):
            p = p.strip()
            if p:
                try:
                    builder.pattern(p)
                except (ValueError, PatternNotFoundError) as e:
                    console.print(f"[bold red]Warning:[/bold red] {e}")

    # Task
    task = Prompt.ask("\nTask description", default="")
    if task:
        builder.task(task)

    # Context
    context = Prompt.ask("Context (paste code/text)", default="")
    if context:
        builder.context(context)

    prompt = builder.build()

    console.print("\n")
    console.print(Panel(prompt, title="Generated Prompt", border_style="blue"))
    console.print(f"[dim]Estimated tokens: {builder.estimate_tokens()}[/dim]")
