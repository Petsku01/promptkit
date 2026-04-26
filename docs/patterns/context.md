# Context Patterns

Patterns for managing examples, roles, and contextual information.

## few-shot

Provides positive examples to guide the model's output format and style.

```python
from llm_promptkit import PromptBuilder

builder = PromptBuilder()
builder.pattern("few-shot")
builder.example("2 + 2", "4")
builder.example("3 + 5", "8")
builder.task("Solve: 7 + 3")
prompt = builder.build()
```

**Best for:** Consistent output formatting, style transfer, task demonstration.

## few-shot-negatives

Provides both positive and negative examples, teaching the model what NOT to do.

```python
from llm_promptkit import PromptBuilder

builder = PromptBuilder()
builder.pattern("few-shot-negatives")
builder.task("Classify this review")
builder.example("Great product!", "positive")
builder.example("Terrible quality, waste of money", "negative")
builder.example("It's okay I guess", "neutral")
prompt = builder.build()
```

**Best for:** Classification tasks, boundary definition, reducing over-generation.

## role-play

Adopts a specific expert persona to frame the model's perspective.

```python
from llm_promptkit import PromptBuilder

builder = PromptBuilder()
builder.pattern("role-play")
builder.persona("Senior security auditor")
builder.task("Review this system architecture for security flaws")
prompt = builder.build()
```

**Best for:** Domain-specific analysis, perspective shifts, expert-level responses.