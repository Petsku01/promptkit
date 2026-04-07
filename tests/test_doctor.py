"""Tests for the prompt doctor."""

import pytest

from llm_promptkit.doctor import Severity, analyze_prompt


def _issues_with(result, needle: str):
    return [i for i in result if needle.lower() in i.issue.lower() or needle.lower() in i.suggestion.lower()]


def test_detects_vague_phrase():
    result = analyze_prompt("Make it good please")
    assert _issues_with(result, "vague")


def test_detects_multiple_vague_phrases():
    result = analyze_prompt("Do it well and finish asap")
    assert len(_issues_with(result, "vague")) >= 2


def test_specific_instruction_no_vague():
    result = analyze_prompt("Refactor this function to use list comprehension")
    assert not _issues_with(result, "vague")


def test_missing_role():
    result = analyze_prompt("Summarize this code into 5 bullets in markdown")
    role_issues = _issues_with(result, "role")
    assert role_issues
    assert role_issues[0].severity == Severity.SUGGESTION


def test_role_present():
    result = analyze_prompt("You are a senior Python engineer. Summarize this code in markdown")
    assert not _issues_with(result, "role")


def test_token_inefficiency():
    result = analyze_prompt("Please kindly review this and thank you")
    assert len(_issues_with(result, "token inefficiency")) >= 3


def test_missing_output_format():
    result = analyze_prompt("You are a reviewer. Analyze this function for bugs.")
    assert _issues_with(result, "output format")


def test_output_format_present():
    result = analyze_prompt("You are a reviewer. Return output: JSON with fields severity and fix.")
    assert not _issues_with(result, "output format")


@pytest.mark.parametrize("text", [
    "Don't use recursion; return JSON output",
    "Do not include personal data in output: markdown",
    "Never expose secrets. Output: json",
])
def test_negative_constraints(text):
    result = analyze_prompt(text)
    assert _issues_with(result, "negative constraints")


def test_empty_prompt():
    result = analyze_prompt("")
    assert result[0].severity == Severity.CRITICAL
    assert "empty" in result[0].issue.lower()


def test_long_prompt_structure_suggestion():
    long_text = "You are a reviewer. Output as JSON. " + ("analyze this requirement in detail " * 30)
    result = analyze_prompt(long_text)
    assert _issues_with(result, "structural formatting")


def test_code_blocks_skip_nlp():
    prompt = "```\nmake it good please and do it well asap\n```"
    result = analyze_prompt(prompt)
    assert not _issues_with(result, "vague")
    assert _issues_with(result, "contains only code")
