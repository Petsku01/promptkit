"""Search prompts by content and filename."""

from typing import List, Optional

import typer
from rich.table import Table

from llm_promptkit.helpers import console, get_all_prompt_dirs, is_prompt_file


def search_prompts(query: str, limit: int = 10, category: Optional[str] = None) -> List[dict]:
    """Search prompts by content and filename.

    Returns list of dicts with: path, title, score, snippet, source
    """
    results = []

    # Normalize query terms
    query_lower = query.lower()
    query_terms = query_lower.split()

    # Search all prompt directories (user first, then built-in)
    all_dirs = get_all_prompt_dirs()

    for prompt_dir in all_dirs:
        source = "custom" if prompt_dir != all_dirs[-1] else "built-in"
        search_dirs = [prompt_dir]
        if category:
            category_path = prompt_dir / category
            if category_path.exists():
                search_dirs = [category_path]
            else:
                continue

        for search_dir in search_dirs:
            if not search_dir.exists():
                continue

            for prompt_file in search_dir.rglob("*.md"):
                if not is_prompt_file(prompt_file):
                    continue

                try:
                    content = prompt_file.read_text()
                except (OSError, UnicodeDecodeError):
                    continue

                content_lower = content.lower()
                filename_lower = prompt_file.stem.lower()

                # Calculate score based on term matches
                score = 0

                # Exact phrase match (highest value)
                if query_lower in content_lower:
                    score += 10
                if query_lower in filename_lower:
                    score += 15

                # Individual term matches
                for term in query_terms:
                    if term in filename_lower:
                        score += 5
                    term_count = content_lower.count(term)
                    if term_count > 0:
                        score += min(term_count, 5)

                # Path/category bonus
                rel_path = prompt_file.relative_to(prompt_dir)
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
                        first_line = content.split("\n")[0][:80]
                        snippet = first_line

                    results.append(
                        {
                            "path": str(rel_path),
                            "title": prompt_file.stem,
                            "score": score,
                            "snippet": snippet,
                            "source": source,
                        }
                    )

    # Sort by score descending
    results.sort(
        key=lambda x: x["score"] if isinstance(x["score"], (int, float)) else 0, reverse=True
    )
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
    table.add_column("Source", style="yellow")
    table.add_column("Snippet", style="green", max_width=40)

    for i, result in enumerate(results, 1):
        table.add_row(
            str(i),
            result["title"],
            result["path"],
            f"\\[{result['source']}]",
            result["snippet"][:40] + ("..." if len(result["snippet"]) > 40 else ""),
        )

    console.print(table)
    console.print(f"\n[dim]Found {len(results)} results. Use --limit N for more.[/dim]")
    console.print("[dim]View with: promptkit prompts --show <path>[/dim]")
