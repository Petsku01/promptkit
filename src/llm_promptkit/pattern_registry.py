"""Pattern registry with alias support."""

from pathlib import Path
from typing import Dict, List, Optional

from ..pattern_loader import PatternLoader


# Pattern name aliases for backward compatibility
PATTERN_ALIASES = {
    # Legacy names -> canonical names
    "json-enforcer": "json-output",
    "json_enforcer": "json-output",
    "jsonoutput": "json-output",
    "few-shot": "few-shot-negatives",
    "few_shot": "few-shot-negatives",
    "fewshot": "few-shot-negatives",
    "chain-of-thought": "chain-of-thought",
    "chain_of_thought": "chain-of-thought",
    "chainofthought": "chain-of-thought",
    "cot": "chain-of-thought",
    "self-consistency": "self-consistency",
    "self_consistency": "self-consistency",
    "selfconsistency": "self-consistency",
    "senior-reviewer": "senior-reviewer",
    "senior_reviewer": "senior-reviewer",
    "seniorreviewer": "senior-reviewer",
    "stack-trace-decoder": "stack-trace-decoder",
    "stack_trace_decoder": "stack-trace-decoder",
    "stacktracedecoder": "stack-trace-decoder",
    "tdd-prompting": "tdd-prompting",
    "tdd_prompting": "tdd-prompting",
    "tddprompting": "tdd-prompting",
    "hallucination-reducer": "hallucination-reducer",
    "hallucination_reducer": "hallucination-reducer",
    "hallucinationreducer": "hallucination-reducer",
}


class PatternRegistry:
    """Registry for prompt patterns with alias support."""
    
    def __init__(self, patterns_dir: Optional[Path] = None):
        self._patterns: Dict[str, str] = {}
        self._aliases: Dict[str, str] = PATTERN_ALIASES.copy()
        
        if patterns_dir:
            self.load_from_directory(patterns_dir)
    
    def load_from_directory(self, patterns_dir: Path) -> None:
        """Load patterns from directory."""
        loader = PatternLoader()
        self._patterns = loader.load_from_directory(patterns_dir)
    
    def resolve(self, name: str) -> str:
        """Resolve pattern name (handle aliases).
        
        Returns canonical name or raises ValueError if not found.
        """
        normalized = name.lower().replace("_", "-").replace(" ", "-")
        
        # Check if it's an alias
        if normalized in self._aliases:
            canonical = self._aliases[normalized]
            # TODO: Add deprecation warning here
            return canonical
        
        # Check if it's a direct pattern name
        if normalized in self._patterns:
            return normalized
        
        raise ValueError(f"Unknown pattern: {name}")
    
    def get(self, name: str) -> str:
        """Get pattern content by name (with alias resolution)."""
        canonical = self.resolve(name)
        return self._patterns[canonical]
    
    def __contains__(self, name: str) -> bool:
        """Check if pattern exists (including aliases)."""
        try:
            self.resolve(name)
            return True
        except ValueError:
            return False
    
    def __getitem__(self, name: str) -> str:
        """Get pattern content by name."""
        return self.get(name)
    
    def keys(self) -> List[str]:
        """Return all canonical pattern names."""
        return list(self._patterns.keys())
    
    def items(self):
        """Return all pattern items."""
        return self._patterns.items()


# Global registry instance
_registry: Optional[PatternRegistry] = None


def get_registry(patterns_dir: Optional[Path] = None) -> PatternRegistry:
    """Get or create global pattern registry."""
    global _registry
    if _registry is None:
        _registry = PatternRegistry(patterns_dir)
    return _registry


def resolve_pattern(name: str) -> str:
    """Resolve pattern name using global registry."""
    return get_registry().resolve(name)
