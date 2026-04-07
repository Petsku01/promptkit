"""CLI for promptkit — build, list, and doctor commands."""

import argparse
from pathlib import Path

from rich.panel import Panel
from rich.table import Table

from .builder import PromptBuilder
from .console import console
from .doctor import analyze_prompt


def list_patterns():
    """List all available patterns."""
    table = Table(title="Available Patterns", show_header=True, header_style="bold magenta")
    table.add_column("Pattern", style="cyan")
    table.add_column("Preview", style="dim")

    for name, text in sorted(PromptBuilder.PATTERNS.items()):
        preview = text[:80].replace("\n", " ") + ("..." if len(text) > 80 else "")
        table.add_row(name, preview)

    console.print(table)


def build_prompt(args):
    """Build a prompt from CLI args."""
    builder = PromptBuilder()

    if args.persona:
        builder.persona(args.persona)

    for pattern_name in args.pattern or []:
        try:
            builder.pattern(pattern_name)
        except ValueError as e:
            console.print(f"[red]Error: {e}[/red]")
            return

    if args.task:
        builder.task(args.task)
    if args.context:
        builder.context(args.context)
    for c in args.constraint or []:
        builder.constraint(c)

    prompt = builder.build()

    if args.tokens:
        console.print(f"[dim]# Estimated tokens: {builder.estimate_tokens()}[/dim]")

    if args.output:
        Path(args.output).write_text(prompt)
        console.print(f"[bold green]Prompt written to {args.output}[/bold green]")
    else:
        console.print(Panel(prompt, title="Generated Prompt", border_style="blue"))


def doctor_command(args):
    """Analyze a prompt for common issues."""
    if args.file:
        path = Path(args.file)
        if not path.exists():
            console.print(f"[red]Error: File not found: {args.file}[/red]")
            return
        text = path.read_text()
    else:
        text = args.target or ""

    issues = analyze_prompt(text.lower())

    if not issues:
        console.print("[bold green]No issues found. Prompt looks solid.[/bold green]")
        return

    table = Table(title="Prompt Analysis", show_header=True, header_style="bold magenta")
    table.add_column("Severity", style="bold")
    table.add_column("Issue", style="cyan")
    table.add_column("Suggestion", style="green")

    for entry in issues:
        table.add_row(entry.severity.value, entry.issue, entry.suggestion)

    console.print(table)


def main():
    """Main entry point for CLI."""
    parser = argparse.ArgumentParser(prog="promptkit", description="Build effective LLM prompts from patterns")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    subparsers.add_parser("list", help="List available patterns")

    build_parser = subparsers.add_parser("build", help="Build a prompt")
    build_parser.add_argument("--persona", "-p", help="AI persona/role")
    build_parser.add_argument("--pattern", "-P", action="append", help="Pattern to use (can repeat)")
    build_parser.add_argument("--task", "-t", help="Task description")
    build_parser.add_argument("--context", "-c", help="Context (code/text)")
    build_parser.add_argument("--constraint", action="append", help="Constraint (can repeat)")
    build_parser.add_argument("--output", "-o", help="Output file")
    build_parser.add_argument("--tokens", action="store_true", help="Show token estimate")

    doctor_parser = subparsers.add_parser("doctor", help="Analyze prompts for common issues")
    doctor_parser.add_argument("target", nargs="?", default="", help="Prompt text string")
    doctor_parser.add_argument("--file", "-f", help="Read prompt from file")

    args = parser.parse_args()

    if args.command == "list":
        list_patterns()
    elif args.command == "doctor":
        doctor_command(args)
    elif args.command == "build":
        build_prompt(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
