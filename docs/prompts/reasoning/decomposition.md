[← Back to Reasoning Prompts](../index.md)

# Decomposition (Least-to-Most)

**Category:** reasoning
**Source:** Research (Zhou et al. 2022)

## When to Use

When facing a complex problem that's too hard to solve in one step.

## The Prompt

```
This is a complex problem. Let's break it down.

Problem: [INSERT COMPLEX PROBLEM]

Step 1: List all the sub-problems we need to solve first.

Step 2: Solve the simplest sub-problem.

Step 3: Use that solution to solve the next sub-problem.

Continue until all sub-problems are solved, then combine into final answer.
```

## How It Works

Complex problems overwhelm the model's "working memory" (context window attention). By decomposing into smaller pieces:
- Each sub-problem is tractable
- Solutions build on each other
- Errors are isolated to specific steps

## Example

```
Problem: "Build a user authentication system"

Sub-problems:
1. How to hash passwords securely
2. How to store user credentials
3. How to create login sessions
4. How to handle password reset
5. How to integrate with the app

[Solve each, then combine]
```

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| GPT-4 | Yes | Excellent decomposition |
| Claude | Yes | Very systematic |
| Llama 3 | Yes | Good |
