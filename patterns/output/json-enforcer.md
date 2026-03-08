# JSON Enforcer

## When to Use

- Integrating LLM output into code pipelines
- When you need parseable, valid JSON
- Extracting structured data from unstructured text
- API responses that must be machine-readable

## How It Works

LLMs naturally want to be conversational and add explanations. This pattern suppresses that tendency by:

1. **Explicit instruction** to output ONLY JSON
2. **Schema definition** so the model knows the exact structure
3. **No-prose directive** to prevent wrapping text

Many models (GPT-4, Claude) also support native JSON mode via API parameters.

## The Prompt

```
Extract the following information and return ONLY valid JSON matching this schema:

{
  "field1": "string - description",
  "field2": "number - description", 
  "field3": ["array", "of", "strings"]
}

Input text:
[TEXT_TO_PARSE]

Return ONLY the JSON object. No explanation, no markdown, no code blocks.
```

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `[TEXT_TO_PARSE]` | The unstructured input | `John Smith, 35 years old, lives in NYC` |

## Example

**Input:**
```
Extract the following information and return ONLY valid JSON:

{
  "name": "string - full name",
  "age": "number - age in years",
  "city": "string - city of residence"
}

Input text:
"My name is Sarah Johnson. I'm 28 and I've been living in San Francisco for 3 years now."

Return ONLY the JSON object. No explanation.
```

**Output:**
```json
{"name": "Sarah Johnson", "age": 28, "city": "San Francisco"}
```

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| GPT-4 | Yes | Use `response_format: { type: "json_object" }` in API |
| Claude 3.5 | Yes | Works well with explicit instruction |
| Llama 3 70B | Partial | Sometimes adds markdown code blocks |
| Gemini Pro | Yes | Good compliance |

## Variations

- **TypeScript Schema:** Define interface instead of JSON example
- **JSON5:** Allow comments and trailing commas for complex schemas
- **Nested Objects:** Show full nested structure in schema

## Common Mistakes

- No: Forgetting "no markdown" — models love to wrap in ```json blocks
- No: Vague field descriptions — be explicit about format (ISO date, etc.)
- No: No error handling — add "If field not found, use null"

## Pro Tips

```
# For APIs that support it:
response_format={"type": "json_object"}  # OpenAI
# or
output_format="json"  # Anthropic
```

## Related Patterns

- [Schema Extraction](./schema-extraction.md) — Generate schema from examples
- [Structured Lists](./structured-lists.md) — When arrays are the main output

---

*Last tested: 2026-03-08*
