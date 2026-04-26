"""Tests for the patterns registry."""

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
    def test_list_pattern_names_not_empty(self):
        assert len(list_pattern_names()) > 0

    def test_list_pattern_names_contains_core_patterns(self):
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
        for name in list_pattern_names():
            assert name == name.lower(), f"Not lowercase: {name}"
            assert " " not in name, f"Has spaces: {name}"

    def test_list_pattern_names_returns_tuple(self):
        names = list_pattern_names()
        assert isinstance(names, tuple)
        assert not isinstance(names, list)

    def test_list_patterns_with_categories(self):
        pairs = list_patterns_with_categories()
        assert len(pairs) > 0
        for name, category in pairs:
            assert name
            assert category

    def test_read_pattern_chain_of_thought(self):
        content = read_pattern("chain-of-thought")
        assert "step-by-step" in content.lower() or "step" in content.lower()

    def test_read_pattern_self_consistency(self):
        content = read_pattern("self-consistency")
        assert "three" in content.lower() or "different" in content.lower()

    def test_read_pattern_unknown_raises(self):
        with pytest.raises(PatternNotFoundError, match="Unknown pattern"):
            read_pattern("nonexistent-pattern")

    def test_pattern_not_found_error_hierarchy(self):
        assert issubclass(PatternNotFoundError, PromptKitError)
        assert issubclass(PatternNotFoundError, LookupError)

    def test_get_pattern_description(self):
        desc = get_pattern_description("chain-of-thought")
        assert 0 < len(desc) <= 80

    def test_all_patterns_readable(self):
        for name in list_pattern_names():
            content = read_pattern(name)
            assert len(content) > 0, f"Pattern {name} has empty content"

    def test_available_patterns_returns_tuple(self):
        from llm_promptkit.builder import PromptBuilder

        patterns = PromptBuilder.get_available_patterns()
        assert isinstance(patterns, tuple)
        assert len(patterns) >= 13

    def test_invalidate_cache(self):
        names1 = list_pattern_names()
        invalidate_pattern_cache()
        names2 = list_pattern_names()
        assert names1 == names2
