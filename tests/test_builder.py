import pytest
from promptkit.builder import PromptBuilder

def test_basic_build():
    builder = PromptBuilder()
    builder.persona("Senior Developer").task("Review code")
    prompt = builder.build()
    assert "You are a Senior Developer" in prompt
    assert "Task: Review code" in prompt

def test_pattern_addition():
    builder = PromptBuilder()
    builder.pattern("chain-of-thought")
    prompt = builder.build()
    assert "Think through this step-by-step" in prompt

def test_invalid_pattern():
    builder = PromptBuilder()
    with pytest.raises(ValueError):
        builder.pattern("non-existent-pattern")
