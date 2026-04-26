"""Tests for the patterns registry — single source of truth."""

import pytest

from llm_promptkit.patterns._registry import (
    PatternNotFoundError,
    PromptKitError,
    get_pattern_description,
    invalidate_pattern_cache,
    list_pattern_names,
    list_patterns_with_categories,
    read_pattern,
)


class TestPatternRegistry:
    """Tests for pattern registry loading from .md files."""

    def test_list_pattern_names_not_empty(self):
        """Pattern names should be loaded from .md files."""
        names = list_pattern_names()
        assert len(names) > 0

    def test_list_pattern_names_contains_core_patterns(self):
        """Core patterns from the original dict should be present."""
        names = list_pattern_names()
        core = [
            "chain-of-thought",
            "self-consistency",
            "tree-of-thought",
            "step-back",
            "decomposition",
            "reflection",
            "react",
            "prompt-chaining",
            "meta-prompting",
            "few-shot",
            "role-play",
            "json-output",
            "senior-reviewer",
        ]
        for name in core:
            assert name in names, f"Missing core pattern: {name}"

    def test_list_pattern_names_are_slugs(self):
        """Pattern names should be slug format (lowercase, hyphens)."""
        for name in list_pattern_names():
            assert name == name.lower(), f"Pattern name not lowercase: {name}"
            assert " " not in name, f"Pattern name has spaces: {name}"

    def test_list_pattern_names_returns_tuple(self):
        """list_pattern_names should return a tuple (immutable cache-safe)."""
        names = list_pattern_names()
        assert isinstance(names, tuple)
        assert not isinstance(names, list)

    def test_list_patterns_with_categories(self):
        """Each pattern should have a category."""
        pairs = list_patterns_with_categories()
        assert len(pairs) > 0
        for name, category in pairs:
            assert name, "Pattern name should not be empty"
            assert category, "Category should not be empty"

    def test_read_pattern_chain_of_thought(self):
        """Chain-of-thought pattern should load from .md file."""
        content = read_pattern("chain-of-thought")
        assert "step-by-step" in content.lower() or "step" in content.lower()

    def test_read_pattern_self_consistency(self):
        """Self-consistency pattern should load from .md file."""
        content = read_pattern("self-consistency")
        assert "three" in content.lower() or "different" in content.lower()

    def test_read_pattern_unknown_raises(self):
        """Reading an unknown pattern should raise PatternNotFoundError."""
        with pytest.raises(PatternNotFoundError, match="Unknown pattern"):
            read_pattern("nonexistent-pattern")

    def test_pattern_not_found_error_hierarchy(self):
        """PatternNotFoundError should be a PromptKitError and LookupError subclass."""
        assert issubclass(PatternNotFoundError, PromptKitError)
        assert issubclass(PatternNotFoundError, LookupError)

    def test_get_pattern_description(self):
        """Pattern description should be first line of content."""
        desc = get_pattern_description("chain-of-thought")
        assert len(desc) > 0
        assert len(desc) <= 80

    def test_all_patterns_readable(self):
        """Every listed pattern name should be readable."""
        for name in list_pattern_names():
            content = read_pattern(name)
            assert len(content) > 0, f"Pattern {name} has empty content"

    def test_available_patterns_returns_list(self):
        """PromptBuilder.get_available_patterns() should return a list."""
        from llm_promptkit.builder import PromptBuilder

        patterns = PromptBuilder.get_available_patterns()
        assert isinstance(patterns, list)
        assert len(patterns) >= 13

    def test_invalidate_cache(self):
        """Cache invalidation should allow re-fetching pattern names."""
        names1 = list_pattern_names()
        invalidate_pattern_cache()
        names2 = list_pattern_names()
        assert names1 == names2
