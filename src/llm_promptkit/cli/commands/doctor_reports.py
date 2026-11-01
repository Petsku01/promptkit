"""Doctor report rendering and a single issue serialization implementation."""

import json
from typing import List

from rich.table import Table

from llm_promptkit import __version__
from llm_promptkit.helpers import console

from .doctor_heuristics import Issue


def serialize_issues(issues: List[Issue]) -> list:
    return [dict(zip(("severity", "issue", "suggestion", "line", "fixable"), issue)) for issue in issues]


def issues_to_json(text: str, issues: List[Issue]) -> str:
    return json.dumps({"version": __version__, "input_length": len(text), "issues": serialize_issues(issues)}, indent=2)


def fixed_report(text: str, issues: List[Issue], fixed_text: str, fixed_issues: List[Issue]) -> str:
    return json.dumps({
        "version": __version__, "input_length": len(text),
        "original_issues": len(issues), "remaining_issues": len(fixed_issues),
        "fixed_text": fixed_text, "analysis": serialize_issues(issues),
        "fixed_analysis": serialize_issues(fixed_issues),
    }, indent=2)


def print_issues_table(issues: List[Issue]) -> None:
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
