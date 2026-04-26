[← Back to Context Prompts](../index.md)

# Few-Shot with Negatives

**Category:** context
**Source:** Best practices

## When to Use

When you need to teach the model by showing both good AND bad examples.

## The Prompt

```
I'll show you examples of good and bad [TASK]. Learn from both.

GOOD Example 1:
Input: [input]
Output: [correct output]
Why it's good: [explanation]

BAD Example 1:
Input: [input]
Output: [incorrect output]
Why it's bad: [explanation]

GOOD Example 2:
Input: [input]
Output: [correct output]

BAD Example 2:
Input: [input]
Output: [incorrect output]
Why it's bad: [explanation]

Now apply this to:
[YOUR INPUT]
```

## How It Works

Negative examples create decision boundaries. The model learns not just WHAT to do, but explicitly WHAT NOT to do. This is especially powerful for style, formatting, and avoiding common mistakes.

## Example

```
GOOD: "The user clicked the submit button" (active voice)
BAD: "The submit button was clicked by the user" (passive - avoid)

GOOD: "Returns null if not found" (concise)
BAD: "This function will return a null value in the case that..." (verbose - avoid)
```

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| GPT-4 | Yes | Learns well from contrast |
| Claude | Yes | Excellent |
| Llama 3 | Yes | Good |
