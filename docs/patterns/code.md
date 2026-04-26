# Code Patterns

Patterns for software development tasks.

## TDD Prompting

Generate tests first, then implementation.

```python
from llm_promptkit import PromptBuilder

prompt = (PromptBuilder()
    .pattern("tdd-prompting")
    .task("Implement a user authentication module")
    .build())
```

**When to use:** Writing new features, ensuring testability.

---

## Stack Trace Decoder

Analyze and explain stack traces.

```python
prompt = (PromptBuilder()
    .pattern("stack-trace-decoder")
    .task("Debug this error")
    .context(traceback_text)
    .build())
```

**When to use:** Debugging errors, understanding crashes.