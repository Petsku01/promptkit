"""Doctor command: input contracts and safe, atomic prompt corrections."""

import json
import os
import re
import shutil
import tempfile
from pathlib import Path
from typing import Optional

import typer

from llm_promptkit.helpers import console

# Keep historical private imports available to existing callers/tests.
from .doctor_heuristics import _has_any_phrase, _match_phrase  # noqa: F401
from .doctor_heuristics import analyze_prompt as _analyze_prompt
from .doctor_reports import fixed_report
from .doctor_reports import issues_to_json as _issues_to_json
from .doctor_reports import print_issues_table as _print_issues_table

_BOUNDARY_RE = re.compile(r"(?:#{1,6}[ \t]+)?(?:Task|Context|Instructions|Task description):[ \t]*$", re.I)
_FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})")


def _prose_fix(text: str) -> str:
    """Fix prose only; never consume a newline while removing a word."""
    lines = text.splitlines(keepends=True)
    result = []
    for index, line in enumerate(lines):
        if _BOUNDARY_RE.fullmatch(line.strip()):
            following = lines[index + 1].strip() if index + 1 < len(lines) else ""
            if not following or _BOUNDARY_RE.fullmatch(following):
                continue
        line = re.sub(r"\bplease\b[, \t]*", "", line, flags=re.IGNORECASE)
        line = re.sub(r"[ \t]{2,}", " ", line)
        line = re.sub(r"[ \t]+(?=\r?\n|$)", "", line)
        result.append(line)
    return "".join(result)


def _apply_safe_fixes(text: str) -> str:
    """Preserve fenced regions (including fences/newlines) byte for byte.

    Accept backtick/tilde fences of any length >=3, indented <=3 spaces.
    An unclosed fence protects the rest of the input as code.
    """
    segments = []
    prose: list[str] = []
    code = []
    fence = ""
    for line in text.splitlines(keepends=True):
        if fence:
            code.append(line)
            if re.fullmatch(r" {0,3}" + re.escape(fence[0]) + "{" + str(len(fence)) + r",}[ \t]*(?:\r?\n)?", line):
                segments.append((True, "".join(code)))
                code = []
                fence = ""
            continue
        match = _FENCE_RE.match(line)
        if match:
            if prose:
                segments.append((False, _prose_fix("".join(prose))))
                prose = []
            fence = match.group(1)
            code.append(line)
        else:
            prose.append(line)
    if code:
        segments.append((True, "".join(code)))
    if prose:
        segments.append((False, _prose_fix("".join(prose))))
    # Trim only the external prose, not a fence's own whitespace/newline.
    if segments and not segments[0][0]:
        segments[0] = (False, segments[0][1].lstrip())
    if segments and not segments[-1][0]:
        segments[-1] = (False, segments[-1][1].rstrip())
    return "".join(value for _, value in segments)


def _atomic_fix(file_path: Path, fixed_text: str) -> Path:
    """Reserve a unique backup exclusively, then replace from the same directory."""
    backup_base = Path(str(file_path) + ".bak")
    number = 0
    while True:
        backup_path = backup_base if number == 0 else Path(f"{backup_base}.{number}")
        try:
            backup = backup_path.open("xb")
        except FileExistsError:
            number += 1
            continue
        try:
            with backup, file_path.open("rb") as source:
                shutil.copyfileobj(source, backup)
            shutil.copystat(file_path, backup_path)
        except OSError:
            backup_path.unlink(missing_ok=True)
            raise
        break
    temp_path = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", newline="", dir=file_path.parent, prefix=f".{file_path.name}.", delete=False) as temporary:
            temp_path = Path(temporary.name)
            temporary.write(fixed_text)
            temporary.flush()
            os.fsync(temporary.fileno())
        shutil.copymode(file_path, temp_path)
        os.replace(temp_path, file_path)
    finally:
        if temp_path is not None:
            temp_path.unlink(missing_ok=True)
    return backup_path


def _error(message: str, fmt: str, code: int = 2) -> None:
    if fmt == "json":
        typer.echo(json.dumps({"error": message}, ensure_ascii=False))
    else:
        typer.echo(message, err=True)
    raise typer.Exit(code=code)


def doctor_command(
    target: Optional[str] = typer.Argument(None, help="Prompt text string or existing file"),
    file: Optional[str] = typer.Option(None, "--file", "-f", help="Read prompt from file"),
    fix: bool = typer.Option(False, "--fix", help="Apply safe automatic fixes"),
    dry_run: bool = typer.Option(False, "--dry-run", help="Show fixes without making changes"),
    fmt: str = typer.Option("table", "--format", help="Output format: table or json"),
):
    """Analyze a prompt for common issues."""
    if fmt not in ("table", "json"):
        _error(f"Invalid format '{fmt}'. Use 'table' or 'json'.", "table", 1)
    if file is not None and target is not None:
        _error("Anna EITHER text TAI --file", fmt)
    if dry_run and not fix:
        typer.echo("--dry-run requires --fix. Showing analysis only.", err=True)
        dry_run = False

    file_path = None
    try:
        if file is not None:
            file_path = Path(file).resolve()
        elif target is not None and "\n" not in target:
            # A long literal prompt is not an invalid filename error.
            try:
                if Path(target).is_file():
                    file_path = Path(target).resolve()
            except OSError:
                pass
        if file_path is not None:
            if not file_path.is_file():
                _error(f"Error: File not found: {file or target}", fmt, 1)
            # read_text's universal newline conversion would alter fenced bytes.
            with file_path.open("r", encoding="utf-8", newline="") as source:
                text = source.read()
            if not text.strip():
                _error("empty" if fmt == "json" else "tyhjä prompt — mitään analyysoitavissa", fmt)
        elif target is not None:
            text = target
            if not text.strip():
                _error("Empty prompt provided.", fmt, 1)
        else:
            _error("Please provide prompt text or --file.", fmt, 1)
            return
    except (OSError, UnicodeError) as exc:
        _error(f"Error reading prompt: {exc}", fmt)
        return

    issues = _analyze_prompt(text)
    fixed_text = _apply_safe_fixes(text) if fix else text
    backup_path = None
    if fix and file_path is not None and not dry_run and fixed_text != text:
        try:
            backup_path = _atomic_fix(file_path, fixed_text)
        except (OSError, UnicodeError) as exc:
            _error(f"Error writing prompt: {exc}", fmt)
    if fmt == "json":
        if fix and file_path is None:
            typer.echo(fixed_report(text, issues, fixed_text, _analyze_prompt(fixed_text)))
        else:
            typer.echo(_issues_to_json(text, issues))
        return

    if file_path is not None:
        console.print(f"[bold]Analyzing file:[/bold] {file or target}\n")
    else:
        console.print("[bold]Analyzing text prompt...[/bold]\n")
    _print_issues_table(issues)
    if not fix:
        return
    if file_path is None:
        console.print("\n[bold]Suggested fix:[/bold]")
        console.print(fixed_text)
    elif fixed_text == text:
        console.print("\n[dim]No safe fixes to apply.[/dim]")
    elif dry_run:
        console.print("\n[bold yellow]Dry run — would apply these fixes:[/bold yellow]")
        import difflib
        for line in difflib.unified_diff(text.splitlines(), fixed_text.splitlines(), lineterm=""):
            console.print(line, markup=False)
    else:
        console.print(f"\n[bold green]Fixed![/bold green] Backup saved to {backup_path}")
