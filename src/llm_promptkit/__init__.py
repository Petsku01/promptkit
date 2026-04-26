"""llm-promptkit: A toolkit for building effective LLM prompts from patterns.

Usage:
    from llm_promptkit import PromptBuilder

    prompt = (PromptBuilder()
        .persona("Senior Developer")
        .pattern("chain-of-thought")
        .task("Review this code")
        .build())
"""

from importlib.metadata import version as _version

from .builder import PromptBuilder
from .patterns._registry import PatternLoadError, PatternNotFoundError, PromptKitError

__version__ = _version("llm-promptkit")
__all__ = [
    "PromptBuilder",
    "PromptKitError",
    "PatternNotFoundError",
    "PatternLoadError",
]
