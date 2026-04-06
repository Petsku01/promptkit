# Iterative Refinement Pattern

## Description

Start broad, then refine with follow-up prompts. Each turn narrows the output closer to what you want.

## When to use

Complex creative tasks, long documents, or when you don't know exactly what you want until you see a draft.

## When to avoid

When you can specify everything upfront — iterating wastes tokens and time.

## Template

```
Turn 1: [Broad initial request]
Turn 2: "Good, but [specific feedback]. Revise to [direction]."
Turn 3: "Almost. Change [specific element] and [specific element]."
Turn 4: "Final version. Polish for [audience/context]."
```

## Example

```
Turn 1: "Write a landing page headline for an AI writing tool aimed at marketers."
Turn 2: "Good, but too generic. Make it more specific about saving time on blog posts."
Turn 3: "Almost. Remove the exclamation mark, make it sound confident not excited."
Turn 4: "Final version. Polish for a SaaS landing page — professional, benefit-driven."
```

## Variations

- **Two-turn:** Initial + one revision
- **Multi-turn:** 5+ iterations for complex tasks
- **Self-refinement:** Ask the model to critique and improve its own output

## Tags

intermediate, creative, refinement, iteration
