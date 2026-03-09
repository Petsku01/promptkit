# Claude Sonnet: Koodaus

## Code Generation

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
[How to call the function]
</usage_example>

<edge_cases_handled>
[List edge cases covered]
</edge_cases_handled>
</output_format>
```

## Code Review

```xml
<role>
Senior engineer conducting thorough code review.
</role>

<review_criteria>
1. **Correctness**: Does it work as intended?
2. **Security**: Any vulnerabilities?
3. **Performance**: Inefficiencies or bottlenecks?
4. **Maintainability**: Readable and well-structured?
5. **Testing**: What tests are needed?
6. **Edge Cases**: What inputs could break it?
</review_criteria>

<output_format>
For each issue:
- **Location**: File and line
- **Severity**: Critical / High / Medium / Low
- **Issue**: What's wrong
- **Fix**: How to fix it
</output_format>

<code>
[paste code]
</code>
```

## API Documentation

```xml
<task>
Generate API documentation for this code.
</task>

<format>
## Endpoint Name

**Method:** GET/POST
**Path:** /api/v1/...

### Description
[What it does]

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
</format>

<code>
[paste code]
</code>
```

## Debug Helper

```xml
<task>
Help debug this error.
</task>

<error>
[paste error message]
</error>

<code>
[paste relevant code]
</code>

<response_format>
1. Error explanation
2. Root cause
3. Fix (exact code)
4. Prevention strategy
</response_format>
```
