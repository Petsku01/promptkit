# Code Explanation Pattern

## Description

Explain code by breaking it down into understandable parts with context and rationale.

## When to use

When learning from code, documenting legacy systems, or onboarding developers.

## When to avoid

Code that is self-explanatory or where explanations add unnecessary verbosity.

## Template

```
Please explain the following code:

```
[CODE_BLOCK]
```

For each section:
1. **What it does**: High-level purpose
2. **How it works**: Key logic and flow
3. **Why it exists**: Business or technical rationale
4. **Potential issues**: Edge cases or tech debt
```

## Example

```
Please explain the following code:

```python
def retry_with_backoff(func, max_retries=3, base_delay=1):
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            delay = base_delay * (2 ** attempt)
            time.sleep(delay)
    return None
```

For each section:
1. **What it does**: High-level purpose
2. **How it works**: Key logic and flow
3. **Why it exists**: Business or technical rationale
4. **Potential issues**: Edge cases or tech debt
```

## Tags

code, explanation, documentation, learning
