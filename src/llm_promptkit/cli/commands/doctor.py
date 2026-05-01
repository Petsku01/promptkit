"""Doctor command - analyze prompts for common issues and optionally fix them."""

import json
import re
import shutil
from pathlib import Path
from typing import List, Optional, Tuple

import typer
from rich.table import Table

from llm_promptkit.helpers import console

# ---------------------------------------------------------------------------
# Doctor phrase lists — private to this module
# ---------------------------------------------------------------------------
_VAGUE_PHRASES = [
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

_ROLE_PHRASES = [
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

_VERBOSE_PHRASES = [
    "please could you",
    "i would like you to",
    "if you don't mind",
    "can you please",
    "please",
    "thank you",
    "thanks",
    "kindly",
]

_FORMAT_PHRASES = [
    "format",
    "json",
    "markdown",
    "output:",
    "structure",
    "return as",
]

_EXAMPLE_PHRASES = [
    "example:",
    "example",
    "e.g.",
    "for instance",
    "few-shot",
    "here is an example",
]

_NEGATIVE_PHRASES = [
    "don't",
    "do not",
    "never",
    "avoid",
    "must not",
    "stop",
]

_AMBIGUOUS_PHRASES = [
    "maybe",
    "possibly",
    "might",
    "perhaps",
    "somewhat",
    "sort of",
    "kind of",
]

_STOP_WORDS_BIGRAM = frozenset({
    "the", "a", "an", "is", "are", "in", "on", "at", "to", "of",
    "for", "and", "or", "it", "this", "that",
})


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------
def _match_phrase(text: str, phrase: str) -> bool:
    """Check if phrase exists as whole word in text."""
    return bool(re.search(rf"(?<!\w){re.escape(phrase)}(?!\w)", text, re.IGNORECASE))


def _has_any_phrase(text: str, phrases: list) -> bool:
    """Check if any phrase exists in text."""
    return any(_match_phrase(text, p) for p in phrases)


def _analyze_prompt(text: str) -> List[Tuple[str, str, str, Optional[int], bool]]:
    """Analyze a prompt and return issues.

    Returns list of (severity, issue, suggestion, line_number, fixable) tuples.
    """
    issues: List[Tuple[str, str, str, Optional[int], bool]] = []
    clean_text = text.strip()

    if not clean_text:
        issues.append(("Error", "Prompt is empty.", "Please provide text to analyze.", None, False))
        return issues

    # Strip code blocks for NLP checks
    text_no_code = re.sub(r"```.*?```", "", text, flags=re.DOTALL).strip()

    if len(clean_text) < 20:
        issues.append(
            (
                "Warning",
                "Prompt is very short.",
                "Prompts under 20 characters often lack sufficient detail.",
                None,
                False,
            )
        )

    if text_no_code:
        # --- Existing heuristics (v0.2.0) ---

        # Vague phrases
        for phrase in _VAGUE_PHRASES:
            if _match_phrase(text_no_code, phrase):
                issues.append(
                    (
                        "Warning",
                        "Vague or ambiguous instructions.",
                        f"Found '{phrase}'. Be more specific.",
                        None,
                        False,
                    )
                )

        # Missing role
        if not _has_any_phrase(text_no_code, _ROLE_PHRASES):
            issues.append(
                (
                    "Suggestion",
                    "Missing context or role definition.",
                    "Add a persona (e.g., 'You are an expert...').",
                    None,
                    False,
                )
            )

        # Verbose phrasing
        for phrase in _VERBOSE_PHRASES:
            if _match_phrase(text_no_code, phrase):
                issues.append(
                    (
                        "Info",
                        "Token inefficiency.",
                        f"Found '{phrase}'. Use direct commands.",
                        None,
                        phrase == "please" or phrase in _VERBOSE_PHRASES[:4],
                    )
                )

        # Missing format
        if not _has_any_phrase(text_no_code, _FORMAT_PHRASES):
            issues.append(
                (
                    "Warning",
                    "Missing output format.",
                    "Specify format (e.g., 'Output as JSON').",
                    None,
                    False,
                )
            )

        # Missing examples
        if not _has_any_phrase(text_no_code, _EXAMPLE_PHRASES):
            issues.append(
                (
                    "Info",
                    "No examples provided.",
                    "Few-shot examples improve output quality.",
                    None,
                    False,
                )
            )

        # Negative phrasing
        for phrase in _NEGATIVE_PHRASES:
            if _match_phrase(text_no_code, phrase):
                issues.append(
                    (
                        "Warning",
                        "Negative constraints.",
                        f"Found '{phrase}'. LLMs follow positive instructions better "
                        f"(e.g., 'Do X' instead of 'Don't do Y').",
                        None,
                        False,
                    )
                )

        # --- New heuristics (v0.3.0) ---

        # Sentence length check
        sentences = re.split(r'[.!?]+', text_no_code)
        for sent in sentences:
            word_count = len(sent.split())
            if word_count > 40:
                line_num = text[: text.find(sent)].count("\n") + 1 if sent in text else None
                issues.append(
                    (
                        "Warning",
                        "Long sentence detected.",
                        f"Sentence has {word_count} words. Break it into shorter sentences (max 40 words).",
                        line_num,
                        False,
                    )
                )
                break  # Only report one long sentence

        # Duplication check (bigram)
        words = text_no_code.lower().split()
        seen_bigrams: set = set()
        for i in range(len(words) - 1):
            bigram = f"{words[i]} {words[i + 1]}"
            if bigram in seen_bigrams and words[i] not in _STOP_WORDS_BIGRAM:
                issues.append(
                    (
                        "Info",
                        "Repeated bigram detected.",
                        f"Found '{bigram}' repeated. Consider using varied phrasing.",
                        None,
                        False,
                    )
                )
                break  # Only report one duplicate
            seen_bigrams.add(bigram)

        # Context boundary check
        for marker in ["Task:", "Context:", "Instructions:", "Task description:"]:
            if marker in text:
                marker_pos = text.find(marker)
                # Content after the marker (before next section or end of text)
                after_all = text[marker_pos + len(marker):]
                # Extract just the section content: up to next blank line or next marker
                section_lines = []
                for line in after_all.lstrip("\n").split("\n"):
                    if line.strip() and not any(
                        line.strip().startswith(m) for m in ["Task:", "Context:", "Instructions:", "Task description:"]
                    ):
                        section_lines.append(line)
                    else:
                        break
                section_content = "\n".join(section_lines).strip()
                if not section_content or len(section_content) < 10:
                    line_num = text[:marker_pos].count("\n") + 1
                    issues.append(
                        (
                            "Suggestion",
                            f"Empty section: '{marker.strip()}'",
                            f"Add content after '{marker.strip()}' or remove the heading.",
                            line_num,
                            False,
                        )
                    )

        # Ambiguous phrasing
        for phrase in _AMBIGUOUS_PHRASES:
            if _match_phrase(text_no_code, phrase):
                issues.append(
                    (
                        "Info",
                        "Ambiguous language.",
                        f"Found '{phrase}'. Use definitive language for clearer instructions.",
                        None,
                        False,
                    )
                )
                break  # Only report one ambiguous phrase

    else:
        issues.append(
            (
                "Info",
                "Prompt contains only code.",
                "No natural language instructions found. Consider adding context or formatting instructions.",
                None,
                False,
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
                    None,
                    False,
                )
            )

    return issues


def _apply_safe_fixes(text: str) -> str:
    """Apply safe, automatic fixes to prompt text.

    Only performs: remove standalone 'please', collapse double whitespace,
    strip trailing whitespace, strip leading/trailing blank lines.
    """
    # Remove standalone 'please' (word boundary, case-insensitive)
    # "Please review" → "Review", "Please, review" → "Review"
    # But NOT "PleaseNote" or "unprecedented"
    text = re.sub(r"\b[Pp]lease\b[,\s]*", "", text)

    # Collapse double (or more) whitespace into single space
    text = re.sub(r"[ \t]{2,}", " ", text)

    # Strip trailing whitespace from each line
    lines = [line.rstrip() for line in text.split("\n")]
    text = "\n".join(lines)

    # Strip leading and trailing blank lines
    text = text.strip()

    return text


def _print_issues_table(issues: List[Tuple[str, str, str, Optional[int], bool]]) -> None:
    """Print issues as a Rich table."""
    if not issues:
        console.print("[bold green]No issues found. Prompt looks solid.[/bold green]")
        return

    table = Table(title="Prompt Analysis", show_header=True, header_style="bold magenta")
    table.add_column("Severity", style="bold")
    table.add_column("Issue", style="cyan")
    table.add_column("Suggestion", style="green")

    for severity, issue, suggestion, _line, _fixable in issues:
        table.add_row(severity, issue, suggestion)

    console.print(table)


def _issues_to_json(text: str, issues: List[Tuple[str, str, str, Optional[int], bool]]) -> str:
    """Convert issues to JSON format."""
    try:
        from llm_promptkit import __version__
        version = __version__
    except Exception:
        version = "0.3.0"

    result = {
        "version": version,
        "input_length": len(text),
        "issues": [
            {
                "severity": severity,
                "issue": issue,
                "suggestion": suggestion,
                "line": line,
                "fixable": fixable,
            }
            for severity, issue, suggestion, line, fixable in issues
        ],
    }
    return json.dumps(result, indent=2)


# ---------------------------------------------------------------------------
# CLI command
# ---------------------------------------------------------------------------
def doctor_command(
    target: Optional[str] = typer.Argument(None, help="Prompt text string"),
    file: Optional[str] = typer.Option(None, "--file", "-f", help="Read prompt from file"),
    fix: bool = typer.Option(False, "--fix", help="Apply safe automatic fixes"),
    dry_run: bool = typer.Option(
        False, "--dry-run", help="Show what would be fixed without making changes"
    ),
    fmt: str = typer.Option("table", "--format", help="Output format: table or json"),
):
    """Analyze a prompt for common issues."""
    # Validate format
    if fmt not in ("table", "json"):
        console.print(f"[red]Invalid format '{fmt}'. Use 'table' or 'json'.[/red]")
        raise typer.Exit(code=1)

    # Validate --fix and --dry-run
    if dry_run and not fix:
        console.print("[yellow]--dry-run requires --fix. Showing analysis only.[/yellow]")
        dry_run = False

    # Read input
    if file and target:
        console.print("[yellow]Both text and --file provided; using --file.[/yellow]")

    source_is_file = False
    file_path = None

    if file:
        path = Path(file).resolve()
        if not path.is_file():
            console.print(f"[red]Error: File not found: {file}[/red]")
            raise typer.Exit(code=1)
        if path.is_dir():
            console.print(f"[red]Error: '{file}' is a directory, not a file.[/red]")
            raise typer.Exit(code=1)
        text = path.read_text()
        source_is_file = True
        file_path = path
        if fmt == "table":
            console.print(f"[bold]Analyzing file:[/bold] {file}\n")
    elif target:
        text = target
        if not text.strip():
            console.print("[red]Empty prompt provided.[/red]")
            raise typer.Exit(code=1)
        if fmt == "table":
            console.print("[bold]Analyzing text prompt...[/bold]\n")
    else:
        console.print("[red]Please provide prompt text or --file.[/red]")
        raise typer.Exit(code=1)

    # Analyze
    issues = _analyze_prompt(text)

    # Output
    if fmt == "json":
        if fix and not source_is_file:
            # JSON + text input + --fix: output single combined JSON
            fixed_text = _apply_safe_fixes(text)
            try:
                from llm_promptkit import __version__ as _ver
            except Exception:
                _ver = "0.3.0"
            fixed_issues = _analyze_prompt(fixed_text)
            result = {
                "version": _ver,
                "input_length": len(text),
                "original_issues": len(issues),
                "remaining_issues": len(fixed_issues),
                "fixed_text": fixed_text,
                "analysis": [
                    {
                        "severity": severity,
                        "issue": issue,
                        "suggestion": suggestion,
                        "line": line,
                        "fixable": fixable,
                    }
                    for severity, issue, suggestion, line, fixable in issues
                ],
                "fixed_analysis": [
                    {
                        "severity": severity,
                        "issue": issue,
                        "suggestion": suggestion,
                        "line": line,
                        "fixable": fixable,
                    }
                    for severity, issue, suggestion, line, fixable in fixed_issues
                ],
            }
            print(json.dumps(result, indent=2))
        else:
            print(_issues_to_json(text, issues))
    else:
        _print_issues_table(issues)

    # Handle --fix / --dry-run
    if fix and source_is_file and file_path is not None:
        fixed_text = _apply_safe_fixes(text)
        if fixed_text == text:
            if fmt == "table":
                console.print("\n[dim]No safe fixes to apply.[/dim]")
        else:
            if dry_run:
                if fmt == "table":
                    console.print("\n[bold yellow]Dry run — would apply these fixes:[/bold yellow]")
                    # Show diff-like view
                    for i, (old, new) in enumerate(
                        zip(text.splitlines(), fixed_text.splitlines())
                    ):
                        if old != new:
                            console.print(f"  [red]- {old}[/red]")
                            console.print(f"  [green]+ {new}[/green]")
            else:
                # Create backup
                backup_path = file_path.with_suffix(file_path.suffix + ".bak")
                shutil.copy2(file_path, backup_path)
                file_path.write_text(fixed_text)
                if fmt == "table":
                    console.print(f"\n[bold green]Fixed![/bold green] Backup saved to {backup_path}")

    elif fix and not source_is_file:
        # Input from argument, table format: print fixed version
        if fmt == "table":
            fixed_text = _apply_safe_fixes(text)
            console.print("\n[bold]Suggested fix:[/bold]")
            console.print(fixed_text)
