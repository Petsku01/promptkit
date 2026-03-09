# Claude 3/3.5 Sonnet Prompting Guide

## Model Characteristics
- **Context:** 200K tokens
- **Strengths:** Balance of speed, cost, intelligence
- **Best for:** Production workloads, coding, general tasks

---

## Prompt 1: Chain of Thought with XML

```xml
<task>
Solve this problem systematically.
</task>

<process>
1. Understand what is being asked
2. Identify key information
3. Plan your approach
4. Execute step by step
5. Verify your solution
</process>

<output_format>
<thinking>
[Your step-by-step reasoning]
</thinking>

<answer>
[Your final answer]
</answer>
</output_format>
```

---

## Prompt 2: Code Generation

```xml
<task>
Write a Python function: [description]
</task>

<requirements>
- Type hints on all parameters and return value
- Comprehensive docstring with examples
- Handle edge cases (empty input, invalid types)
- Include input validation
- Add inline comments for complex logic
</requirements>

<output_format>
```python
[code here]
```

<usage_example>
[Show how to call the function]
</usage_example>

<edge_cases_handled>
[List what edge cases you covered]
</edge_cases_handled>
</output_format>
```

---

## Prompt 3: Document Analysis

```xml
<task>
Analyze the following document thoroughly.
</task>

<analysis_sections>
1. **Summary**: 3-5 sentence overview
2. **Key Points**: Bullet list of main ideas
3. **Entities**: People, organizations, dates mentioned
4. **Sentiment**: Overall tone and attitude
5. **Action Items**: Any tasks or next steps implied
6. **Questions**: Unclear points that need clarification
</analysis_sections>

<document>
[paste document here]
</document>
```

---

## Prompt 4: JSON Extraction

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

---

## Prompt 5: Code Review

```xml
<role>
You are a senior engineer conducting a thorough code review.
</role>

<review_criteria>
1. **Correctness**: Does it work as intended?
2. **Security**: Any vulnerabilities? (injection, auth, exposure)
3. **Performance**: Inefficiencies or bottlenecks?
4. **Maintainability**: Is it readable and well-structured?
5. **Testing**: What tests are needed?
6. **Edge Cases**: What inputs could break it?
</review_criteria>

<output_format>
For each issue found:
- **Location**: File and line
- **Severity**: Critical / High / Medium / Low
- **Issue**: What's wrong
- **Fix**: How to fix it
</output_format>

<code>
[paste code]
</code>
```

---

## Prompt 6: Writing Assistant

```xml
<task>
Improve this text while maintaining the original meaning.
</task>

<improvements>
- Fix grammar and spelling
- Improve clarity and flow
- Make it more concise
- Strengthen weak phrases
- Maintain original tone
</improvements>

<output_format>
<improved_text>
[Your improved version]
</improved_text>

<changes_made>
- [List of specific changes]
</changes_made>
</output_format>

<original_text>
[paste text]
</original_text>
```

---

## Prompt 7: Decision Analysis

```xml
<task>
Help me decide between these options.
</task>

<options>
1. [Option A]
2. [Option B]
3. [Option C - if applicable]
</options>

<context>
[Relevant background information]
</context>

<analysis_format>
For each option analyze:
- Pros (at least 3)
- Cons (at least 3)
- Risks
- Long-term implications

Then provide:
- Comparison matrix
- Clear recommendation
- Reasoning for recommendation
</analysis_format>
```

---

## Prompt 8: API Documentation

```xml
<task>
Generate API documentation for this endpoint/function.
</task>

<format>
## Endpoint Name

**Method:** GET/POST/etc
**Path:** /api/v1/...

### Description
[What this endpoint does]

### Parameters
| Name | Type | Required | Description |
|------|------|----------|-------------|

### Request Example
```json
{}
```

### Response Example
```json
{}
```

### Error Codes
| Code | Description |
|------|-------------|

### Notes
- [Important information]
</format>

<code>
[paste code/function]
</code>
```

---

## Key Tips

- XML tags improve consistency and parsing
- 3.5 Sonnet significantly better than 3 Sonnet
- Excellent for coding tasks
- Good for high-volume production use
- Best price/performance ratio for most tasks
