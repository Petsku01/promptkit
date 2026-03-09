# Claude 3 Haiku Prompting Guide

## Model Characteristics
- **Context:** 200K tokens
- **Strengths:** Speed, low cost, efficiency
- **Best for:** Simple tasks, classification, extraction, high volume

## Key Principle

**SHORT prompts. DIRECT instructions. FAST responses.**

---

## Prompt 1: Classification

```
Classify as: positive, negative, or neutral.

Text: [input]
Classification:
```

---

## Prompt 2: Entity Extraction

```
Extract from text:
- Names:
- Dates:
- Amounts:
- Locations:

Text: [input]
```

---

## Prompt 3: Yes/No Question

```
Answer yes or no.

Question: [question]
Context: [brief context]

Answer:
```

---

## Prompt 4: Simple Summary

```
Summarize in 2 sentences:

[text]

Summary:
```

---

## Prompt 5: Format Conversion

```
Convert to JSON:
{"name": "", "email": "", "phone": ""}

Input: John Smith, john@email.com, 555-1234

JSON:
```

---

## Prompt 6: Language Detection

```
What language is this? Reply with language name only.

Text: [input]
Language:
```

---

## Prompt 7: Keyword Extraction

```
List 5 keywords from this text:

[text]

Keywords:
```

---

## Prompt 8: Spam Detection

```
Is this spam? Reply: spam or not_spam

Message: [input]
Result:
```

---

## Prompt 9: Data Cleaning

```
Fix formatting issues:
- Capitalize names
- Format phone as XXX-XXX-XXXX
- Format date as YYYY-MM-DD

Input: [messy data]
Output:
```

---

## Prompt 10: Quick Q&A

```
Answer briefly (1-2 sentences).

Q: [question]
A:
```

---

## What NOT to Use Haiku For

 Complex reasoning
 Long-form writing
 Nuanced analysis
 Multi-step problems
 Code generation (use Sonnet)

-> Use Sonnet or Opus for these.

---

## Key Tips

- Shorter prompt = faster response
- Skip XML tags for simple tasks
- One task per prompt
- High volume? Haiku is most cost-effective
- Batch processing: great for Haiku
