from pathlib import Path

cli_path = Path("/home/ette/.openclaw/workspace/promptkit/src/llm_promptkit/cli.py")
content = cli_path.read_text()

new_doctor_func = """def doctor_command(args):
    \"\"\"Analyze a prompt for common issues.\"\"\"
    if getattr(args, 'file', None):
        path = Path(args.file)
        if not path.exists():
            console.print(f"[red]Error: File not found: {args.file}[/red]")
            return
        text = path.read_text().lower()
        console.print(f"[bold]Analyzing file:[/bold] {args.file}\\n")
    else:
        text = args.target.lower() if args.target else ""
        console.print("[bold]Analyzing text prompt...[/bold]\\n")

    issues = []

    clean_text = text.strip()

    if not clean_text:
        issues.append(("Error", "Prompt is empty.", "Please provide text to analyze."))
        _print_issues(issues)
        return

    # Strip code blocks for NLP checks
    text_no_code = re.sub(r'```.*?```', '', text, flags=re.DOTALL).strip()

    if len(clean_text) < 20:
        issues.append(("Warning", "Prompt is very short.", "Prompts under 20 characters often lack sufficient detail."))

    # Only run NLP checks if there's non-code text
    if text_no_code:
        # Vague phrases
        for phrase in VAGUE_PHRASES:
            if _match_phrase(text_no_code, phrase):
                issues.append(("Warning", "Vague or ambiguous instructions.", f"Found '{phrase}'. Be more specific."))

        # Missing role
        if not _has_any_phrase(text_no_code, ROLE_PHRASES):
            issues.append(("Suggestion", "Missing context or role definition.", "Add a persona (e.g., 'You are an expert...')."))

        # Verbose phrasing
        for phrase in VERBOSE_PHRASES:
            if _match_phrase(text_no_code, phrase):
                issues.append(("Info", "Token inefficiency.", f"Found '{phrase}'. Use direct commands."))

        # Missing format
        if not _has_any_phrase(text_no_code, FORMAT_PHRASES):
            issues.append(("Warning", "Missing output format.", "Specify format (e.g., 'Output as JSON')."))

        # Missing examples
        if not _has_any_phrase(text_no_code, EXAMPLE_PHRASES):
            issues.append(("Info", "No examples provided.", "Few-shot examples improve output quality."))

        # Negative phrasing
        for phrase in NEGATIVE_PHRASES:
            if _match_phrase(text_no_code, phrase):
                issues.append(("Warning", "Negative constraints.", f"Found '{phrase}'. LLMs follow positive instructions better (e.g., 'Do X' instead of 'Don\\'t do Y')."))
    else:
        issues.append(("Info", "Prompt contains only code.", "No natural language instructions found. Consider adding context or formatting instructions."))

    # Structural formatting check for longer prompts
    if len(clean_text) > 200:
        has_structure = any(marker in text for marker in ["#", "```", "- ", "* ", "1. "])
        if not has_structure:
            issues.append(("Suggestion", "Lacks structural formatting.", "Long prompt detected without markdown structure. Use headers, bullet points, or code blocks."))

    _print_issues(issues)

def _print_issues(issues):
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
"""

# Replace doctor_command to end of file, then append new
old_parts = content.split("def doctor_command(args):")
if len(old_parts) > 1:
    content = old_parts[0] + new_doctor_func + "\n" + "\n".join(old_parts[1].split("def main():")[1:])
    content = content.replace("def main():", "def main():") # add it back
    content = old_parts[0] + new_doctor_func + "\ndef main():\n" + old_parts[1].split("def main():")[1]
    cli_path.write_text(content)
    print("Patched successfully.")
else:
    print("Could not find doctor_command.")
