"""
PromptBuilder - Fluent API for composing prompts from patterns.
"""

from typing import Optional, List, Dict, Any
from pathlib import Path
import json


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
    
    PATTERNS = {
        "chain-of-thought": "Think through this step-by-step:\n1. First, analyze the problem\n2. Then, consider possible approaches\n3. Finally, provide your solution\n\nShow your reasoning at each step.",
        "few-shot": "Here are some examples:\n{examples}\n\nNow apply the same approach to:",
        "json-output": "Return ONLY valid JSON matching this schema:\n{schema}\n\nNo explanation, no markdown, no code blocks.",
        "senior-reviewer": "You are a senior engineer with 15 years of experience. You are known for thorough, critical reviews. Never say 'looks good' unless it's genuinely excellent.",
        "self-consistency": "Solve this problem three different ways, then compare your answers and give the most likely correct one.",
        "tree-of-thought": "Imagine three different experts are answering this question. All experts will write down 1 step of their thinking, then share it with the group. Then all experts will go on to the next step, etc. If any expert realizes they are wrong at any point then they leave. The question is...",
        "role-play": "Act as a {role}. Write your response from this perspective, using appropriate tone, vocabulary, and addressing the specific concerns of someone in this position.",
        "step-back": "First, take a step back and identify the core principles or concepts that underlying this specific problem. Then, use those principles to solve the original problem.",
        "decomposition": "Break this complex problem down into 3-5 smaller, manageable sub-problems. Solve each sub-problem independently, then combine them to form the final solution.",
        "reflection": "After writing your initial response, review it critically. Identify any flaws, assumptions, or areas for improvement, and then provide a revised and improved final answer.",
    }
    
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
        """Add a prompt pattern by name."""
        if pattern_name not in self.PATTERNS:
            available = ", ".join(self.PATTERNS.keys())
            raise ValueError(f"Unknown pattern '{pattern_name}'. Available: {available}")
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
        
        # Patterns
        for pattern_name in self._patterns:
            pattern_text = self.PATTERNS[pattern_name]
            
            # Handle few-shot pattern specially
            if pattern_name == "few-shot" and self._examples:
                examples_text = "\n".join([
                    f"Input: {ex['input']}\nOutput: {ex['output']}"
                    for ex in self._examples
                ])
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
                parts.append(f"Return valid JSON matching this schema:\n{json.dumps(self._output_schema, indent=2)}")
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
        Requires tiktoken: pip install tiktoken
        """
        try:
            import tiktoken
            encoding = tiktoken.encoding_for_model(model)
            return len(encoding.encode(self.build()))
        except ImportError:
            # Rough estimate: ~4 chars per token
            return len(self.build()) // 4
    
    def __str__(self) -> str:
        return self.build()
    
    def __repr__(self) -> str:
        return f"PromptBuilder(patterns={self._patterns}, task={self._task!r})"
