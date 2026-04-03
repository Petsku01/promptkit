# Benchmark: Instruction Following

## Model Comparison (Instruction Following)

> Sources: IFEval, MT-Bench, AlpacaEval 2.0 (as of early 2026)

| Model | IFEval (strict) | MT-Bench | AlpacaEval 2.0 |
|-------|-----------------|----------|----------------|
| **GPT-4o** | 86.5% | 9.2 | 46.1% |
| **Claude 3.5 Sonnet** | 88.0% | 9.1 | 52.4% |
| **Claude 3 Opus** | 83.2% | 8.9 | 40.5% |
| **Gemini 1.5 Pro** | 81.3% | 8.7 | 38.2% |
| **Mistral Large** | 78.5% | 8.5 | 32.1% |
| **Llama 3.1 70B** | 77.2% | 8.3 | 34.5% |
| **GPT-3.5 Turbo** | 69.1% | 7.9 | 22.3% |

## What Makes Instructions "Followable"?

### Format Compliance Test

```
Task: "Respond in exactly 3 bullet points"

| Instruction Type | Compliance Rate |
|------------------|-----------------|
| Just "3 bullet points" | 71% |
| "Exactly 3 bullet points, no more, no less" | 89% |
| "Format: • Point 1 • Point 2 • Point 3" | 96% |
| With example output | 98% |
```

### Best Practices for Instruction Following

**Be explicit about format:**
```
Format your response EXACTLY as:
## Title
[2-3 sentences]

### Key Points
• [point 1]
• [point 2]
• [point 3]

Do not add any additional sections.
```

**Use constraints clearly:**
```
Constraints:
- Maximum 100 words
- No bullet points
- No questions back to user
- End with a single recommendation
```

**Show don't tell:**
```
Example of correct format:
---
Name: John
Age: 25
Status: Active
---

Now do the same for: [input]
```

## Common Failure Modes

| Issue | Cause | Fix |
|-------|-------|-----|
| Too verbose | Model defaults to helpful elaboration | "Be concise. Maximum X words." |
| Wrong format | Ambiguous instructions | Show example output |
| Extra content | Model adds "helpful" extras | "Output ONLY X, nothing else" |
| Ignores constraints | Constraint buried in text | Put constraints first or in caps |

## Prompt Patterns That Work

### Numbered constraints (high compliance)
```
Follow these rules:
1. Respond in JSON only
2. Maximum 5 fields
3. No nested objects
4. Use snake_case keys
```

### Explicit boundaries
```
START OUTPUT
[your structured response here]
END OUTPUT

Include nothing outside these markers.
```

### Role + constraints
```
You are a concise assistant. 
You ONLY output the requested format.
You NEVER add explanations unless asked.
You NEVER ask clarifying questions.

User request: [request]
```

## Key Findings

1. **Explicit beats implicit**
   - "Be brief" -> inconsistent
   - "Maximum 50 words" -> consistent

2. **Examples are the strongest signal**
   - 20-30% improvement with good examples

3. **Position matters**
   - Constraints at START or END of prompt work best
   - Middle of prompt = often ignored

4. **Repetition helps**
   - State constraint, give example, restate constraint
