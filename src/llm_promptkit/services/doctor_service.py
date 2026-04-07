"""Rule-based prompt analysis service."""

import re
from typing import List

from ..doctor.constants import (
    EXAMPLE_PHRASES,
    FORMAT_PHRASES,
    NEGATIVE_PHRASES,
    ROLE_PHRASES,
    VAGUE_PHRASES,
    VERBOSE_PHRASES,
)
from ..doctor.models import DoctorIssue, IssueSeverity


def _match_phrase(text: str, phrase: str) -> bool:
    """Check if phrase exists as whole word in text."""
    return bool(re.search(rf"(?<!\w){re.escape(phrase)}(?!\w)", text, re.IGNORECASE))


def _has_any_phrase(text: str, phrases: list) -> bool:
    """Check if any phrase exists in text."""
    return any(_match_phrase(text, p) for p in phrases)


def analyze_prompt(text: str) -> List[DoctorIssue]:
    """Analyze prompt text and return detected issues."""
    issues: List[DoctorIssue] = []
    clean_text = (text or "").strip()

    if not clean_text:
        return [DoctorIssue(
            severity=IssueSeverity.CRITICAL,
            category="validation",
            issue="Prompt is empty.",
            suggestion="Please provide text to analyze."
        )]

    # Strip code blocks for NLP checks
    text_no_code = re.sub(r'```.*?```', '', text or '', flags=re.DOTALL).strip()

    if len(clean_text) < 20:
        issues.append(DoctorIssue(
            severity=IssueSeverity.WARNING,
            category="length",
            issue="Prompt is very short.",
            suggestion="Prompts under 20 characters often lack sufficient detail."
        ))

    # Only run NLP checks if there's non-code text
    if text_no_code:
        # Vague phrases
        for phrase in VAGUE_PHRASES:
            if _match_phrase(text_no_code, phrase):
                issues.append(DoctorIssue(
                    severity=IssueSeverity.WARNING,
                    category="clarity",
                    issue="Vague or ambiguous instructions.",
                    suggestion=f"Found '{phrase}'. Be more specific."
                ))

        # Missing role
        if not _has_any_phrase(text_no_code, ROLE_PHRASES):
            issues.append(DoctorIssue(
                severity=IssueSeverity.SUGGESTION,
                category="context",
                issue="Missing context or role definition.",
                suggestion="Add a persona (e.g., 'You are an expert...')."
            ))

        # Verbose phrasing
        for phrase in VERBOSE_PHRASES:
            if _match_phrase(text_no_code, phrase):
                issues.append(DoctorIssue(
                    severity=IssueSeverity.INFO,
                    category="efficiency",
                    issue="Token inefficiency.",
                    suggestion=f"Found '{phrase}'. Use direct commands."
                ))

        # Missing format
        if not _has_any_phrase(text_no_code, FORMAT_PHRASES):
            issues.append(DoctorIssue(
                severity=IssueSeverity.WARNING,
                category="output",
                issue="Missing output format.",
                suggestion="Specify format (e.g., 'Output as JSON')."
            ))

        # Missing examples
        if not _has_any_phrase(text_no_code, EXAMPLE_PHRASES):
            issues.append(DoctorIssue(
                severity=IssueSeverity.INFO,
                category="examples",
                issue="No examples provided.",
                suggestion="Few-shot examples improve output quality."
            ))

        # Negative phrasing
        for phrase in NEGATIVE_PHRASES:
            if _match_phrase(text_no_code, phrase):
                issues.append(DoctorIssue(
                    severity=IssueSeverity.WARNING,
                    category="constraints",
                    issue="Negative constraints.",
                    suggestion=f"Found '{phrase}'. LLMs follow positive instructions better (e.g., 'Do X' instead of 'Don\'t do Y')."
                ))
    else:
        issues.append(DoctorIssue(
            severity=IssueSeverity.INFO,
            category="content",
            issue="Prompt contains only code.",
            suggestion="No natural language instructions found. Consider adding context or formatting instructions."
        ))

    # Structural formatting check for longer prompts
    if len(clean_text) > 200:
        has_markdown = any(marker in text for marker in ["#", "```", "- ", "* ", "1. "])
        has_xml = bool(re.search(r'<[a-z_]+>', text, re.IGNORECASE))
        has_structure = has_markdown or has_xml
        if not has_structure:
            issues.append(DoctorIssue(
                severity=IssueSeverity.SUGGESTION,
                category="structure",
                issue="Lacks structural formatting.",
                suggestion="Long prompt detected without markdown or XML structure. Use headers, bullet points, code blocks, or XML tags."
            ))

    return issues
