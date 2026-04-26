"""Doctor command - analyze prompts for common issues."""

import re
from pathlib import Path
from typing import List, Optional, Tuple

import typer
from rich.table import Table

from llm_promptkit.helpers import console

# Doctor Command Constants
VAGUE_PHRASES = [
    "make it good",
    "do it well",
    "as best as you can",
    "stuff",
    "things",
    "as soon as possible",
    "asap",
    "etc",
    "and so on",
    "whatever you think",
]
ROLE_PHRASES = [
    "you are a",
    "you are an",
    "role:",
    "persona:",
    "act as",
    "system:",
    "<role>",
    "<system_prompt>",
    "<persona>",
]
VERBOSE_PHRASES = [
    "please could you",
    "i would like you to",
    "if you don't mind",
    "can you please",
    "please",
    "thank you",
    "thanks",
    "kindly",
]
FORMAT_PHRASES = [
    "format",
    "json",
    "markdown",
    "output:",
    "structure",
    "return as",
]
EXAMPLE_PHRASES = [
    "example:",
    "example",
    "e.g.",
    "for instance",
    "few-shot",
    "here is an example",
]
NEGATIVE_PHRASES = [
    "don't",
    "do not",
    "never",
    "avoid",
    "must not",
    "stop",
]


def _match_phrase(text: str, phrase: str) -> bool:
    """Check if phrase exists as whole word in text."""
    return bool(re.search(rf"(?<!\w){re.escape(phrase)}(?!\w)", text, re.IGNORECASE))


def _has_any_phrase(text: str, phrases: list) -> bool:
    """Check if any phrase exists in text."""
    return any(_match_phrase(text, p) for p in phrases)


def _print_issues(issues: List[Tuple[str, str, str]]):
    """Print issues as a Rich table."""
    if not issues:
        console.print("[bold green]No issues found. Prompt looks solid.[/bold green]")
        return

    table = Table(title="Prompt Analysis", show_header=True, header_style="bold magenta")
    table.add_column("Severity", style="bold")
    table.add_column("Issue", style="cyan")
    table.add_column("Suggestion", style="green")

    for severity, issue, suggestion in issues:
        table.add_row(severity, issue, suggestion)

    console.print(table)


def doctor_command(
    target: Optional[str] = typer.Argument(None, help="Prompt text string"),
    file: Optional[str] = typer.Option(None, "--file", "-f", help="Read prompt from file"),
):
    """Analyze a prompt for common issues."""
    if file:
        path = Path(file)
        if not path.exists():
            console.print(f"[red]Error: File not found: {file}[/red]")
            raise typer.Exit(code=1)
        text = path.read_text().lower()
        console.print(f"[bold]Analyzing file:[/bold] {file}\n")
    elif target:
        text = target.lower()
        console.print("[bold]Analyzing text prompt...[/bold]\n")
    else:
        console.print("[red]Please provide prompt text or --file.[/red]")
        raise typer.Exit(code=1)

    issues = []

    clean_text = text.strip()

    if not clean_text:
        issues.append(("Error", "Prompt is empty.", "Please provide text to analyze."))
        _print_issues(issues)
        return

    # Strip code blocks for NLP checks
    text_no_code = re.sub(r"```.*?```", "", text, flags=re.DOTALL).strip()

    if len(clean_text) < 20:
        issues.append(
            (
                "Warning",
                "Prompt is very short.",
                "Prompts under 20 characters often lack sufficient detail.",
            )
        )

    if text_no_code:
        # Vague phrases
        for phrase in VAGUE_PHRASES:
            if _match_phrase(text_no_code, phrase):
                issues.append(
                    (
                        "Warning",
                        "Vague or ambiguous instructions.",
                        f"Found '{phrase}'. Be more specific.",
                    )
                )

        # Missing role
        if not _has_any_phrase(text_no_code, ROLE_PHRASES):
            issues.append(
                (
                    "Suggestion",
                    "Missing context or role definition.",
                    "Add a persona (e.g., 'You are an expert...').",
                )
            )

        # Verbose phrasing
        for phrase in VERBOSE_PHRASES:
            if _match_phrase(text_no_code, phrase):
                issues.append(
                    (
                        "Info",
                        "Token inefficiency.",
                        f"Found '{phrase}'. Use direct commands.",
                    )
                )

        # Missing format
        if not _has_any_phrase(text_no_code, FORMAT_PHRASES):
            issues.append(
                (
                    "Warning",
                    "Missing output format.",
                    "Specify format (e.g., 'Output as JSON').",
                )
            )

        # Missing examples
        if not _has_any_phrase(text_no_code, EXAMPLE_PHRASES):
            issues.append(
                (
                    "Info",
                    "No examples provided.",
                    "Few-shot examples improve output quality.",
                )
            )

        # Negative phrasing
        for phrase in NEGATIVE_PHRASES:
            if _match_phrase(text_no_code, phrase):
                issues.append(
                    (
                        "Warning",
                        "Negative constraints.",
                        f"Found '{phrase}'. LLMs follow positive instructions better "
                        f"(e.g., 'Do X' instead of 'Don't do Y').",
                    )
                )
    else:
        issues.append(
            (
                "Info",
                "Prompt contains only code.",
                "No natural language instructions found. Consider adding context or formatting instructions.",
            )
        )

    # Structural formatting check for longer prompts
    if len(clean_text) > 200:
        has_markdown = any(marker in text for marker in ["#", "```", "- ", "* ", "1. "])
        has_xml = bool(re.search(r"<[a-z_]+>", text, re.IGNORECASE))
        if not (has_markdown or has_xml):
            issues.append(
                (
                    "Suggestion",
                    "Lacks structural formatting.",
                    "Long prompt detected without markdown or XML structure. "
                    "Use headers, bullet points, code blocks, or XML tags.",
                )
            )

    _print_issues(issues)
