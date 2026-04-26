[← Back to Code Prompts](../index.md)

# Test-Driven Development (TDD) Generator

**Category:** code
**Source:** Best practices

## When to Use

Writing robust code by focusing on edge cases first.

## The Prompt

```
I need a [LANGUAGE] function that [describe function purpose]. 

Before writing the function itself, write a comprehensive suite of unit tests for it. Include:
- Standard cases
- Edge cases
- Invalid inputs
- Performance bounds

Only after generating the tests, provide the implementation that will pass these tests.
```

## How It Works

It forces the LLM to define the constraints, types, and edge cases BEFORE writing the implementation. This usually results in much more robust and error-free code.

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `[LANGUAGE]` | Programming language | `Python` |
| `[purpose]` | What the function does | `validates email addresses` |

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| GPT-4 | Yes | Excellent |
| Claude | Yes | Excellent |
| Codex | Yes | Native strength |
