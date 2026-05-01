"""llm-promptkit: A toolkit for building effective LLM prompts from patterns."""

from importlib.metadata import version as _version

from .builder import PromptBuilder
from .config import PromptKitConfig, get_config, reload_config
from .patterns._registry import PatternLoadError, PatternNotFoundError, PromptKitError

__version__ = _version("llm-promptkit")
__all__ = [
    "PromptBuilder",
    "PromptKitConfig",
    "PromptKitError",
    "PatternNotFoundError",
    "PatternLoadError",
    "get_config",
    "reload_config",
]
