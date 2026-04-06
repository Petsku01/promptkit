import pytest

from llm_promptkit.doctor.models import IssueSeverity
from llm_promptkit.services import analyze_prompt


def _issues_with(result, needle: str):
    return [i for i in result if needle.lower() in i.issue.lower() or needle.lower() in i.suggestion.lower()]


def test_detects_vague_phrase_make_it_good():
    result = analyze_prompt("Make it good please")
    vague_issues = _issues_with(result, "vague")
    assert vague_issues
    assert vague_issues[0].severity == IssueSeverity.WARNING


def test_detects_vague_phrase_do_it_well_and_asap():
    result = analyze_prompt("Do it well and finish asap")
    vague_issues = _issues_with(result, "vague")
    assert len(vague_issues) >= 2


def test_specific_instruction_has_no_vague_issue():
    result = analyze_prompt("Refactor this function to use list comprehension")
    vague_issues = _issues_with(result, "vague")
    assert not vague_issues


def test_missing_role_triggers_warning():
    result = analyze_prompt("Summarize this code into 5 bullets in markdown")
    role_issues = _issues_with(result, "role")
    assert role_issues
    assert role_issues[0].severity == IssueSeverity.SUGGESTION


def test_role_present_passes_role_check():
    result = analyze_prompt("You are a senior Python engineer. Summarize this code in markdown")
    role_issues = _issues_with(result, "role")
    assert not role_issues


def test_token_inefficiency_detects_politeness_words():
    result = analyze_prompt("Please kindly review this and thank you")
    token_issues = _issues_with(result, "token inefficiency")
    assert len(token_issues) >= 3
    assert all(i.severity == IssueSeverity.INFO for i in token_issues)


def test_direct_command_has_no_token_inefficiency():
    result = analyze_prompt("Review this code and return JSON output")
    token_issues = _issues_with(result, "token inefficiency")
    assert not token_issues


def test_missing_output_format_detected():
    result = analyze_prompt("You are a reviewer. Analyze this function for bugs.")
    fmt_issues = _issues_with(result, "output format")
    assert fmt_issues
    assert fmt_issues[0].severity == IssueSeverity.WARNING


def test_output_format_present_passes_check():
    result = analyze_prompt("You are a reviewer. Return output: JSON with fields severity and fix.")
    fmt_issues = _issues_with(result, "output format")
    assert not fmt_issues


@pytest.mark.parametrize("text", [
    "Don't use recursion; return JSON output",
    "Do not include personal data in output: markdown",
    "Never expose secrets. Output: json",
])
def test_negative_constraints_detected(text):
    result = analyze_prompt(text)
    neg_issues = _issues_with(result, "negative constraints")
    assert neg_issues
    assert all(i.severity == IssueSeverity.WARNING for i in neg_issues)


def test_empty_prompt_returns_error():
    result = analyze_prompt("")
    assert result
    assert result[0].severity == IssueSeverity.CRITICAL
    assert "empty" in result[0].issue.lower()


def test_very_long_prompt_can_trigger_structure_suggestion():
    long_text = "You are a reviewer. Output as JSON. " + ("analyze this requirement in detail " * 30)
    result = analyze_prompt(long_text)
    structure_issues = _issues_with(result, "structural formatting")
    assert structure_issues
    assert structure_issues[0].severity == IssueSeverity.SUGGESTION


def test_code_blocks_skip_nlp_phrase_detection_inside_code():
    prompt = "```\nmake it good please and do it well asap\n```"
    result = analyze_prompt(prompt)
    vague_issues = _issues_with(result, "vague")
    assert not vague_issues
    code_only = _issues_with(result, "contains only code")
    assert code_only
