[← Back to Advanced Techniques](./index.md)

# ReAct (Reasoning + Acting)

Combines reasoning and action iteratively.

## Basic ReAct

```
Task: [task requiring information gathering]

Thought 1: [what I need to find out first]
Action 1: Search[query]
Observation 1: [results]

Thought 2: [what I learned and what I need next]
Action 2: Search[next query]
Observation 2: [results]

Thought 3: [synthesizing information]
Action 3: Finish[final answer]
```

## ReAct for Research

```
Question: [research question]

Thought: I need to find information about [topic].
Action: Search for "[search terms]"
Observation: [what was found]

Thought: This tells me [insight]. Now I need to verify [aspect].
Action: Search for "[verification query]"
Observation: [what was found]

Thought: I now have enough information to answer.
Action: Synthesize findings
Answer: [comprehensive answer with citations]
```

## ReAct for Problem Solving

```
Problem: [problem]

Thought: Let me break this down. First, I need to [step].
Action: Calculate/Analyze [what]
Result: [result]

Thought: Now I see that [insight]. Next step is [step].
Action: Apply [method/formula]
Result: [result]

Thought: Verifying... [verification reasoning]
Action: Check [verification method]
Result: [confirmation or correction]

Final: [answer]
```

## ReAct with Tools

```
Task: [task]

Available tools:
- Calculator: for math
- Search: for information
- Code: for programming tasks

Thought 1: I should [reasoning]
Tool: [tool name]
Input: [tool input]
Output: [tool output]

Thought 2: Based on that, [reasoning]
Tool: [tool name]
Input: [tool input]
Output: [tool output]

Final Answer: [answer]
```

## ReAct for Coding

```
Task: [coding task]

Thought: First, I need to understand the requirements.
Action: Parse requirements
Observation:
- Input: [expected input]
- Output: [expected output]
- Constraints: [any constraints]

Thought: I'll implement using [approach].
Action: Write code
```python
[code]
```

Thought: Let me test with [test case].
Action: Run test
Observation: [output]

Thought: [Works/Doesn't work]. [Next action if needed]
...

Final: [complete, tested solution]
```
