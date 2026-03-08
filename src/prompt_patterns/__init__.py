"""
prompt-patterns: A toolkit for building effective LLM prompts.

Usage:
    from prompt_patterns import PromptBuilder
    
    prompt = (PromptBuilder()
        .persona("Senior Developer")
        .pattern("chain-of-thought")
        .task("Review this code")
        .build())
"""

from .builder import PromptBuilder

__version__ = "0.1.0"
__all__ = ["PromptBuilder"]
