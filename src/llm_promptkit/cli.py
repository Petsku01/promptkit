"""
CLI for prompt-patterns.

Usage:
    prompt-patterns list
    prompt-patterns build --pattern chain-of-thought --task "Review this code"
    prompt-patterns build --interactive
"""

import argparse
import time

from rich.console import Console
from rich.panel import Panel
from rich.progress import track
from rich.prompt import Prompt
from rich.table import Table

from .builder import PromptBuilder

console = Console()

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

    args = parser.parse_args()

    if args.command == "list":
        list_patterns()
    elif args.command == "build":
        if args.interactive:
            interactive_build()
        else:
            build_prompt(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
