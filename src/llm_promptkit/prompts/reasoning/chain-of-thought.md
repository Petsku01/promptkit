# Zero-Shot Chain of Thought (CoT)

**Category:** reasoning
**Source:** Research (Wei et al. 2022)

## When to Use

Complex problem solving, logic puzzles, or math where the LLM might jump to a wrong conclusion if forced to answer immediately.

## The Prompt

```
[Insert your complex question or task here]

Let's think step by step.
```

## How It Works

Appending "Let's think step by step" forces the autoregressive model to generate intermediate reasoning tokens before outputting the final answer, significantly reducing logical errors and hallucinated math.

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `[question/task]` | Your complex problem | `What is 247 * 38?` |

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| GPT-4 | Yes | Excellent |
| Claude | Yes | Excellent |
| Llama 3 | Yes | Good |
