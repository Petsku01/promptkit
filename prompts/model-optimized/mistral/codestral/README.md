# Codestral

## Characteristics
- **Type:** Code-specialized model
- **Context:** 32K tokens
- **Strengths:** Code generation, completion, explanation

## Prompt Examples

### Code Generation

```
Write a Python function that:
- Takes a list of integers
- Returns the sum of even numbers
- Handles empty lists

Include docstring and type hints.
```

### Code Explanation

```
Explain this code:

[paste code]

Cover:
1. What it does
2. How it works
3. Potential issues
```

### Code Review

```
Review this code for bugs and improvements:

[paste code]

Focus on: correctness, performance, readability
```

### Fill-in-the-Middle

```
# Implement the missing function
def validate_email(email: str) -> bool:
    <FILL>

# Should return True for valid emails, False otherwise
```

## Tips

- Works well with code context
- Supports many languages
- Good at explaining complex code
