"""
CLI for promptkit.

Usage:
    promptkit list
    promptkit build --pattern chain-of-thought --task "Review this code"
    promptkit build --interactive
    promptkit prompts
    promptkit prompts --model openai/gpt-4o
    promptkit prompts --show openai/gpt-4o/coding
    promptkit search "security code review"
"""

import argparse
from importlib import resources
import subprocess
from pathlib import Path
from typing import List, Optional, Tuple

import re

# Doctor Command Constants
VAGUE_PHRASES = ["make it good", "do it well", "as best as you can", "stuff", "things", "as soon as possible", "asap", "etc", "and so on", "whatever you think"]
ROLE_PHRASES = ["you are a", "you are an", "role:", "persona:", "act as", "system:", "<role>", "<system_prompt>", "<persona>"]
VERBOSE_PHRASES = ["please could you", "i would like you to", "if you don't mind", "can you please", "please", "thank you", "thanks", "kindly"]
FORMAT_PHRASES = ["format", "json", "markdown", "output:", "structure", "return as"]
EXAMPLE_PHRASES = ["example:", "example", "e.g.", "for instance", "few-shot", "here is an example"]
NEGATIVE_PHRASES = ["don't", "do not", "never", "avoid", "must not", "stop"]


from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax
from rich.table import Table

from .builder import PromptBuilder

console = Console()

# Constants
CHARS_PER_TOKEN = 4  # Rough estimate for token counting


def get_prompts_dir() -> Path:
    """Get the prompts directory path."""
    package_prompts = Path(str(resources.files("llm_promptkit").joinpath("prompts")))
    if package_prompts.exists():
        return package_prompts

    # Local repo fallback
    cwd_prompts = Path.cwd() / "prompts"
    if cwd_prompts.exists():
        return cwd_prompts
    return package_prompts


def is_prompt_file(path: Path) -> bool:
    """Check if a file is a prompt (not README)."""
    return path.suffix == ".md" and path.stem.lower() != "readme"


def get_prompt_files(directory: Path) -> List[Path]:
    """Get all prompt files in a directory."""
    return sorted([p for p in directory.glob("*.md") if is_prompt_file(p)])


def count_prompts(directory: Path) -> int:
    """Count prompt files in a directory."""
    return len(get_prompt_files(directory))


def get_models_with_prompts(provider_path: Path) -> List[Tuple[str, int]]:
    """Get models that have actual prompts."""
    models = []
    for m in sorted(provider_path.iterdir()):
        if m.is_dir():
            prompt_count = count_prompts(m)
            if prompt_count > 0:
                models.append((m.name, prompt_count))
    return models


def copy_to_clipboard(text: str) -> bool:
    """Copy text to clipboard. Returns True on success."""
    commands = [
        ["xclip", "-selection", "clipboard"],
        ["xsel", "--clipboard", "--input"],
        ["pbcopy"],
    ]
    for cmd in commands:
        try:
            process = subprocess.Popen(cmd, stdin=subprocess.PIPE)
            process.communicate(text.encode())
            if process.returncode == 0:
                return True
        except FileNotFoundError:
            continue
    return False

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

    prompt = builder.build()

    console.print("\n")
    console.print(Panel(prompt, title="Generated Prompt", border_style="blue"))
    console.print(f"[dim]Estimated tokens: {builder.estimate_tokens()}[/dim]")


def interactive_prompts():
    """Interactive prompt selector with back navigation."""
    prompts_dir = get_prompts_dir()
    model_dir = prompts_dir / "model-optimized"

    if not model_dir.exists():
        console.print("[red]Model-optimized prompts directory not found.[/red]")
        return

    console.print(Panel.fit("Prompt Selector", style="bold magenta"))
    console.print("[dim]Enter number to select, 'b' to go back, 'q' to quit[/dim]")

    while True:
        # Step 1: Select provider (only those with models that have prompts)
        providers = []
        for p in sorted(model_dir.iterdir()):
            if p.is_dir():
                models_with_prompts = len(get_models_with_prompts(p))
                if models_with_prompts > 0:
                    providers.append((p.name, models_with_prompts))

        console.print("\n[bold cyan]Select a provider:[/bold cyan]")
        for i, (provider, model_count) in enumerate(providers, 1):
            console.print(f"  [dim]{i}.[/dim] [cyan]{provider}[/cyan] [dim]({model_count} models)[/dim]")

        provider_choice = Prompt.ask("\nProvider").strip().lower()
        if provider_choice == "q":
            return
        if provider_choice == "b":
            console.print("[dim]Already at top level.[/dim]")
            continue
        try:
            provider_idx = int(provider_choice) - 1
            if provider_idx < 0 or provider_idx >= len(providers):
                console.print("[red]Invalid selection.[/red]")
                continue
            selected_provider = providers[provider_idx][0]
        except ValueError:
            console.print("[red]Enter a number, 'b' for back, or 'q' to quit.[/red]")
            continue

        # Step 2: Select model (only those with prompts)
        while True:
            provider_path = model_dir / selected_provider
            models = get_models_with_prompts(provider_path)

            if not models:
                console.print(f"[red]No models with prompts found for {selected_provider}.[/red]")
                break

            console.print(f"\n[bold cyan]Select a model for {selected_provider}:[/bold cyan]")
            for i, (model, prompt_count) in enumerate(models, 1):
                console.print(f"  [dim]{i}.[/dim] [cyan]{model}[/cyan] [dim]({prompt_count} prompts)[/dim]")

            model_choice = Prompt.ask("\nModel").strip().lower()
            if model_choice == "q":
                return
            if model_choice == "b":
                break  # Back to provider selection
            try:
                model_idx = int(model_choice) - 1
                if model_idx < 0 or model_idx >= len(models):
                    console.print("[red]Invalid selection.[/red]")
                    continue
                selected_model = models[model_idx][0]
            except ValueError:
                console.print("[red]Enter a number, 'b' for back, or 'q' to quit.[/red]")
                continue

            # Step 3: Select prompt
            while True:
                model_path = provider_path / selected_model
                prompt_files = get_prompt_files(model_path)

                if not prompt_files:
                    console.print(f"[red]No prompts found for {selected_provider}/{selected_model}.[/red]")
                    break

                console.print(f"\n[bold cyan]Select a prompt for {selected_provider}/{selected_model}:[/bold cyan]")
                for i, pf in enumerate(prompt_files, 1):
                    console.print(f"  [dim]{i}.[/dim] [cyan]{pf.stem}[/cyan]")

                prompt_choice = Prompt.ask("\nPrompt").strip().lower()
                if prompt_choice == "q":
                    return
                if prompt_choice == "b":
                    break  # Back to model selection
                try:
                    prompt_idx = int(prompt_choice) - 1
                    if prompt_idx < 0 or prompt_idx >= len(prompt_files):
                        console.print("[red]Invalid selection.[/red]")
                        continue
                    selected_prompt = prompt_files[prompt_idx]
                except ValueError:
                    console.print("[red]Enter a number, 'b' for back, or 'q' to quit.[/red]")
                    continue

                # Show the selected prompt
                content = selected_prompt.read_text()
                console.print("\n")
                console.print(Panel(
                    Syntax(content, "markdown", theme="monokai", word_wrap=True),
                    title=f"{selected_provider}/{selected_model}/{selected_prompt.stem}",
                    border_style="blue"
                ))
                console.print(f"\n[dim]Estimated tokens: ~{len(content) // CHARS_PER_TOKEN}[/dim]")

                # Copy option
                copy_choice = Prompt.ask("\nCopy to clipboard? [y/n/q]", default="n").strip().lower()
                if copy_choice == "q":
                    return
                if copy_choice == "y":
                    if copy_to_clipboard(content):
                        console.print("[green]Copied to clipboard![/green]")
                    else:
                        console.print("[yellow]No clipboard tool found (install xclip or xsel).[/yellow]")

                # After showing prompt, ask what to do next
                next_action = Prompt.ask("\n[dim]Press Enter to select another prompt, 'b' for back, 'q' to quit[/dim]", default="").strip().lower()
                if next_action == "q":
                    return
                if next_action == "b":
                    break


def list_providers():
    """List available model providers (only those with prompts)."""
    prompts_dir = get_prompts_dir()
    model_dir = prompts_dir / "model-optimized"

    if not model_dir.exists():
        console.print("[red]Model-optimized prompts directory not found.[/red]")
        console.print(f"[dim]Looking in: {model_dir}[/dim]")
        return

    table = Table(title="Available Providers", show_header=True, header_style="bold magenta")
    table.add_column("Provider", style="cyan")
    table.add_column("Models", style="green")

    for provider_path in sorted(model_dir.iterdir()):
        if provider_path.is_dir():
            models = get_models_with_prompts(provider_path)
            if models:
                model_names = [m[0] for m in models]
                table.add_row(
                    provider_path.name,
                    ", ".join(model_names[:4]) + ("..." if len(models) > 4 else "")
                )

    console.print(table)
    console.print("\n[dim]Use: promptkit prompts --model <provider> to list models[/dim]")
    console.print("[dim]Use: promptkit prompts --model <provider>/<model> to list prompts[/dim]")


def list_model_prompts(model_path: str):
    """List available prompts for a specific model."""
    prompts_dir = get_prompts_dir()

    parts = model_path.split("/")
    if len(parts) == 1:
        # Just provider - list models
        provider_dir = prompts_dir / "model-optimized" / parts[0]
        if not provider_dir.exists():
            console.print(f"[red]Provider '{parts[0]}' not found.[/red]")
            return

        table = Table(title=f"Models for {parts[0]}", show_header=True, header_style="bold magenta")
        table.add_column("Model", style="cyan")
        table.add_column("Prompts", style="green")

        for model_name, prompt_count in get_models_with_prompts(provider_dir):
            prompts = get_prompt_files(provider_dir / model_name)
            table.add_row(model_name, ", ".join(p.stem for p in prompts))

        console.print(table)
        console.print(f"\n[dim]Use: promptkit prompts --model {parts[0]}/<model> to list prompts[/dim]")

    elif len(parts) == 2:
        # Provider/model - list prompts
        full_model_dir = prompts_dir / "model-optimized" / parts[0] / parts[1]
        if not full_model_dir.exists():
            console.print(f"[red]Model '{model_path}' not found.[/red]")
            return

        table = Table(title=f"Prompts for {model_path}", show_header=True, header_style="bold magenta")
        table.add_column("Prompt", style="cyan")
        table.add_column("File", style="dim")

        for prompt_file in get_prompt_files(full_model_dir):
            table.add_row(prompt_file.stem, prompt_file.name)

        console.print(table)
        console.print(f"\n[dim]Use: promptkit prompts --show {model_path}/<prompt> to view[/dim]")
    else:
        console.print("[red]Invalid format. Use: provider or provider/model[/red]")


def show_prompt(prompt_path: str):
    """Show a specific prompt."""
    prompts_dir = get_prompts_dir()

    parts = prompt_path.split("/")
    if len(parts) != 3:
        console.print("[red]Invalid format. Use: provider/model/prompt[/red]")
        console.print("[dim]Example: openai/gpt-4o/coding[/dim]")
        return

    provider, model, prompt_name = parts
    prompt_file = prompts_dir / "model-optimized" / provider / model / f"{prompt_name}.md"

    if not prompt_file.exists():
        console.print(f"[red]Prompt '{prompt_path}' not found.[/red]")
        console.print(f"[dim]Looking for: {prompt_file}[/dim]")
        return

    content = prompt_file.read_text()

    # Display with syntax highlighting
    console.print(Panel(
        Syntax(content, "markdown", theme="monokai", word_wrap=True),
        title=f"{provider}/{model}/{prompt_name}",
        border_style="blue"
    ))

    # Show token estimate
    console.print(f"\n[dim]Estimated tokens: ~{len(content) // CHARS_PER_TOKEN}[/dim]")


def prompts_command(args):
    """Handle prompts subcommand."""
    if args.interactive:
        interactive_prompts()
    elif args.show:
        show_prompt(args.show)
    elif args.model:
        list_model_prompts(args.model)
    else:
        list_providers()


def search_prompts(query: str, limit: int = 10, category: Optional[str] = None) -> List[dict]:
    """Search prompts by content and filename.

    Returns list of dicts with: path, title, score, snippet
    """
    prompts_dir = get_prompts_dir()
    results = []

    # Normalize query terms
    query_lower = query.lower()
    query_terms = query_lower.split()

    # Search all prompt directories
    search_dirs = [prompts_dir]
    if category:
        search_dirs = [prompts_dir / category]

    for search_dir in search_dirs:
        if not search_dir.exists():
            continue

        for prompt_file in search_dir.rglob("*.md"):
            if not is_prompt_file(prompt_file):
                continue

            try:
                content = prompt_file.read_text()
            except Exception:
                continue

            content_lower = content.lower()
            filename_lower = prompt_file.stem.lower()
            rel_path = prompt_file.relative_to(prompts_dir)

            # Calculate score based on term matches
            score = 0

            # Exact phrase match (highest value)
            if query_lower in content_lower:
                score += 10
            if query_lower in filename_lower:
                score += 15

            # Individual term matches
            for term in query_terms:
                # Filename matches are weighted higher
                if term in filename_lower:
                    score += 5
                # Content matches
                term_count = content_lower.count(term)
                if term_count > 0:
                    score += min(term_count, 5)  # Cap at 5 per term

            # Path/category bonus
            path_str = str(rel_path).lower()
            for term in query_terms:
                if term in path_str:
                    score += 2

            if score > 0:
                # Extract snippet around first match
                snippet = ""
                for term in query_terms:
                    idx = content_lower.find(term)
                    if idx != -1:
                        start = max(0, idx - 40)
                        end = min(len(content), idx + len(term) + 60)
                        snippet = content[start:end].replace("\n", " ").strip()
                        if start > 0:
                            snippet = "..." + snippet
                        if end < len(content):
                            snippet = snippet + "..."
                        break

                if not snippet:
                    # Use first line as fallback
                    first_line = content.split("\n")[0][:80]
                    snippet = first_line

                results.append({
                    "path": str(rel_path),
                    "title": prompt_file.stem,
                    "score": score,
                    "snippet": snippet,
                })

    # Sort by score descending
    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:limit]


def search_command(args):
    """Handle search subcommand."""
    query = " ".join(args.query)

    if not query.strip():
        console.print("[red]Please provide a search query.[/red]")
        return

    results = search_prompts(query, limit=args.limit, category=args.category)

    if not results:
        console.print(f"[yellow]No prompts found matching '{query}'[/yellow]")
        console.print("[dim]Try broader terms or check spelling.[/dim]")
        return

    table = Table(
        title=f"Search Results for '{query}'",
        show_header=True,
        header_style="bold magenta"
    )
    table.add_column("#", style="dim", width=3)
    table.add_column("Prompt", style="cyan")
    table.add_column("Path", style="dim")
    table.add_column("Snippet", style="green", max_width=50)

    for i, result in enumerate(results, 1):
        table.add_row(
            str(i),
            result["title"],
            result["path"],
            result["snippet"][:50] + ("..." if len(result["snippet"]) > 50 else "")
        )

    console.print(table)
    console.print(f"\n[dim]Found {len(results)} results. Use --limit N for more.[/dim]")
    console.print("[dim]View with: promptkit prompts --show <path>[/dim]")



def _match_phrase(text: str, phrase: str) -> bool:
    """Check if phrase exists as whole word in text."""
    return bool(re.search(rf"(?<!\w){re.escape(phrase)}(?!\w)", text, re.IGNORECASE))


def _has_any_phrase(text: str, phrases: list) -> bool:
    """Check if any phrase exists in text."""
    return any(_match_phrase(text, p) for p in phrases)


def doctor_command(args):
    """Analyze a prompt for common issues."""
    if getattr(args, 'file', None):
        path = Path(args.file)
        if not path.exists():
            console.print(f"[red]Error: File not found: {args.file}[/red]")
            return
        text = path.read_text().lower()
        console.print(f"[bold]Analyzing file:[/bold] {args.file}\n")
    else:
        text = args.target.lower() if args.target else ""
        console.print("[bold]Analyzing text prompt...[/bold]\n")

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
                issues.append(("Warning", "Negative constraints.", f"Found '{phrase}'. LLMs follow positive instructions better (e.g., 'Do X' instead of 'Don\'t do Y')."))
    else:
        issues.append(("Info", "Prompt contains only code.", "No natural language instructions found. Consider adding context or formatting instructions."))

    # Structural formatting check for longer prompts
    if len(clean_text) > 200:
        # Check for markdown OR XML structure
        has_markdown = any(marker in text for marker in ["#", "```", "- ", "* ", "1. "])
        has_xml = bool(re.search(r'<[a-z_]+>', text, re.IGNORECASE))
        has_structure = has_markdown or has_xml
        if not has_structure:
            issues.append(("Suggestion", "Lacks structural formatting.", "Long prompt detected without markdown or XML structure. Use headers, bullet points, code blocks, or XML tags."))

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

def main():

    parser = argparse.ArgumentParser(
        prog="promptkit",
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

    # Prompts command
    prompts_parser = subparsers.add_parser("prompts", help="Browse model-optimized prompts")
    prompts_parser.add_argument("--model", "-m", help="Provider or provider/model (e.g., openai or openai/gpt-4o)")
    prompts_parser.add_argument("--show", "-s", help="Show prompt content (e.g., openai/gpt-4o/coding)")
    prompts_parser.add_argument("--interactive", "-i", action="store_true", help="Interactive selection mode")

    # Search command
    search_parser = subparsers.add_parser("search", help="Search prompts by content")
    search_parser.add_argument("query", nargs="+", help="Search terms")
    search_parser.add_argument("--limit", "-l", type=int, default=10, help="Max results (default: 10)")
    search_parser.add_argument("--category", "-c", help="Limit to category (e.g., model-optimized, reasoning)")


    # Doctor command
    doctor_parser = subparsers.add_parser("doctor", help="Analyze prompts for common issues")
    doctor_parser.add_argument("target", nargs="?", default="", help="Prompt text string")
    doctor_parser.add_argument("--file", "-f", help="Read prompt from file")

    args = parser.parse_args()


    if args.command == "list":
        list_patterns()
    elif args.command == "doctor":
        doctor_command(args)
    elif args.command == "build":
        if args.interactive:
            interactive_build()
        else:
            build_prompt(args)
    elif args.command == "prompts":
        prompts_command(args)
    elif args.command == "search":
        search_command(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
