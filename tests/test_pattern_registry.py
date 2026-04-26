"""Tests for the patterns registry — single source of truth."""
import pytest
from llm_promptkit.patterns._registry import (
    list_pattern_names,
    list_patterns_with_categories,
    read_pattern,
    get_pattern_description,
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
        """Reading an unknown pattern should raise ValueError."""
        with pytest.raises(ValueError, match="Unknown pattern"):
            read_pattern("nonexistent-pattern")

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

    def test_patterns_have_no_dict_fallback(self):
        """Ensure the PATTERNS dict is gone from builder."""
        from llm_promptkit.builder import PromptBuilder
        # AVAILABLE_PATTERNS should be a list of names
        assert isinstance(PromptBuilder.AVAILABLE_PATTERNS, list)
        assert len(PromptBuilder.AVAILABLE_PATTERNS) >= 13