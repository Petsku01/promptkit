# Self-Refinement

**Category:** reasoning
**Source:** Research (Madaan et al. 2023)

## When to Use

When you want the AI to improve its own output iteratively.

## The Prompt

```
[TASK DESCRIPTION]

After your initial response, critique your own answer:
1. What are the weaknesses or gaps?
2. What could be improved?
3. What did you miss?

Then provide an improved version addressing these issues.

Repeat this refinement process once more for a final polished answer.
```

## How It Works

Forces the model to engage in metacognition - thinking about its own thinking. Each iteration catches errors and adds depth that the previous version missed.

## Example

```
Write a function to validate email addresses.

[Initial attempt]

Self-critique:
- Missing: international domain support
- Weakness: doesn't handle edge cases like consecutive dots
- Could improve: add specific error messages

[Refined version with improvements]
```

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| GPT-4 | Yes | Excellent |
| Claude | Yes | Very thorough critique |
| Llama 3 | Partial | May need explicit guidance |
