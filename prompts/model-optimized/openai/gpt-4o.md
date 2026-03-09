# GPT-4o Prompting Guide

## Model Characteristics
- **Context:** 128K tokens
- **Strengths:** Speed, multimodal (vision + audio), cost-effective
- **Best for:** Real-time apps, vision tasks, high-volume

---

## Prompt 1: Step-by-Step Analysis

GPT-4o may skip steps - be explicit:

```
Analyze this problem completely. Show EVERY step.

Step 1: State what you understand
Step 2: Identify key information  
Step 3: Plan your approach
Step 4: Execute step by step
Step 5: Verify your answer
Step 6: Final conclusion

Do not skip any steps. Show your work.
```

---

## Prompt 2: Code Review

```
Review this code as a senior engineer:

1. **Bugs**: List any bugs or potential issues
2. **Security**: Check for vulnerabilities
3. **Performance**: Identify inefficiencies
4. **Readability**: Suggest improvements
5. **Testing**: What tests are needed?

Be specific. Reference line numbers.

Code:
```

---

## Prompt 3: Structured JSON Output

Use with Structured Outputs API for guaranteed schema:

```
Analyze the following text and extract:

Return JSON matching exactly:
{
  "summary": "2-3 sentence summary",
  "sentiment": "positive|negative|neutral",
  "key_points": ["point1", "point2", "point3"],
  "action_items": ["action1", "action2"],
  "confidence": 0.0-1.0
}

Text to analyze:
```

---

## Prompt 4: Image Analysis (Vision)

```
Analyze this image thoroughly:

1. **Objects**: What objects are present? List them.
2. **Text**: Is there any text? Transcribe it exactly.
3. **People**: Describe any people (count, actions, positions)
4. **Setting**: Where is this? (indoor/outdoor, location type)
5. **Context**: What is happening in this image?
6. **Details**: Note any interesting or unusual details.

Be specific and detailed.
```

---

## Prompt 5: Technical Explanation

```
Explain [TOPIC] for a [AUDIENCE]:

Structure your explanation:
1. **Simple analogy**: Start with an everyday comparison
2. **Core concept**: The fundamental idea in 2-3 sentences
3. **How it works**: Step-by-step breakdown
4. **Example**: Concrete, practical example
5. **Common mistakes**: What people often get wrong
6. **Summary**: Key takeaway in one sentence

Keep language appropriate for the audience level.
```

---

## Prompt 6: Data Extraction

```
Extract structured data from this text:

Required fields:
- Names (all people mentioned)
- Dates (in YYYY-MM-DD format)
- Amounts (with currency)
- Locations (city, country)
- Organizations (companies, institutions)

Return as JSON. Use null for missing fields.

Text:
```

---

## Prompt 7: Comparison Analysis

```
Compare [A] vs [B]:

| Aspect | [A] | [B] | Winner |
|--------|-----|-----|--------|
| [Criterion 1] | | | |
| [Criterion 2] | | | |
| [Criterion 3] | | | |

After the table:
1. Summary of key differences
2. When to choose A
3. When to choose B
4. Overall recommendation
```

---

## Prompt 8: Debug Assistant

```
Help me debug this error:

Error message:
[paste error]

Code:
[paste code]

Your response:
1. **Error explanation**: What does this error mean?
2. **Root cause**: Why is this happening?
3. **Fix**: Exact code change needed
4. **Prevention**: How to avoid this in future
5. **Verification**: How to confirm it's fixed
```

---

## Key Tips

- Faster than GPT-4 but may be less thorough
- Add "show each step" to prevent skipping
- Excellent for multimodal (images)
- Use Structured Outputs API for guaranteed JSON
- Good balance of speed and quality
