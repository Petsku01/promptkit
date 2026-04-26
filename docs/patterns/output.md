# Output Control Patterns

Patterns that control response format and structure.

## JSON Output

Returns structured JSON matching a schema.

```python
from llm_promptkit import PromptBuilder

prompt = (PromptBuilder()
    .pattern("json-output")
    .output_format("json", schema={
        "sentiment": "positive|negative|neutral",
        "confidence": "number"
    })
    .task("Analyze the sentiment of this text")
    .context("I love this product!")
    .build())
```

**When to use:** API responses, structured data extraction.

---

## JSON Enforcer

Strictly enforces valid JSON — no markdown, no explanation.

```python
prompt = (PromptBuilder()
    .pattern("json-enforcer")
    .task("Extract key information")
    .output_format("json", schema={"name": "string", "date": "string"})
    .build())
```

**When to use:** Strict JSON parsing needed, no tolerance for formatting errors.