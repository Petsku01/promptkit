# GPT-4 Prompting Guide

## Model Characteristics
- **Context:** 8K (standard) / 32K (gpt-4-32k)
- **Strengths:** Complex reasoning, nuanced instructions, reliability
- **Best for:** Analysis, creative writing, code generation

---

## Prompt 1: Step-by-Step Reasoning

```
Solve this problem step by step:

1. State what you understand
2. Break into smaller parts
3. Solve each part
4. Combine for final answer

Show your work.

Problem:
```

---

## Prompt 2: Code Review

```
Review this code as a senior developer:

Focus on:
- Bugs and logic errors
- Security vulnerabilities
- Performance issues
- Code style and readability
- Missing error handling

For each issue, provide:
- Location (line number)
- Problem description
- Suggested fix

Code:
```

---

## Prompt 3: JSON Structured Output

```
Analyze this text and return JSON:

{
  "summary": "brief summary",
  "sentiment": "positive|negative|neutral",
  "topics": ["topic1", "topic2"],
  "entities": [{"name": "...", "type": "person|org|place"}]
}

Return ONLY valid JSON, no explanation.

Text:
```

---

## Prompt 4: Writing Improvement

```
Improve this text:

Goals:
- Fix grammar and spelling
- Improve clarity
- Make it more concise
- Maintain the original tone

Provide:
1. The improved version
2. List of changes made

Text:
```

---

## Prompt 5: Explanation for Different Audiences

```
Explain [TOPIC] for a [AUDIENCE].

Structure:
1. Simple analogy
2. Core concept (2-3 sentences)
3. How it works
4. Practical example
5. Common misconceptions
6. One-sentence summary

Keep language appropriate for the audience.
```

---

## Prompt 6: Decision Framework

```
Help me decide: [DECISION]

Options:
1. [Option A]
2. [Option B]

For each option analyze:
- Pros (at least 3)
- Cons (at least 3)
- Risks
- Long-term impact

Then:
- Compare in a table
- Give recommendation
- Explain reasoning
```

---

## Prompt 7: System Design

```
Design a system for [DESCRIPTION].

Requirements:
- Expected scale: [users/requests]
- Key constraints: [latency, cost, etc.]

Cover:
1. High-level architecture (describe components)
2. Data model
3. API design
4. Scaling strategy
5. Trade-offs made

Use clear diagrams (described in text).
```

---

## Prompt 8: Debugging Assistant

```
Help debug this issue:

Error:
[paste error message]

Code:
[paste relevant code]

Provide:
1. What the error means
2. Why it's happening
3. How to fix it (exact code)
4. How to prevent it in future
```

---

## Key Tips

- More reliable than turbo for accuracy-critical tasks
- Handles detailed, nuanced instructions well
- Markdown formatting helps organize prompts
- System message for persona, user message for task
- Good at following multi-step instructions
