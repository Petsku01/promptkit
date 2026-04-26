"""Tests for PromptBuilder."""

import pytest

from llm_promptkit.builder import PromptBuilder


class TestBasicBuild:
    def test_empty_build(self):
        builder = PromptBuilder()
        assert builder.build() == ""

    def test_persona_only(self):
        prompt = PromptBuilder().persona("Senior Developer").build()
        assert "You are a Senior Developer" in prompt

    def test_task_only(self):
        prompt = PromptBuilder().task("Review code").build()
        assert "Task: Review code" in prompt

    def test_persona_and_task(self):
        builder = PromptBuilder()
        builder.persona("Senior Developer").task("Review code")
        prompt = builder.build()
        assert "You are a Senior Developer" in prompt
        assert "Task: Review code" in prompt


class TestPatterns:
    def test_chain_of_thought(self):
        prompt = PromptBuilder().pattern("chain-of-thought").build()
        assert "Think through this step-by-step" in prompt

    def test_self_consistency(self):
        prompt = PromptBuilder().pattern("self-consistency").build()
        assert "three different ways" in prompt

    def test_senior_reviewer(self):
        prompt = PromptBuilder().pattern("senior-reviewer").build()
        assert "senior engineer" in prompt

    def test_invalid_pattern_raises(self):
        from llm_promptkit.patterns._registry import PatternNotFoundError

        builder = PromptBuilder()
        with pytest.raises(PatternNotFoundError) as exc_info:
            builder.pattern("non-existent-pattern")
        assert "Unknown pattern" in str(exc_info.value)
        assert "non-existent-pattern" in str(exc_info.value)

    def test_multiple_patterns(self):
        builder = PromptBuilder()
        builder.pattern("chain-of-thought").pattern("reflection")
        prompt = builder.build()
        assert "step-by-step" in prompt
        assert "review it critically" in prompt

    def test_all_patterns_exist(self):
        expected = [
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
        for pattern in expected:
            PromptBuilder().pattern(pattern)


class TestContext:
    def test_context_included(self):
        prompt = PromptBuilder().context("def hello(): pass").build()
        assert "def hello(): pass" in prompt
        assert "```" in prompt

    def test_context_with_task(self):
        builder = PromptBuilder()
        builder.task("Review this").context("code here")
        prompt = builder.build()
        assert "Task: Review this" in prompt
        assert "code here" in prompt


class TestExamples:
    def test_single_example(self):
        builder = PromptBuilder()
        builder.example("input1", "output1")
        assert len(builder._examples) == 1
        assert builder._examples[0] == {"input": "input1", "output": "output1"}

    def test_multiple_examples(self):
        builder = PromptBuilder()
        builder.example("in1", "out1").example("in2", "out2")
        assert len(builder._examples) == 2

    def test_examples_bulk(self):
        builder = PromptBuilder()
        builder.examples([{"input": "a", "output": "b"}, {"input": "c", "output": "d"}])
        assert len(builder._examples) == 2

    def test_examples_invalid_keys_raises(self):
        builder = PromptBuilder()
        with pytest.raises(ValueError, match="input.*output"):
            builder.examples([{"question": "what?", "answer": "42"}])

    def test_few_shot_pattern_uses_examples(self):
        builder = PromptBuilder()
        builder.pattern("few-shot").example("2+2", "4")
        prompt = builder.build()
        assert "Input: 2+2" in prompt
        assert "Output: 4" in prompt


class TestOutputFormat:
    def test_simple_format(self):
        prompt = PromptBuilder().output_format("markdown").build()
        assert "markdown" in prompt.lower()

    def test_json_with_schema(self):
        builder = PromptBuilder()
        builder.output_format("json", schema={"name": "string", "age": "number"})
        prompt = builder.build()
        assert '"name"' in prompt
        assert '"age"' in prompt

    def test_json_output_pattern_with_schema(self):
        builder = PromptBuilder()
        builder.pattern("json-output")
        builder.output_format("json", schema={"result": "string"})
        prompt = builder.build()
        assert "valid JSON" in prompt
        assert '"result"' in prompt


class TestConstraints:
    def test_single_constraint(self):
        prompt = PromptBuilder().constraint("Max 100 words").build()
        assert "Max 100 words" in prompt
        assert "Constraints:" in prompt

    def test_multiple_constraints(self):
        builder = PromptBuilder()
        builder.constraint("Max 100 words").constraint("Use bullet points")
        prompt = builder.build()
        assert "Max 100 words" in prompt
        assert "Use bullet points" in prompt


class TestSystem:
    def test_system_overrides_persona(self):
        builder = PromptBuilder()
        builder.system("Custom system prompt").persona("Developer")
        prompt = builder.build()
        assert "Custom system prompt" in prompt
        assert "Developer" not in prompt


class TestTokenEstimation:
    def test_estimate_without_tiktoken(self):
        builder = PromptBuilder()
        builder.task("This is a test task with some words")
        tokens = builder.estimate_tokens()
        assert tokens > 0
        prompt = builder.build()
        assert tokens == len(prompt) // 4


class TestFluentInterface:
    def test_chaining(self):
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
        builder = PromptBuilder().task("Test")
        assert str(builder) == builder.build()

    def test_repr(self):
        builder = PromptBuilder()
        builder.pattern("chain-of-thought").task("Test task")
        repr_str = repr(builder)
        assert "PromptBuilder" in repr_str
        assert "chain-of-thought" in repr_str
        assert "Test task" in repr_str
