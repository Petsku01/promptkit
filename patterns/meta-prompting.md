# Meta-Prompting Pattern

## Description

Ask the model to write a better prompt for your task. Use AI to improve your AI instructions.

## When to use

You're stuck on how to phrase a complex request, or you want to optimize an existing prompt.

## When to avoid

When you already know exactly what you want — meta-prompting adds a round-trip.

## Template

```
I want to [describe your goal in plain language].

Write me an optimized prompt that I can use with an LLM to achieve this goal. The prompt should:
- Be specific and unambiguous
- Include relevant constraints
- Specify the output format
- Anticipate edge cases
```

## Example

```
I want to turn customer support tickets into structured bug reports that my engineering team can act on.

Write me an optimized prompt that I can use with an LLM to achieve this goal. The prompt should:
- Be specific and unambiguous
- Include relevant constraints (what fields to extract)
- Specify the output format (JSON)
- Anticipate edge cases (vague tickets, feature requests disguised as bugs)
```

## Follow-up

After getting the meta-prompt, you can:
1. Refine it further ("Make it more concise")
2. Test it with real inputs
3. Iterate on the meta-prompt itself

## Tags

advanced, optimization, prompt-engineering, meta
