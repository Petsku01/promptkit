[← Back to Reasoning Prompts](../index.md)

# Step-Back Prompting

**Category:** reasoning
**Source:** Research (Zheng et al. 2024)

## When to Use

When tackling a very specific, nuanced problem where the LLM gets lost in the details.

## The Prompt

```
[Insert specific problem details]

Before solving this specific problem, let's take a step back. What are the core underlying principles that govern this type of situation? Explain those principles first, and then apply them to the specific problem.
```

## How It Works

It abstracts the problem to a higher-level concept first. Grounding the LLM in fundamental principles before tackling the specifics prevents it from getting derailed by irrelevant details.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| GPT-4 | Yes | Excellent |
| Claude | Yes | Excellent |
| Llama 3 | Yes | Good |
