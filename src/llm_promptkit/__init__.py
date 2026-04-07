"""
promptkit: A toolkit for building effective LLM prompts.

Usage:
    from llm_promptkit import PromptBuilder, analyze_prompt

    prompt = (PromptBuilder()
        .persona("Senior Developer")
        .pattern("chain-of-thought")
        .task("Review this code")
        .build())
"""

from .builder import PromptBuilder
from .doctor import analyze_prompt

__version__ = "0.1.0"
__all__ = ["PromptBuilder", "analyze_prompt"]
