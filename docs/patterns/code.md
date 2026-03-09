# Code Patterns

Patterns for development tasks.

## Senior Reviewer

Strict, critical code review.

```python
from llm_promptkit import PromptBuilder

prompt = (PromptBuilder()
    .pattern("senior-reviewer")
    .task("Review this pull request")
    .context(diff)
    .build())
```

**The prompt includes:**
```
You are a senior engineer with 15 years of experience. 
You are known for thorough, critical reviews. 
Never say 'looks good' unless it's genuinely excellent.
```

---

## Code Review Combo

Combine patterns for thorough review:

```python
prompt = (PromptBuilder()
    .pattern("senior-reviewer")
    .pattern("chain-of-thought")
    .task("Review this code for security issues")
    .context(code)
    .constraint("Focus on: injection, auth, data exposure")
    .build())
```

---

## Debugging

```python
prompt = (PromptBuilder()
    .pattern("step-back")
    .pattern("decomposition")
    .task("Why is this failing?")
    .context(f"Error: {error}\n\nCode:\n{code}")
    .build())
```

---

## TDD Prompting

Generate tests first:

```python
prompt = (PromptBuilder()
    .persona("TDD practitioner")
    .task("Write tests for this function, then implement it")
    .context(function_signature)
    .constraint("Write failing tests first")
    .constraint("Then write minimal code to pass")
    .build())
```

---

## Code Generation

```python
prompt = (PromptBuilder()
    .persona("Senior Python developer")
    .pattern("decomposition")
    .task("Implement a rate limiter")
    .constraint("Use stdlib only")
    .constraint("Thread-safe")
    .constraint("Include docstrings")
    .build())
```
