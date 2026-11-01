"""Pure doctor heuristics. Issue tuples and ordering are the public contract."""

import re
from typing import List, Optional, Tuple

Issue = Tuple[str, str, str, Optional[int], bool]

_VAGUE_PHRASES = ["make it good", "do it well", "as best as you can", "stuff", "things", "as soon as possible", "asap", "etc", "and so on", "whatever you think"]
_ROLE_PHRASES = ["you are a", "you are an", "role:", "persona:", "act as", "system:", "<role>", "<system_prompt>", "<persona>"]
_VERBOSE_PHRASES = ["please could you", "i would like you to", "if you don't mind", "can you please", "please", "thank you", "thanks", "kindly"]
_FORMAT_PHRASES = ["format", "json", "markdown", "output:", "structure", "return as"]
_EXAMPLE_PHRASES = ["example:", "example", "e.g.", "for instance", "few-shot", "here is an example"]
_NEGATIVE_PHRASES = ["don't", "do not", "never", "avoid", "must not", "stop"]
_AMBIGUOUS_PHRASES = ["maybe", "possibly", "might", "perhaps", "somewhat", "sort of", "kind of"]
_STOP_WORDS_BIGRAM = frozenset({"the", "a", "an", "is", "are", "in", "on", "at", "to", "of", "for", "and", "or", "it", "this", "that"})
_BOUNDARIES = ["Task:", "Context:", "Instructions:", "Task description:"]


def _match_phrase(text: str, phrase: str) -> bool:
    return bool(re.search(rf"(?<!\w){re.escape(phrase)}(?!\w)", text, re.IGNORECASE))


def _has_any_phrase(text: str, phrases: list) -> bool:
    return any(_match_phrase(text, phrase) for phrase in phrases)


def phrase_issues(text: str) -> List[Issue]:
    issues: List[Issue] = []
    for phrase in _VAGUE_PHRASES:
        if _match_phrase(text, phrase):
            issues.append(("Warning", "Vague or ambiguous instructions.", f"Found '{phrase}'. Be more specific.", None, False))
    if not _has_any_phrase(text, _ROLE_PHRASES):
        issues.append(("Suggestion", "Missing context or role definition.", "Add a persona (e.g., 'You are an expert...').", None, False))
    for phrase in _VERBOSE_PHRASES:
        if _match_phrase(text, phrase):
            issues.append(("Info", "Token inefficiency.", f"Found '{phrase}'. Use direct commands.", None, phrase == "please" or phrase in _VERBOSE_PHRASES[:4]))
    if not _has_any_phrase(text, _FORMAT_PHRASES):
        issues.append(("Warning", "Missing output format.", "Specify format (e.g., 'Output as JSON').", None, False))
    if not _has_any_phrase(text, _EXAMPLE_PHRASES):
        issues.append(("Info", "No examples provided.", "Few-shot examples improve output quality.", None, False))
    for phrase in _NEGATIVE_PHRASES:
        if _match_phrase(text, phrase):
            issues.append(("Warning", "Negative constraints.", f"Found '{phrase}'. LLMs follow positive instructions better (e.g., 'Do X' instead of 'Don't do Y').", None, False))
    return issues


def language_issues(text: str, text_no_code: str) -> List[Issue]:
    issues: List[Issue] = []
    for sent in re.split(r'[.!?]+', text_no_code):
        word_count = len(sent.split())
        if word_count > 40:
            line_num = text[:text.find(sent)].count("\n") + 1 if sent in text else None
            issues.append(("Warning", "Long sentence detected.", f"Sentence has {word_count} words. Break it into shorter sentences (max 40 words).", line_num, False))
            break
    words = text_no_code.lower().split()
    seen_bigrams: set = set()
    for i in range(len(words) - 1):
        bigram = f"{words[i]} {words[i + 1]}"
        if bigram in seen_bigrams and words[i] not in _STOP_WORDS_BIGRAM:
            issues.append(("Info", "Repeated bigram detected.", f"Found '{bigram}' repeated. Consider using varied phrasing.", None, False))
            break
        seen_bigrams.add(bigram)
    issues.extend(boundary_issues(text))
    for phrase in _AMBIGUOUS_PHRASES:
        if _match_phrase(text_no_code, phrase):
            issues.append(("Info", "Ambiguous language.", f"Found '{phrase}'. Use definitive language for clearer instructions.", None, False))
            break
    return issues


def boundary_issues(text: str) -> List[Issue]:
    issues: List[Issue] = []
    for marker in _BOUNDARIES:
        if marker not in text:
            continue
        marker_pos = text.find(marker)
        after_all = text[marker_pos + len(marker):]
        section_lines = []
        for line in after_all.lstrip("\n").split("\n"):
            if line.strip() and not any(line.strip().startswith(m) for m in _BOUNDARIES):
                section_lines.append(line)
            else:
                break
        section_content = "\n".join(section_lines).strip()
        if not section_content or len(section_content) < 10:
            line_num = text[:marker_pos].count("\n") + 1
            issues.append(("Suggestion", f"Empty section: '{marker.strip()}'", f"Add content after '{marker.strip()}' or remove the heading.", line_num, False))
    return issues


def analyze_prompt(text: str) -> List[Issue]:
    """Keep historical issue messages, tuple shape and ordering unchanged."""
    if not text.strip():
        return [("Error", "Prompt is empty.", "Please provide text to analyze.", None, False)]
    issues: List[Issue] = []
    text_no_code = re.sub(r"```.*?```", "", text, flags=re.DOTALL).strip()
    if len(text.strip()) < 20:
        issues.append(("Warning", "Prompt is very short.", "Prompts under 20 characters often lack sufficient detail.", None, False))
    if text_no_code:
        issues.extend(phrase_issues(text_no_code))
        issues.extend(language_issues(text, text_no_code))
    else:
        issues.append(("Info", "Prompt contains only code.", "No natural language instructions found. Consider adding context or formatting instructions.", None, False))
    if len(text.strip()) > 200:
        has_markdown = any(marker in text for marker in ["#", "```", "- ", "* ", "1. "])
        has_xml = bool(re.search(r"<[a-z_]+>", text, re.IGNORECASE))
        if not (has_markdown or has_xml):
            issues.append(("Suggestion", "Lacks structural formatting.", "Long prompt detected without markdown or XML structure. Use headers, bullet points, code blocks, or XML tags.", None, False))
    return issues
