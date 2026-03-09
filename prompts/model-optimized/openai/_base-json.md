# JSON Output — OpenAI (GPT-4)

## Optimizations

- **response_format** — Use API's JSON mode when available
- **Concise schema** — GPT prefers compact schema definitions
- **Strict instruction** — "Return ONLY JSON" works well

## The Prompt

```
Return a JSON object with this structure:
{
  "field": "type"
}

Return ONLY the JSON. No explanation, no code blocks.
```

## With API JSON Mode

```python
response = client.chat.completions.create(
    model="gpt-4-turbo",
    response_format={"type": "json_object"},
    messages=[{"role": "user", "content": prompt}]
)
```

When using JSON mode, include "JSON" in your prompt:

```
Analyze this text and return JSON with sentiment and keywords.
```

## Structured Outputs (GPT-4o+)

For guaranteed schema compliance:

```python
from pydantic import BaseModel

class Analysis(BaseModel):
    sentiment: str
    confidence: float
    keywords: list[str]

response = client.beta.chat.completions.parse(
    model="gpt-4o",
    messages=[...],
    response_format=Analysis
)
```

## Notes

- Always mention "JSON" in prompt when using JSON mode
- GPT-4o supports strict structured outputs via API
- For complex nested schemas, provide an example
