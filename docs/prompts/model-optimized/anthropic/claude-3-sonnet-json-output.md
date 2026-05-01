[← Back to Model-Optimized Anthropic](../index.md)

# Claude Sonnet: JSON Output

## JSON Extraction (XML-wrapped)

```xml
<task>
Extract structured data from this text.
</task>

<schema>
{
  "entities": [{"name": "string", "type": "person|org|location"}],
  "dates": ["YYYY-MM-DD"],
  "amounts": [{"value": number, "currency": "string"}],
  "summary": "string"
}
</schema>

<rules>
- Return ONLY valid JSON
- No markdown code blocks
- Use null for missing fields
- Dates in ISO format
</rules>

<text>
[input text]
</text>
```

## Classification to JSON

```xml
<task>
Classify this text and return structured result.
</task>

<categories>
- category_a: [description]
- category_b: [description]
- category_c: [description]
</categories>

<output_schema>
{
  "category": "string",
  "confidence": 0.0-1.0,
  "reasoning": "brief explanation",
  "keywords": ["relevant", "terms"]
}
</output_schema>

<text>
[input]
</text>
```

## Multi-Document JSON

```xml
<task>
Parse multiple items into JSON array.
</task>

<schema>
[
  {
    "id": number,
    "title": "string",
    "content": "string",
    "metadata": {}
  }
]
</schema>

<documents>
[paste documents separated by ---]
</documents>
```

## Validation + JSON

```xml
<task>
Validate this data and return results as JSON.
</task>

<validation_rules>
- email: valid email format
- phone: valid phone format
- date: not in future
- required: name, email
</validation_rules>

<output_schema>
{
  "valid": boolean,
  "errors": [{"field": "string", "error": "string"}],
  "cleaned_data": {}
}
</output_schema>

<data>
[input data]
</data>
```
