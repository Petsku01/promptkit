# Mistral Large: Coding

## Code Generation

```
[INST] Write a [language] function that [description].

Requirements:
- Type hints/annotations
- Comprehensive docstring
- Error handling
- Unit test examples

Output only the code with comments. [/INST]
```

## Code Review

```
[INST] Review this code thoroughly:

```[language]
[code]
```

Analyze:
1. Correctness - any bugs?
2. Security - vulnerabilities?
3. Performance - inefficiencies?
4. Maintainability - readable?

For each issue provide:
- Location
- Severity (critical/high/medium/low)
- Fix [/INST]
```

## Debugging

```
[INST] Debug this error:

Error: [error message]
Code:
```[language]
[code]
```

Provide:
1. Error explanation
2. Root cause
3. Fixed code
4. Prevention strategy [/INST]
```

## Function Calling (Native)

```python
# Mistral supports native function calling
from mistralai import Mistral

client = Mistral(api_key="...")

tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get current weather",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string"}
            },
            "required": ["city"]
        }
    }
}]

response = client.chat.complete(
    model="mistral-large-latest",
    messages=[{"role": "user", "content": "Weather in Paris?"}],
    tools=tools
)
```

## Architecture Design

```
[INST] Design a system architecture for:

Requirements:
[list requirements]

Provide:
1. High-level architecture diagram (ASCII)
2. Component descriptions
3. Data flow
4. Technology recommendations
5. Scalability considerations [/INST]
```

## SQL Generation

```
[INST] Generate SQL for:

Task: [description]
Tables:
- [table1]: [columns]
- [table2]: [columns]

Requirements:
- Optimized query
- Handle NULL values
- Add comments [/INST]
```
