# JSON Output — Anthropic (Claude)

## Optimizations

- **XML wrapper** — Use tags to delimit JSON clearly
- **Schema in tags** — Wrap schema definition in XML
- **Explicit constraints** — Claude follows formatting rules precisely

## The Prompt

```xml
<instructions>
Return your response as valid JSON only.
No explanation, no markdown code blocks, just raw JSON.
</instructions>

<schema>
{
  "field_name": "type (string|number|boolean|array|object)",
  "another_field": "description of expected value"
}
</schema>

<constraints>
- Output ONLY the JSON object
- Ensure all required fields are present
- Use null for missing optional values
- No trailing commas
</constraints>
```

## With Example

```xml
<example>
Input: "Review of iPhone: Great phone, fast, expensive"
Output: {"sentiment": "mixed", "pros": ["fast"], "cons": ["expensive"], "rating": 4}
</example>

<task>
Analyze the following and return JSON matching the schema above:
</task>
```

## Notes

- Claude 3+ has excellent JSON compliance
- Use `<json>` wrapper tags if model adds explanation
- For arrays: specify "return an array of objects matching..."
