[← Back to Qwen](./index.md)

# Qwen 2.5: JSON Output

## Basic JSON

```
Extract as JSON:
{
  "field1": "value",
  "field2": "value"
}

Text: [input]
JSON:
```

## Entity Extraction

```
Extract entities as JSON:

{
  "names": [],
  "dates": [],
  "locations": [],
  "organizations": []
}

Text: [input]
JSON:
```

## Structured Analysis

```
Analyze and return JSON:

{
  "summary": "brief summary",
  "sentiment": "positive/negative/neutral",
  "topics": ["topic1", "topic2"],
  "language": "detected language"
}

Text: [input]
```

## List to JSON

```
Convert this list to JSON array:

[input list]

Format:
[
  {"item": "...", "details": "..."},
  ...
]
```

## Form Data

```
Parse this form data:

[paste form text]

Return JSON:
{
  "name": "",
  "email": "",
  "phone": "",
  "message": ""
}
```
