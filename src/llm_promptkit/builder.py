"""
PromptBuilder - Fluent API for composing prompts from patterns.
"""

import json
from typing import Dict, List, Optional

from llm_promptkit.patterns._registry import PatternNotFoundError, list_pattern_names, read_pattern


class PromptBuilder:
    """
    Fluent builder for composing prompts from patterns.

    Example:
        prompt = (PromptBuilder()
            .persona("Senior Developer")
            .pattern("chain-of-thought")
            .task("Review this code for bugs")
            .context(code_snippet)
            .output_format("json")
            .build())
    """

    @classmethod
    def get_available_patterns(cls) -> List[str]:
        """Return a copy of available pattern names.

        Use this instead of AVAILABLE_PATTERNS for forward compatibility.
        The return value is a fresh list — mutations do not affect the cache.
        """
        return list(list_pattern_names())

    # Backward-compatible attribute access via classproperty descriptor
    # Deprecated: use get_available_patterns() or list_pattern_names() instead
    AVAILABLE_PATTERNS: List[str] = []  # populated lazily via __init_subclass__ is not needed

    def __init_subclass__(cls, **kwargs):
        """Ensure subclasses don't inherit stale class-level state."""
        super().__init_subclass__(**kwargs)

    def __init__(self):
        self._system: Optional[str] = None
        self._persona: Optional[str] = None
        self._patterns: List[str] = []
        self._task: Optional[str] = None
        self._context: Optional[str] = None
        self._examples: List[Dict[str, str]] = []
        self._output_format: Optional[str] = None
        self._output_schema: Optional[Dict] = None
        self._constraints: List[str] = []

    def system(self, system_prompt: str) -> "PromptBuilder":
        """Set a custom system prompt."""
        self._system = system_prompt
        return self

    def persona(self, role: str) -> "PromptBuilder":
        """Set the AI persona/role."""
        self._persona = role
        return self

    def pattern(self, pattern_name: str) -> "PromptBuilder":
        """Add a prompt pattern by name.

        Raises:
            PatternNotFoundError: If the pattern name is not in the registry.
        """
        available = list_pattern_names()
        if pattern_name not in available:
            raise PatternNotFoundError(
                f"Unknown pattern '{pattern_name}'. Available: {', '.join(available)}"
            )
        self._patterns.append(pattern_name)
        return self

    def task(self, task_description: str) -> "PromptBuilder":
        """Set the main task/question."""
        self._task = task_description
        return self

    def context(self, context_text: str) -> "PromptBuilder":
        """Add context (code, document, data)."""
        self._context = context_text
        return self

    def example(self, input_text: str, output_text: str) -> "PromptBuilder":
        """Add a few-shot example."""
        self._examples.append({"input": input_text, "output": output_text})
        return self

    def examples(self, examples_list: List[Dict[str, str]]) -> "PromptBuilder":
        """Add multiple few-shot examples."""
        self._examples.extend(examples_list)
        return self

    def output_format(self, format_type: str, schema: Optional[Dict] = None) -> "PromptBuilder":
        """Specify output format (json, markdown, list, etc.)."""
        self._output_format = format_type
        self._output_schema = schema
        return self

    def constraint(self, constraint: str) -> "PromptBuilder":
        """Add a constraint/guardrail."""
        self._constraints.append(constraint)
        return self

    def build(self) -> str:
        """Build the final prompt string."""
        parts = []

        # System/Persona
        if self._system:
            parts.append(self._system)
        elif self._persona:
            parts.append(f"You are a {self._persona}.")

        # Patterns — loaded from .md files via registry
        for pattern_name in self._patterns:
            pattern_text = read_pattern(pattern_name)

            # Handle few-shot pattern specially
            if pattern_name == "few-shot" and self._examples:
                examples_text = "\n".join(
                    [f"Input: {ex['input']}\nOutput: {ex['output']}" for ex in self._examples]
                )
                pattern_text = pattern_text.format(examples=examples_text)

            # Handle json-output pattern specially
            if pattern_name == "json-output" and self._output_schema:
                pattern_text = pattern_text.format(schema=json.dumps(self._output_schema, indent=2))

            parts.append(pattern_text)

        # Constraints
        if self._constraints:
            constraints_text = "Constraints:\n" + "\n".join(f"- {c}" for c in self._constraints)
            parts.append(constraints_text)

        # Output format (if not using json-output pattern)
        if self._output_format and "json-output" not in self._patterns:
            if self._output_format == "json" and self._output_schema:
                parts.append(
                    f"Return valid JSON matching this schema:\n"
                    f"{json.dumps(self._output_schema, indent=2)}"
                )
            else:
                parts.append(f"Format your response as: {self._output_format}")

        # Task
        if self._task:
            parts.append(f"Task: {self._task}")

        # Context
        if self._context:
            parts.append(f"Context:\n```\n{self._context}\n```")

        return "\n\n".join(parts)

    def estimate_tokens(self, model: str = "gpt-4") -> int:
        """
        Estimate token count for the built prompt.

        Uses tiktoken for accurate counts when available (pip install llm-promptkit[tokens]).
        Falls back to a rough heuristic of ~4 chars per token for English text.
        """
        try:
            import tiktoken

            encoding = tiktoken.encoding_for_model(model)
            return len(encoding.encode(self.build()))
        except ImportError:
            # Rough estimate: ~4 chars per token (English text)
            return len(self.build()) // 4

    def __str__(self) -> str:
        return self.build()

    def __repr__(self) -> str:
        return f"PromptBuilder(patterns={self._patterns}, task={self._task!r})"
