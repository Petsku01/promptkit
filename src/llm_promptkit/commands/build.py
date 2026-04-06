"""Build command for promptkit."""

from rich.panel import Panel
from rich.prompt import Prompt

from ..builder import PromptBuilder
from ..console import console


def build_prompt(args):
    """Build a prompt from arguments."""
    builder = PromptBuilder()

    if args.persona:
        builder.persona(args.persona)

    if args.pattern:
        for pattern in args.pattern:
            try:
                builder.pattern(pattern)
            except ValueError as e:
                console.print(f"[red]Error: {e}[/red]")
                return

    if args.task:
        builder.task(args.task)

    if args.context:
        builder.context(args.context)

    if args.constraint:
        for constraint in args.constraint:
            builder.constraint(constraint)

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
    console.print("\n[bold cyan]Available patterns:[/bold cyan]", ", ".join(PromptBuilder.PATTERNS.keys()))
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

    prompt = builder.build()

    console.print("\n")
    console.print(Panel(prompt, title="Generated Prompt", border_style="blue"))
    console.print(f"[dim]Estimated tokens: {builder.estimate_tokens()}[/dim]")
