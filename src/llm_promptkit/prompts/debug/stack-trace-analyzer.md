# Stack Trace Analyzer

**Category:** debug
**Source:** Best practices

## When to Use

Making sense of massive, unreadable error logs (e.g., Java Spring or React Native errors).

## The Prompt

```
Analyze the following stack trace. 

1. Identify the exact file and line number where the root cause originated (ignore library/framework internals unless relevant).
2. Explain the error in plain English.
3. Provide the top 3 most likely reasons this error occurred in this specific context.

[Insert Stack Trace]
```

## How It Works

It filters out the noise of framework boilerplate in stack traces and forces the LLM to pinpoint the developer's actual code that caused the crash.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| GPT-4 | Yes | Excellent |
| Claude | Yes | Very detailed |
| Llama 3 | Yes | Good |
