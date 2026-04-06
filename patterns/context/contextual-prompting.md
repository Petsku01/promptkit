# Contextual Prompting Pattern

## Description

Provide rich context including background, constraints, and relevant information to help the model understand the full picture.

## When to use

When the task requires understanding of domain-specific knowledge, historical context, or situational awareness that the model may not have.

## When to avoid

Simple tasks where extra context adds noise and increases token cost unnecessarily.

## Template

```
## Background
[Provide relevant background information]

## Current Situation
[Describe the current state or problem]

## Constraints
- [Constraint 1]
- [Constraint 2]
- [Constraint 3]

## Task
[The specific task to perform]

## Success Criteria
[How to evaluate a good response]
```

## Example

```
## Background
We are a fintech startup launching a new mobile banking app for Gen Z users. Our brand voice is friendly but professional.

## Current Situation
We need to announce our new "Round Up Savings" feature that automatically rounds up purchases and saves the difference.

## Constraints
- Must comply with financial regulations (include disclaimer)
- Tone should be energetic but not hype-y
- Avoid jargon like "financial wellness" or "empower"
- Maximum 200 words

## Task
Write a feature announcement for our blog.

## Success Criteria
A 18-year-old should understand the feature and want to try it.
```

## Tags

context, background, constraints, situational
