# JSON Enforcer

**Category:** output

Return ONLY valid JSON. No markdown, no code blocks, no explanation.

Required JSON structure:
{schema}

Validation rules:
- All string values must be properly escaped
- Numbers must not be quoted
- Booleans are true/false, not strings
- null is null, not "null" or undefined
- No trailing commas
- Double quotes only