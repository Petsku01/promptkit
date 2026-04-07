"""Rule-based prompt analysis — the 'prompt doctor'."""

import re
from dataclasses import dataclass
from enum import Enum
from typing import List

VAGUE_PHRASES = [
    "make it good", "do it well", "as best as you can", "stuff", "things",
    "as soon as possible", "asap", "etc", "and so on", "whatever you think",
]
ROLE_PHRASES = [
    "you are a", "you are an", "role:", "persona:", "act as",
    "system:", "<role>", "<system_prompt>", "<persona>",
]
VERBOSE_PHRASES = [
    "please could you", "i would like you to", "if you don't mind",
    "can you please", "please", "thank you", "thanks", "kindly",
]
FORMAT_PHRASES = ["format", "json", "markdown", "output:", "structure", "return as"]
EXAMPLE_PHRASES = ["example:", "example", "e.g.", "for instance", "few-shot", "here is an example"]
NEGATIVE_PHRASES = ["don't", "do not", "never", "avoid", "must not", "stop"]


class Severity(Enum):
    CRITICAL = "Critical"
    WARNING = "Warning"
    SUGGESTION = "Suggestion"
    INFO = "Info"


@dataclass
class Issue:
    severity: Severity
    category: str
    issue: str
    suggestion: str


def _match(text: str, phrase: str) -> bool:
    return bool(re.search(rf"(?<!\w){re.escape(phrase)}(?!\w)", text, re.IGNORECASE))


def _has_any(text: str, phrases: list) -> bool:
    return any(_match(text, p) for p in phrases)


def analyze_prompt(text: str) -> List[Issue]:
    """Analyze prompt text and return detected issues."""
    issues: List[Issue] = []
    clean = (text or "").strip()

    if not clean:
        return [Issue(Severity.CRITICAL, "validation", "Prompt is empty.", "Please provide text to analyze.")]

    text_no_code = re.sub(r'```.*?```', '', text or '', flags=re.DOTALL).strip()

    if len(clean) < 20:
        issues.append(Issue(Severity.WARNING, "length", "Prompt is very short.",
                            "Prompts under 20 characters often lack sufficient detail."))

    if text_no_code:
        for phrase in VAGUE_PHRASES:
            if _match(text_no_code, phrase):
                issues.append(Issue(Severity.WARNING, "clarity", "Vague or ambiguous instructions.",
                                    f"Found '{phrase}'. Be more specific."))

        if not _has_any(text_no_code, ROLE_PHRASES):
            issues.append(Issue(Severity.SUGGESTION, "context", "Missing context or role definition.",
                                "Add a persona (e.g., 'You are an expert...')."))

        for phrase in VERBOSE_PHRASES:
            if _match(text_no_code, phrase):
                issues.append(Issue(Severity.INFO, "efficiency", "Token inefficiency.",
                                    f"Found '{phrase}'. Use direct commands."))

        if not _has_any(text_no_code, FORMAT_PHRASES):
            issues.append(Issue(Severity.WARNING, "output", "Missing output format.",
                                "Specify format (e.g., 'Output as JSON')."))

        if not _has_any(text_no_code, EXAMPLE_PHRASES):
            issues.append(Issue(Severity.INFO, "examples", "No examples provided.",
                                "Few-shot examples improve output quality."))

        for phrase in NEGATIVE_PHRASES:
            if _match(text_no_code, phrase):
                issues.append(Issue(Severity.WARNING, "constraints", "Negative constraints.",
                                    f"Found '{phrase}'. LLMs follow positive instructions better."))
    else:
        issues.append(Issue(Severity.INFO, "content", "Prompt contains only code.",
                            "No natural language instructions found. Consider adding context."))

    if len(clean) > 200:
        has_markdown = any(m in text for m in ["#", "```", "- ", "* ", "1. "])
        has_xml = bool(re.search(r'<[a-z_]+>', text, re.IGNORECASE))
        if not has_markdown and not has_xml:
            issues.append(Issue(Severity.SUGGESTION, "structure", "Lacks structural formatting.",
                                "Long prompt without markdown or XML structure. Use headers or bullet points."))

    return issues
