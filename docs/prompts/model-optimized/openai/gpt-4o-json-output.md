[← Back to OpenAI](./index.md)

# GPT-4o: JSON Output

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

Use with Python SDK for guaranteed schema:

```python
from pydantic import BaseModel

class Analysis(BaseModel):
    summary: str
    sentiment: str
    confidence: float
    keywords: list[str]

response = client.beta.chat.completions.parse(
    model="gpt-4o",
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
