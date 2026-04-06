# Zero-Shot Instruction Pattern

## Description

Give a clear instruction with no examples. The model relies entirely on its training.

## When to use

Simple, well-defined tasks where the model already knows the format (summarize, translate, classify).

## When to avoid

When the output format is unusual or the task is ambiguous — the model will guess.

## Template

```
[Task verb] the following [input type].

[Your input here]
```

## Example

```
Summarize the following customer review in one sentence.

"I've been using this project management tool for 6 months. The Kanban board is excellent, but the reporting dashboard is slow and the mobile app crashes frequently. Customer support responded within 2 hours though."
```

## Tags

beginner, instruction, simple
