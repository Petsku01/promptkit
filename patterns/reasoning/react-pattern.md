# ReAct Pattern (Reason + Act)

## Description

Alternate between reasoning about the problem and taking actions (like tool use) to solve complex tasks step by step.

## When to use

Complex multi-step problems where external tools or information are needed (calculations, searches, API calls).

## When to avoid

Simple tasks that can be solved in a single reasoning step.

## Template

```
Solve the following problem by alternating between Thought and Action:

**Problem**: [Describe the problem]

**Available Tools**:
- search: Look up information
- calculator: Perform calculations
- [Other tools]

**Format**:
Thought: [Your reasoning about what to do next]
Action: [Tool name with arguments]
Observation: [Result from the tool]
... (repeat Thought/Action/Observation as needed)
Thought: [Final reasoning]
Answer: [Final answer]

**Begin**:
Thought:
```

## Example

```
Solve the following problem by alternating between Thought and Action:

**Problem**: What is the population of Japan divided by the population of Germany?

**Available Tools**:
- search(query): Look up information about countries
- calculator(expression): Perform mathematical calculations

**Format**:
Thought: [Your reasoning about what to do next]
Action: [Tool name with arguments]
Observation: [Result from the tool]
... (repeat as needed)
Thought: [Final reasoning]
Answer: [Final answer]

**Begin**:
Thought: I need to find the population of Japan first.
Action: search("Japan population 2025")
Observation: Japan population is approximately 123.2 million.

Thought: Now I need Germany's population.
Action: search("Germany population 2025")
Observation: Germany population is approximately 84.5 million.

Thought: Now I can calculate the ratio.
Action: calculator("123.2 / 84.5")
Observation: 1.458

Thought: The population of Japan is about 1.46 times that of Germany.
Answer: Japan's population is approximately 1.46 times (or 46% larger than) Germany's population.
```

## Tags

react, reasoning, tools, agents, multi-step
