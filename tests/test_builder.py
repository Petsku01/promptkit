"""Tests for PromptBuilder."""

import pytest

from llm_promptkit.builder import PromptBuilder


class TestBasicBuild:
    """Test basic prompt building functionality."""

    def test_empty_build(self):
        """Empty builder produces empty string."""
        builder = PromptBuilder()
        assert builder.build() == ""

    def test_persona_only(self):
        """Persona sets role correctly."""
        builder = PromptBuilder().persona("Senior Developer")
        prompt = builder.build()
        assert "You are a Senior Developer" in prompt

    def test_task_only(self):
        """Task is included in output."""
        builder = PromptBuilder().task("Review code")
        prompt = builder.build()
        assert "Task: Review code" in prompt

    def test_persona_and_task(self):
        """Persona and task combine correctly."""
        builder = PromptBuilder()
        builder.persona("Senior Developer").task("Review code")
        prompt = builder.build()
        assert "You are a Senior Developer" in prompt
        assert "Task: Review code" in prompt


class TestPatterns:
    """Test pattern functionality."""

    def test_chain_of_thought(self):
        """Chain of thought pattern included."""
        builder = PromptBuilder().pattern("chain-of-thought")
        prompt = builder.build()
        assert "Think through this step-by-step" in prompt

    def test_self_consistency(self):
        """Self consistency pattern included."""
        builder = PromptBuilder().pattern("self-consistency")
        prompt = builder.build()
        assert "three different ways" in prompt

    def test_senior_reviewer(self):
        """Senior reviewer pattern included."""
        builder = PromptBuilder().pattern("senior-reviewer")
        prompt = builder.build()
        assert "senior engineer" in prompt

    def test_invalid_pattern_raises(self):
        """Invalid pattern raises PatternNotFoundError."""
        from llm_promptkit.patterns._registry import PatternNotFoundError

        builder = PromptBuilder()
        with pytest.raises(PatternNotFoundError) as exc_info:
            builder.pattern("non-existent-pattern")
        assert "Unknown pattern" in str(exc_info.value)
        assert "non-existent-pattern" in str(exc_info.value)

    def test_multiple_patterns(self):
        """Multiple patterns can be combined."""
        builder = PromptBuilder()
        builder.pattern("chain-of-thought").pattern("reflection")
        prompt = builder.build()
        assert "step-by-step" in prompt
        assert "review it critically" in prompt

    def test_all_patterns_exist(self):
        """All documented patterns are valid."""
        expected_patterns = [
            "chain-of-thought",
            "few-shot",
            "json-output",
            "senior-reviewer",
            "self-consistency",
            "tree-of-thought",
            "role-play",
            "step-back",
            "decomposition",
            "reflection",
        ]
        for pattern in expected_patterns:
            builder = PromptBuilder()
            builder.pattern(pattern)  # Should not raise


class TestContext:
    """Test context handling."""

    def test_context_included(self):
        """Context is wrapped in code block."""
        builder = PromptBuilder().context("def hello(): pass")
        prompt = builder.build()
        assert "def hello(): pass" in prompt
        assert "```" in prompt

    def test_context_with_task(self):
        """Context and task combine correctly."""
        builder = PromptBuilder()
        builder.task("Review this").context("code here")
        prompt = builder.build()
        assert "Task: Review this" in prompt
        assert "code here" in prompt


class TestExamples:
    """Test few-shot examples."""

    def test_single_example(self):
        """Single example is stored."""
        builder = PromptBuilder()
        builder.example("input1", "output1")
        assert len(builder._examples) == 1
        assert builder._examples[0] == {"input": "input1", "output": "output1"}

    def test_multiple_examples(self):
        """Multiple examples can be added."""
        builder = PromptBuilder()
        builder.example("in1", "out1").example("in2", "out2")
        assert len(builder._examples) == 2

    def test_examples_bulk(self):
        """Examples can be added in bulk."""
        builder = PromptBuilder()
        examples = [{"input": "a", "output": "b"}, {"input": "c", "output": "d"}]
        builder.examples(examples)
        assert len(builder._examples) == 2

    def test_few_shot_pattern_uses_examples(self):
        """Few-shot pattern formats examples."""
        builder = PromptBuilder()
        builder.pattern("few-shot")
        builder.example("2+2", "4")
        prompt = builder.build()
        assert "Input: 2+2" in prompt
        assert "Output: 4" in prompt


class TestOutputFormat:
    """Test output format handling."""

    def test_simple_format(self):
        """Simple format string is included."""
        builder = PromptBuilder().output_format("markdown")
        prompt = builder.build()
        assert "markdown" in prompt.lower()

    def test_json_with_schema(self):
        """JSON format includes schema."""
        builder = PromptBuilder()
        builder.output_format("json", schema={"name": "string", "age": "number"})
        prompt = builder.build()
        assert '"name"' in prompt
        assert '"age"' in prompt

    def test_json_output_pattern_with_schema(self):
        """JSON output pattern uses schema."""
        builder = PromptBuilder()
        builder.pattern("json-output")
        builder.output_format("json", schema={"result": "string"})
        prompt = builder.build()
        assert "valid JSON" in prompt
        assert '"result"' in prompt


class TestConstraints:
    """Test constraint handling."""

    def test_single_constraint(self):
        """Single constraint is included."""
        builder = PromptBuilder().constraint("Max 100 words")
        prompt = builder.build()
        assert "Max 100 words" in prompt
        assert "Constraints:" in prompt

    def test_multiple_constraints(self):
        """Multiple constraints are listed."""
        builder = PromptBuilder()
        builder.constraint("Max 100 words")
        builder.constraint("Use bullet points")
        prompt = builder.build()
        assert "Max 100 words" in prompt
        assert "Use bullet points" in prompt


class TestSystem:
    """Test system prompt handling."""

    def test_system_overrides_persona(self):
        """System prompt takes precedence over persona."""
        builder = PromptBuilder()
        builder.system("Custom system prompt")
        builder.persona("Developer")  # Should be ignored
        prompt = builder.build()
        assert "Custom system prompt" in prompt
        assert "Developer" not in prompt


class TestTokenEstimation:
    """Test token estimation."""

    def test_estimate_without_tiktoken(self):
        """Estimation works without tiktoken (rough estimate)."""
        builder = PromptBuilder()
        builder.task("This is a test task with some words")
        tokens = builder.estimate_tokens()
        # Rough estimate should be positive
        assert tokens > 0
        # Should be roughly chars/4
        prompt = builder.build()
        assert tokens == len(prompt) // 4


class TestFluentInterface:
    """Test fluent interface returns self."""

    def test_chaining(self):
        """All methods return self for chaining."""
        builder = PromptBuilder()
        result = (
            builder.persona("Dev")
            .pattern("chain-of-thought")
            .task("Do thing")
            .context("code")
            .example("in", "out")
            .output_format("json")
            .constraint("limit")
        )
        assert result is builder

    def test_str(self):
        """__str__ returns built prompt."""
        builder = PromptBuilder().task("Test")
        assert str(builder) == builder.build()

    def test_repr(self):
        """__repr__ shows useful info."""
        builder = PromptBuilder()
        builder.pattern("chain-of-thought").task("Test task")
        repr_str = repr(builder)
        assert "PromptBuilder" in repr_str
        assert "chain-of-thought" in repr_str
        assert "Test task" in repr_str
