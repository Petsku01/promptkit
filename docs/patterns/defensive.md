# Defensive Patterns

Patterns that reduce hallucinations, enforce accuracy, and improve safety.

## hallucination-reducer

Reduces confident but incorrect outputs by explicitly instructing the model to acknowledge uncertainty.

```python
from llm_promptkit import PromptBuilder

builder = PromptBuilder()
builder.pattern("hallucination-reducer")
builder.task("Answer questions about this document")
builder.context(document_text)
prompt = builder.build()
```

**Best for:** Factual QA, research tasks, any scenario where accuracy matters more than fluency.

**What it does:** Adds explicit instructions to:
- State confidence levels
- Admit uncertainty instead of guessing
- Distinguish between facts and inferences
- Flag when information is insufficient