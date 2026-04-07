"""Tests for the pattern registry module."""

import warnings

import pytest

from llm_promptkit.pattern_registry import (
    PATTERN_ALIASES,
    PatternRegistry,
    get_registry,
)


class TestPatternRegistry:
    """Tests for PatternRegistry class."""

    def test_empty_registry(self):
        registry = PatternRegistry()
        assert registry.keys() == []

    def test_load_from_directory(self, tmp_path):
        # Create a minimal pattern file
        category_dir = tmp_path / "reasoning"
        category_dir.mkdir()
        pattern_file = category_dir / "chain-of-thought.md"
        pattern_file.write_text("# Chain of Thought\n\n## Template\n\nThink step by step.")

        registry = PatternRegistry(patterns_dir=tmp_path)
        assert len(registry.keys()) > 0

    def test_resolve_direct_name(self):
        registry = PatternRegistry()
        registry._patterns = {"chain-of-thought": "Think step by step."}

        result = registry.resolve("chain-of-thought")
        assert result == "chain-of-thought"

    def test_resolve_alias(self):
        registry = PatternRegistry()
        registry._patterns = {"chain-of-thought": "Think step by step."}

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            result = registry.resolve("cot")
            assert result == "chain-of-thought"
            assert len(w) == 1
            assert "deprecated" in str(w[0].message).lower()

    def test_resolve_underscore_alias(self):
        registry = PatternRegistry()
        registry._patterns = {"chain-of-thought": "Think step by step."}

        # Underscore variant normalizes to the canonical name, so no deprecation warning
        result = registry.resolve("chain_of_thought")
        assert result == "chain-of-thought"

    def test_resolve_shorthand_alias_warns(self):
        registry = PatternRegistry()
        registry._patterns = {"json-output": "Return JSON."}

        # "json_enforcer" is a true alias (different canonical name), should warn
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            result = registry.resolve("json_enforcer")
            assert result == "json-output"
            assert len(caught) == 1
            assert "deprecated" in str(caught[0].message).lower()

    def test_resolve_unknown_raises(self):
        registry = PatternRegistry()
        with pytest.raises(ValueError, match="Unknown pattern"):
            registry.resolve("nonexistent-pattern")

    def test_get_returns_content(self):
        registry = PatternRegistry()
        registry._patterns = {"chain-of-thought": "Think step by step."}

        content = registry.get("chain-of-thought")
        assert content == "Think step by step."

    def test_contains_direct(self):
        registry = PatternRegistry()
        registry._patterns = {"chain-of-thought": "Think step by step."}

        assert "chain-of-thought" in registry
        assert "nonexistent" not in registry

    def test_contains_alias(self):
        registry = PatternRegistry()
        registry._patterns = {"chain-of-thought": "Think step by step."}

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            assert "cot" in registry

    def test_getitem(self):
        registry = PatternRegistry()
        registry._patterns = {"chain-of-thought": "Think step by step."}

        assert registry["chain-of-thought"] == "Think step by step."

    def test_keys_returns_canonical_names(self):
        registry = PatternRegistry()
        registry._patterns = {"a": "1", "b": "2", "c": "3"}

        assert sorted(registry.keys()) == ["a", "b", "c"]

    def test_items_returns_all_patterns(self):
        registry = PatternRegistry()
        registry._patterns = {"a": "1", "b": "2"}

        items = dict(registry.items())
        assert items == {"a": "1", "b": "2"}

    def test_case_insensitive_resolve(self):
        registry = PatternRegistry()
        registry._patterns = {"chain-of-thought": "Think step by step."}

        result = registry.resolve("Chain-of-Thought")
        assert result == "chain-of-thought"

    def test_space_normalization(self):
        registry = PatternRegistry()
        registry._patterns = {"chain-of-thought": "Think step by step."}

        result = registry.resolve("chain of thought")
        assert result == "chain-of-thought"


class TestPatternAliases:
    """Tests for alias definitions."""

    def test_aliases_dict_not_empty(self):
        assert len(PATTERN_ALIASES) > 0

    def test_common_aliases_exist(self):
        assert "cot" in PATTERN_ALIASES
        assert "fewshot" in PATTERN_ALIASES
        assert "json_enforcer" in PATTERN_ALIASES

    def test_all_alias_values_are_strings(self):
        for key, value in PATTERN_ALIASES.items():
            assert isinstance(key, str)
            assert isinstance(value, str)


class TestGlobalRegistry:
    """Tests for global registry functions."""

    def test_get_registry_returns_instance(self):
        import llm_promptkit.pattern_registry as mod
        old = mod._registry
        mod._registry = None
        try:
            registry = get_registry()
            assert isinstance(registry, PatternRegistry)
        finally:
            mod._registry = old

    def test_get_registry_caches(self):
        import llm_promptkit.pattern_registry as mod
        old = mod._registry
        mod._registry = None
        try:
            r1 = get_registry()
            r2 = get_registry()
            assert r1 is r2
        finally:
            mod._registry = old
