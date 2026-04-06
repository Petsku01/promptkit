"""CLI for promptkit.

Thin adapter layer - delegates to command modules.
"""

import argparse

from .commands import (
    build_prompt,
    doctor_command,
    interactive_build,
    interactive_prompts,
    list_patterns,
    prompts_command,
    search_command,
)
from .commands.prompts import list_model_prompts, list_providers, show_prompt
from .commands.search import search_prompts
from .console import console



def main():
    """Main entry point for CLI."""
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
    doctor_parser.add_argument("--ml", action="store_true", help="Use ML-based analysis (requires Ollama)")
    doctor_parser.add_argument("--model", "-m", default="qwen2.5:3b", help="Ollama model for ML analysis (default: qwen2.5:3b)")

    args = parser.parse_args()

    # Dispatch to command handlers
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
