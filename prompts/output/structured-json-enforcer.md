# Structured JSON Output Enforcer

**Use case:** Ensuring machine-parseable JSON output from LLMs

**Pattern:** Structured Output Enforcement

---

## Quick Version (~80 tokens)

```
Output MUST be valid JSON matching this schema. No preamble, no markdown fences, no explanation.

{"field": "type", "score": number}
```

---

## Extended Version (~350 tokens)

```
OUTPUT REQUIREMENTS:

1. FORMAT: Raw JSON only. No markdown code fences (```json). No preamble text.

2. SCHEMA COMPLIANCE: Output MUST match this exact schema:
   {
     "status": "success" | "error",
     "data": {
       "field1": string (required),
       "field2": number (optional),
       "field3": array of strings (max 5 items)
     },
     "metadata": {
       "timestamp": string (ISO 8601),
       "version": "1.0"
     }
   }

3. FIELD RULES:
   - NEVER omit required fields
   - NEVER add fields not in schema
   - Use null for missing optional fields, don't omit them
   - Arrays must not exceed max item count
   - Strings must respect max length constraints

4. VALIDATION: 
   Before outputting, verify JSON is valid (no trailing commas, quotes balanced).

5. ERROR HANDLING:
   If you cannot produce valid output, return:
   {"status": "error", "data": {}, "metadata": {"error": "descriptive message"}}

EXAMPLE VALID OUTPUT:
{"status":"success","data":{"field1":"value","field2":42,"field3":["a","b"]},"metadata":{"timestamp":"2026-01-15T10:30:00Z","version":"1.0"}}
```

---

## Metadata

- **Author:** Based on Paxrel AI Agent Patterns (2026)
- **Tags:** json, output, structured, api
- **Models:** All
- **Version:** 1.0
