"""Search prompts by content and filename."""

from typing import List, Optional

import typer
from rich.table import Table

from llm_promptkit.helpers import console, get_prompts_dir, is_prompt_file


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

                results.append(
                    {
                        "path": str(rel_path),
                        "title": prompt_file.stem,
                        "score": score,
                        "snippet": snippet,
                    }
                )

    # Sort by score descending
    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:limit]


def search_command(
    query: list[str] = typer.Argument(..., help="Search terms"),
    limit: int = typer.Option(10, "--limit", "-l", help="Max results (default: 10)"),
    category: Optional[str] = typer.Option(None, "--category", "-c", help="Limit to category"),
):
    """Search prompts by content."""
    query_str = " ".join(query)

    if not query_str.strip():
        console.print("[red]Please provide a search query.[/red]")
        raise typer.Exit(code=1)

    results = search_prompts(query_str, limit=limit, category=category)

    if not results:
        console.print(f"[yellow]No prompts found matching '{query_str}'[/yellow]")
        console.print("[dim]Try broader terms or check spelling.[/dim]")
        return

    table = Table(
        title=f"Search Results for '{query_str}'",
        show_header=True,
        header_style="bold magenta",
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
            result["snippet"][:50] + ("..." if len(result["snippet"]) > 50 else ""),
        )

    console.print(table)
    console.print(f"\n[dim]Found {len(results)} results. Use --limit N for more.[/dim]")
    console.print("[dim]View with: promptkit prompts --show <path>[/dim]")
