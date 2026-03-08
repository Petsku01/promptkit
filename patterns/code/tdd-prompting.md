# TDD Prompting (Test-Driven Generation)

## When to Use

- Generating code that must be correct
- When requirements are clear but implementation is complex
- Avoiding common bugs through test-first thinking
- Getting code that's actually testable

## How It Works

By asking the LLM to write tests FIRST, you force it to:

1. **Clarify requirements** — Tests make implicit requirements explicit
2. **Think about edge cases** — Good tests cover boundaries
3. **Produce testable code** — Implementation must satisfy tests

This mirrors human TDD: red → green → refactor.

## The Prompt

```
I need a function that [FUNCTION_DESCRIPTION].

First, write 5-7 unit tests that this function must pass. Include:
- Happy path cases
- Edge cases (empty input, boundary values)
- Error cases

Then, implement the function to pass all tests.

Use [LANGUAGE] and [TEST_FRAMEWORK].
```

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `[FUNCTION_DESCRIPTION]` | What the function does | `validates email addresses` |
| `[LANGUAGE]` | Programming language | `Python` |
| `[TEST_FRAMEWORK]` | Testing framework | `pytest` |

## Example

**Input:**
```
I need a function that calculates the nth Fibonacci number.

First, write 5-7 unit tests that this function must pass. Include:
- Happy path cases
- Edge cases (n=0, n=1, negative n)
- Error cases

Then, implement the function to pass all tests.

Use Python and pytest.
```

**Output:**
```python
# Tests first
import pytest

def test_fib_zero():
    assert fibonacci(0) == 0

def test_fib_one():
    assert fibonacci(1) == 1

def test_fib_small():
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55

def test_fib_negative():
    with pytest.raises(ValueError):
        fibonacci(-1)

def test_fib_large():
    assert fibonacci(20) == 6765

def test_fib_type_error():
    with pytest.raises(TypeError):
        fibonacci("5")

# Implementation
def fibonacci(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| GPT-4 | ✅ | Excellent test coverage |
| Claude 3.5 | ✅ | Very thorough edge cases |
| Llama 3 70B | ⚠️ | Sometimes skips error cases |
| Codex | ✅ | Native strength |

## Variations

- **Property-based:** Ask for hypothesis/property tests instead
- **Integration tests:** For API endpoints or database operations
- **Mutation testing:** Ask "what changes would break each test?"

## Common Mistakes

- ❌ Vague requirements — be specific about expected behavior
- ❌ Skipping edge cases — explicitly ask for boundary testing
- ❌ No error handling — always include "error cases"

## Related Patterns

- [Edge-Case Hunter](./edge-case-hunter.md) — Focus purely on finding edge cases
- [Senior Reviewer](../review/senior-reviewer.md) — Review the generated code

---

*Last tested: 2026-03-08*
