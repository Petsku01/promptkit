# Tool Use Pattern

## Description

Explicitly specify when and how to use external tools to extend the model's capabilities.

## When to use

When the model needs capabilities it doesn't have natively (real-time data, calculations, external APIs).

## When to avoid

Tasks within the model's core capabilities (text generation, analysis, reasoning).

## Template

```
You have access to the following tools:

[TOOL_NAME_1]: [Description of what it does]
- Parameters: [Required and optional parameters]

[TOOL_NAME_2]: [Description]
- Parameters: [...]

**Tool Use Rules**:
1. Only use tools when necessary
2. Always confirm the result before proceeding
3. If a tool fails, try an alternative or explain the limitation
4. Format tool calls exactly as specified

**Task**: [The task to accomplish]

Decide which tools to use and in what order. Show your reasoning.
```

## Example

```
You have access to the following tools:

get_weather: Get current weather for a location
- Parameters: location (required), units (optional: "celsius" or "fahrenheit")

calculate: Perform mathematical calculations
- Parameters: expression (required)

search: Search for information
- Parameters: query (required), num_results (optional, default: 5)

**Tool Use Rules**:
1. Only use tools when necessary
2. Always confirm the result before proceeding
3. If a tool fails, try an alternative or explain the limitation
4. Format tool calls exactly as specified

**Task**: Plan a weekend trip to Paris. I need to know the weather forecast and calculate total budget if I spend €150/day for 2 days plus €300 for flights.

Decide which tools to use and in what order. Show your reasoning.
```

## Tags

tools, external, api, capabilities, extension
