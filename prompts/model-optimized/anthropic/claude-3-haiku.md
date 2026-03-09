# Claude 3 Haiku Prompting Guide

## Model Characteristics
- **Context:** 200K tokens
- **Strengths:** Speed, low cost, efficiency
- **Best for:** Simple tasks, classification, extraction, high volume

## Key Principle

Keep prompts SHORT and DIRECT. Haiku is optimized for speed.

## Chain of Thought

Use simplified version:

```
Solve step by step:
1. [step]
2. [step]
3. Answer: [answer]
```

## JSON Output

```
Return JSON only:
{"field": "value"}
```

## Classification

```
Classify this text as: positive, negative, or neutral.
Text: [input]
Classification:
```

## Extraction

```
Extract from this text:
- Name:
- Date:
- Amount:

Text: [input]
```

## Key Tips

- Shorter prompts = faster responses
- Skip elaborate XML for simple tasks
- Best for:
  - Classification
  - Entity extraction
  - Simple Q&A
  - High-volume processing
- Not ideal for complex reasoning
- Use Sonnet/Opus for harder tasks
