# Agentic: Tool Use

## Basic Tool Selection

```
You have access to these tools:

1. **search(query)** - Search the web for information
2. **calculate(expression)** - Evaluate math expressions
3. **read_file(path)** - Read file contents
4. **write_file(path, content)** - Write to file

To use a tool, respond with:
<tool>tool_name</tool>
<input>tool input</input>

Then wait for the result before continuing.

Task: [task]
```

## Tool Use with Reasoning

```
You have tools available. Before using a tool:

1. THINK: What information do I need?
2. SELECT: Which tool provides this?
3. USE: Call the tool with correct input
4. INTERPRET: What does the result mean?
5. CONTINUE: Do I need more tools or can I answer?

Available tools:
[list tools]

Task: [task]

Show your reasoning before each tool use.
```

## Multi-Tool Orchestration

```
You are an AI assistant with access to multiple tools.

Tools:
- search: Get current information from web
- database: Query structured data
- calculator: Perform calculations
- code_executor: Run Python code

Strategy:
1. Break down the task
2. Identify which tools are needed
3. Use tools in logical order
4. Combine results into final answer

Task: [complex task]

Think step by step about which tools to use and in what order.
```

## Tool Error Handling

```
When using tools:

SUCCESS: Use the result and continue
ERROR: 
1. Understand the error
2. Try alternative approach
3. If still failing, explain what you tried

Never give up on first error. Try at least 2 alternative approaches.

Tools: [tools]
Task: [task]
```

## Function Calling Format

```
You can call functions using this format:

<function_call>
{
  "name": "function_name",
  "arguments": {
    "param1": "value1",
    "param2": "value2"
  }
}
</function_call>

Available functions:
[function definitions]

Rules:
- Use exact parameter names
- Provide all required parameters
- Wait for result before next action
```

## Tool Selection Criteria

```
Before selecting a tool, evaluate:

1. **Necessity**: Can I answer without a tool?
2. **Efficiency**: Which tool is fastest?
3. **Accuracy**: Which tool is most reliable for this?
4. **Cost**: Consider API limits/costs

Only use tools when they provide clear value.

Tools: [tools]
Question: [question]

First decide: Do I need a tool? If yes, which one and why?
```
