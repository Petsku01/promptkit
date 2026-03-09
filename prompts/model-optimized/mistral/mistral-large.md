# Mistral Large Prompting Guide

## Model Characteristics
- **Context:** 128K tokens
- **Strengths:** Multilingual, reasoning, code, function calling
- **Best for:** Complex tasks, enterprise, European languages

## Chain of Thought

Use clear markdown sections:

```markdown
## Task
Solve the following problem with detailed reasoning.

## Process

### Step 1: Understanding
What is the problem asking?

### Step 2: Analysis
What are the key components?

### Step 3: Solution
Work through each component.

### Step 4: Verification
Check your answer.

### Final Answer
State your conclusion.
```

## JSON Output

```markdown
## Format
Return valid JSON only:
{"key": "value"}

## Rules
- No markdown code blocks
- No explanation
- Valid JSON only
```

## Function Calling

```json
{
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_weather",
        "description": "Get weather for a location",
        "parameters": {...}
      }
    }
  ]
}
```

## Key Tips

- Excellent for European languages
- Strong function calling support
- Use markdown sections for structure
- Worded scales > numeric (use "excellent" not "5")
- Clear, explicit instructions
