# Gemma 2 (Google)

## Ominaisuudet
- **Sizes:** 2B, 9B, 27B
- **Konteksti:** 8K tokens
- **Strengths:** Efficient, good price-quality

## Prompts

Use the same short prompts as Phi:
- [../phi-3.5/basic.md](../phi-3.5/basic.md)
- [../phi-3.5/coding.md](../phi-3.5/coding.md)

## Examples

### Classification
```
Classify as positive/negative/neutral:
[text]
Answer:
```

### Summary
```
Summarize in 1-2 sentences:
[text]
Summary:
```

### QA
```
Q: [question]
Context: [context]
A:
```

## Notes

- 2B very limited - only simplest tasks
- 9B good general model
- 27B approaches mid-size model level
- Short context (8K) - no long documents
