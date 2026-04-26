[← Back to Agentic](./index.md)

# Agentic: Tool Use

>  **Modern Best Practice**: Use native function calling APIs (OpenAI, Anthropic, etc.)
> instead of text-based tool invocation. These prompts are for models without native tool support.

## Native Function Calling (Recommended)

```python
# OpenAI / Anthropic native approach - NO PROMPT NEEDED
# Define tools in API call, model returns structured JSON

tools = [
    {
        "type": "function",
        "function": {
            "name": "search",
            "description": "Search the web for information",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search query"}
                },
                "required": ["query"]
            }
        }
    }
]

# Model automatically returns: {"name": "search", "arguments": {"query": "..."}}
```

## Text-Based Tool Use (Fallback for older/local models)

```
You have access to these tools:

TOOLS:
- search(query: str) -> Search results
- calculate(expr: str) -> Math result
- read_file(path: str) -> File contents

USAGE FORMAT:
To use a tool, output EXACTLY:
ACTION: tool_name
INPUT: tool_input

Then STOP and wait for OBSERVATION.

EXAMPLE:
User: What's 25 * 4?
ACTION: calculate
INPUT: 25 * 4

OBSERVATION: 100

Now I can answer: 25 * 4 equals 100.

---
Task: [task]
```

## ReAct Pattern (Reasoning + Acting)

```
You solve problems by alternating between thinking and acting.

FORMAT:
THOUGHT: [what you're thinking, what you need]
ACTION: [tool_name]
INPUT: [tool input]
OBSERVATION: [result - will be provided]
... repeat until solved ...
THOUGHT: [final reasoning]
ANSWER: [final answer]

RULES:
- Always THOUGHT before ACTION
- One ACTION at a time
- Wait for OBSERVATION before next step
- When you have enough info, give ANSWER

TOOLS:
[list tools]

TASK: [task]

Begin:
THOUGHT:
```

## Tool Selection Reasoning

```
Before using any tool, answer:

1. DO I NEED A TOOL?
   Can I answer from my knowledge? If yes, just answer.

2. WHICH TOOL?
   | Tool | Use when |
   |------|----------|
   | search | Need current/external info |
   | calculate | Math beyond mental math |
   | code | Need to run/test code |

3. WHAT INPUT?
   Formulate the exact query/input needed.

4. WHAT IF IT FAILS?
   Have a backup plan.

Task: [task]

My reasoning:
1. Do I need a tool? [yes/no because...]
2. Best tool: [tool] because [reason]
3. Input: [exact input]
4. Backup: [alternative approach]

Proceeding with: [action or direct answer]
```

## Multi-Tool Orchestration

```
Complex tasks may need multiple tools in sequence.

TASK: [complex task]

PLAN:
1. First I need [info] -> use [tool]
2. Then I need [info] -> use [tool]
3. Finally, combine results

EXECUTION:
Step 1:
ACTION: [tool]
INPUT: [input]
OBSERVATION: [result]
LEARNED: [what this tells me]

Step 2:
ACTION: [tool]
INPUT: [input based on step 1]
OBSERVATION: [result]
LEARNED: [what this tells me]

SYNTHESIS:
Combining all observations: [final answer]
```

## Error Recovery

```
Tool errors happen. Handle them gracefully.

If tool returns ERROR:
1. UNDERSTAND: What went wrong?
2. DIAGNOSE: Bad input? Tool down? Wrong tool?
3. RETRY: Fix input and try again
4. FALLBACK: Try alternative tool/approach
5. GIVE UP: After 3 attempts, explain what you tried

EXAMPLE:
ACTION: search
INPUT: latest news
OBSERVATION: ERROR - query too vague

RECOVERY:
The search failed because query was too vague.
Retrying with more specific query.

ACTION: search
INPUT: latest technology news March 2024
OBSERVATION: [results]

Success after retry.
```

## Minimal Tool Use

```
Use tools ONLY when necessary. Prefer:
1. Direct answer from knowledge (fastest)
2. Reasoning without tools (no latency)
3. Single tool call (minimal)
4. Multiple tools (only if required)

Before any tool call, ask:
"Can I answer this without a tool?"

If yes -> answer directly
If no -> use minimal tools needed
```
