# Claude 3.5 Haiku: Simple Tasks

## Classification
```xml
<task>Classify the following text.</task>

<categories>
1. [Category A] — [brief description]
2. [Category B] — [brief description]
3. [Category C] — [brief description]
</categories>

<data>
[paste text]
</data>

<output_format>
Category: [chosen]
Confidence: high/medium/low
</output_format>
```

## Entity Extraction
```xml
<task>Extract entities from this text.</task>

<fields>
- person: full names
- organization: company/org names
- location: places
- date: YYYY-MM-DD format
- amount: number + currency
</fields>

<data>
[paste text]
</data>

<output_format>
JSON with extracted fields. Use null for missing values.
</output_format>
```

## Summarization
```xml
<task>Summarize this text.</task>

<constraints>
- Length: [X sentences / bullet points]
- Include: key findings, main conclusions
- Exclude: minor details, examples
</constraints>

<data>
[paste text]
</data>
```

## Formatting / Transformation
```xml
<task>Convert this data to [target format].</task>

<format>
[show example of desired output]
</format>

<data>
[paste input]
</data>

Rules:
- Preserve all information
- Normalize values: [format]
- Missing data: null
```

## Quick Q&A
```
Answer based on this context:

[paste context]

Question: [question]

Answer only from the provided context.
If not found, say "not found in context."
```

## Sentiment Analysis
```xml
<task>Analyze sentiment.</task>

<data>
[paste text]
</data>

<output_format>
{
  "sentiment": "positive/negative/neutral/mixed",
  "confidence": 0.0-1.0,
  "key_phrases": ["phrase1", "phrase2"]
}
</output_format>
```

## Batch Processing
```
Process each item:

1. [item 1]
2. [item 2]
3. [item 3]

Task: [classify / extract / summarize / translate]

Format per item:
- Index: [number]
- Result: [output]
```

---

**Claude 3.5 Haiku Simple Task Tips:**
- Best value model for classification, extraction, and formatting
- XML tags (`<task>`, `<data>`, `<output_format>`) keep it structured and reliable
- One task per prompt — don't combine multiple operations
- Keep instructions minimal — Haiku follows direct instructions well
- 200K context means you can process long documents, but keep the task simple
- For batch work, list items explicitly rather than describing them abstractly