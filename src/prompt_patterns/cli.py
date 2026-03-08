"""
CLI for prompt-patterns.

Usage:
    prompt-patterns list
    prompt-patterns build --pattern chain-of-thought --task "Review this code"
    prompt-patterns build --interactive
"""

import argparse
import sys
from .builder import PromptBuilder


def list_patterns():
    """List available patterns."""
    print("Available patterns:")
    print("-" * 40)
    for name, description in PromptBuilder.PATTERNS.items():
        # Show first line of description
        first_line = description.split("\n")[0][:60]
        print(f"  {name:20} {first_line}...")
    print()


def build_prompt(args):
    """Build a prompt from arguments."""
    builder = PromptBuilder()
    
    if args.persona:
        builder.persona(args.persona)
    
    if args.pattern:
        for pattern in args.pattern:
            builder.pattern(pattern)
    
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
        print(f"# Estimated tokens: {token_count}", file=sys.stderr)
    
    if args.output:
        with open(args.output, "w") as f:
            f.write(prompt)
        print(f"Prompt written to {args.output}", file=sys.stderr)
    else:
        print(prompt)


def interactive_build():
    """Interactive prompt builder."""
    print("Prompt Builder - Interactive Mode")
    print("=" * 40)
    
    builder = PromptBuilder()
    
    # Persona
    persona = input("Persona (e.g., 'Senior Developer') [skip]: ").strip()
    if persona:
        builder.persona(persona)
    
    # Patterns
    print("\nAvailable patterns:", ", ".join(PromptBuilder.PATTERNS.keys()))
    patterns_input = input("Patterns (comma-separated) [skip]: ").strip()
    if patterns_input:
        for p in patterns_input.split(","):
            p = p.strip()
            if p:
                try:
                    builder.pattern(p)
                except ValueError as e:
                    print(f"Warning: {e}")
    
    # Task
    task = input("\nTask description: ").strip()
    if task:
        builder.task(task)
    
    # Context
    context = input("Context (paste code/text, empty to skip): ").strip()
    if context:
        builder.context(context)
    
    print("\n" + "=" * 40)
    print("Generated Prompt:")
    print("=" * 40)
    print(builder.build())
    print("=" * 40)
    print(f"Estimated tokens: {builder.estimate_tokens()}")


def main():
    parser = argparse.ArgumentParser(
        prog="prompt-patterns",
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
    
    args = parser.parse_args()
    
    if args.command == "list":
        list_patterns()
    elif args.command == "build":
        if args.interactive:
            interactive_build()
        else:
            build_prompt(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
