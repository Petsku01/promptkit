# Strict JSON Enforcer

**Category:** output
**Source:** Best practices

## When to Use

Building LLM pipelines where the output MUST be parsed by an application.

## The Prompt

```
Extract the requested information and format it strictly as a JSON object. 

Use the following schema:
{
  "field1": "string",
  "field2": "number",
  "field3": ["array", "of", "strings"]
}

Do NOT wrap the JSON in markdown formatting (no ```json). 
Do NOT output any conversational text before or after the JSON. 
Output ONLY valid, parsable JSON.

[Insert text to extract from]
```

## How It Works

Explicitly forbidding markdown backticks and conversational filler ("Here is your JSON:") prevents pipeline breaks when parsing the response via `JSON.parse()`.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| GPT-4 | Yes | Use response_format API |
| Claude | Yes | Works well |
| Llama 3 | Partial | May add markdown |
