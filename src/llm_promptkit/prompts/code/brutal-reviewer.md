# The Brutal Code Reviewer

**Category:** code
**Source:** Best practices

## When to Use

Finding hidden bugs, anti-patterns, or security flaws in a pull request.

## The Prompt

```
Review the following code snippet. Act as a ruthless, highly pedantic senior code reviewer. 

Focus on:
1. Security vulnerabilities
2. Time/Space complexity inefficiencies
3. Memory leaks or race conditions
4. Violations of SOLID principles

Do not praise the code. Only list actionable issues and provide the exact code changes needed to fix them.

[Insert Code]
```

## How It Works

LLMs are naturally sycophantic and tend to say "This looks great, but...". This prompt strips away the pleasantries and forces the model to heavily scrutinize the code for specific, high-level vulnerabilities.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| GPT-4 | Yes | Very thorough |
| Claude | Yes | Excellent critical analysis |
| Llama 3 | Partial | Sometimes too polite |
