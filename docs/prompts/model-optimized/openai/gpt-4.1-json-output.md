[← Back to Model-Optimized Openai](../index.md)

# GPT-4.1: JSON Output

## Basic JSON Extraction
```
Analyze this text and return JSON:

{
  "summary": "2-3 sentence summary",
  "sentiment": "positive|negative|neutral",
  "key_points": ["point1", "point2", "point3"],
  "confidence": 0.0-1.0
}

Return ONLY valid JSON, no explanation.

Text:
```

## Entity Extraction
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

## Structured Outputs API
```
Use with Python SDK for guaranteed schema:

from pydantic import BaseModel

class Analysis(BaseModel):
    summary: str
    sentiment: str
    confidence: float
    keywords: list[str]

response = client.beta.chat.completions.parse(
    model="gpt-4.1",
    messages=[{"role": "user", "content": prompt}],
    response_format=Analysis
)
```

## Complex Nested JSON
```
Parse this document into JSON:

{
  "document": {
    "title": "string",
    "date": "YYYY-MM-DD",
    "author": "string"
  },
  "sections": [
    {
      "heading": "string",
      "content": "string",
      "subsections": []
    }
  ],
  "metadata": {
    "word_count": number,
    "language": "string"
  }
}

Document:
```

---
**GPT-4.1 JSON Tips:**
- Better schema adherence than GPT-4o for complex outputs
- Use Structured Outputs (Pydantic) for guaranteed type-safe responses
- Specify "Return ONLY valid JSON" to avoid explanatory text
- Handles nested schemas well — provide the full example schema