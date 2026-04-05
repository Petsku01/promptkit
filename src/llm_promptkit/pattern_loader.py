"""Utilities for loading prompt patterns from markdown files."""

from pathlib import Path
from typing import Dict
import re


class PatternLoader:
    """Load prompt patterns from a patterns directory tree."""

    TEMPLATE_HEADERS = ("template", "prompt")

    def load_from_directory(self, patterns_dir: Path) -> Dict[str, str]:
        """
        Load all .md patterns from ``patterns_dir`` recursively.

        Pattern names are derived from filename stems (e.g. chain-of-thought.md -> chain-of-thought).
        """
        if not patterns_dir.exists() or not patterns_dir.is_dir():
            return {}

        patterns: Dict[str, str] = {}

        for md_file in sorted(patterns_dir.rglob("*.md")):
            name = md_file.stem
            content = md_file.read_text(encoding="utf-8")
            template = self._extract_pattern_text(content)
            if template:
                patterns[name] = template

        return patterns

    def _extract_pattern_text(self, markdown: str) -> str:
        """
        Extract pattern text from markdown.

        Priority:
        1) Content under a "## Template" (or "## Prompt") heading.
        2) Content after the first top-level header line (# ...).
        3) Whole markdown as a final fallback.
        """
        text = markdown.strip()
        if not text:
            return ""

        lines = text.splitlines()

        template_start = None
        for i, line in enumerate(lines):
            m = re.match(r"^##\s+(.+?)\s*$", line.strip(), flags=re.IGNORECASE)
            if not m:
                continue
            heading = m.group(1).strip().lower()
            if any(h in heading for h in self.TEMPLATE_HEADERS):
                template_start = i + 1
                break

        if template_start is not None:
            end = len(lines)
            for j in range(template_start, len(lines)):
                if re.match(r"^##\s+", lines[j].strip()):
                    end = j
                    break
            section = "\n".join(lines[template_start:end]).strip()
            if section:
                return self._strip_code_fences(section)

        first_h1 = None
        for i, line in enumerate(lines):
            if re.match(r"^#\s+", line.strip()):
                first_h1 = i
                break

        if first_h1 is not None and first_h1 + 1 < len(lines):
            remainder = "\n".join(lines[first_h1 + 1 :]).strip()
            if remainder:
                return remainder

        return text

    @staticmethod
    def _strip_code_fences(text: str) -> str:
        """Remove a single wrapping markdown code fence when present."""
        stripped = text.strip()
        if stripped.startswith("```") and stripped.endswith("```"):
            parts = stripped.splitlines()
            if len(parts) >= 2:
                return "\n".join(parts[1:-1]).strip()
        return stripped
