# Structured Output Enforcement Pattern

## Description

Enforce exact output format with schema validation — no deviations allowed.

## When to use

When output is consumed programmatically (APIs, databases, downstream pipelines).

## When to avoid

Creative writing or exploratory tasks where rigid structure hinders quality.

## Template

```
Output MUST be valid [FORMAT] matching this exact schema.
No preamble, no explanation, no markdown fences.

Schema:
{
  "field1": type (constraints),
  "field2": type (constraints),
  ...
}

Validation rules:
- Never omit required fields
- Never add fields not in schema
- Use null for missing data, never omit
```

## Example

```
Output MUST be valid JSON matching this exact schema.
No preamble, no explanation, no markdown fences.

Schema:
{
  "title": string (max 80 chars),
  "summary": string (max 200 chars),
  "relevance_score": integer (1-10),
  "tags": array of strings (max 3 items),
  "source_url": string (valid URL),
  "publish": boolean
}

Validation rules:
- Never omit required fields
- Never add fields not in schema
- Use null for missing data, never omit
```

## Tags

output, schema, json, structured, validation
