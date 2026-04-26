[← Back to Advanced Techniques](./index.md)

# Meta-Prompting

Use LLM to create better prompts.

## Prompt Generator

```
I need a prompt for: [task description]

Create an effective prompt that:
1. Is clear and specific
2. Includes relevant context
3. Specifies output format
4. Handles edge cases
5. Is optimized for [model name]

Generated prompt:
```

## Prompt Improver

```
Improve this prompt:

Original: [paste prompt]

Analysis:
- What's unclear?
- What's missing?
- What could cause misinterpretation?

Improved version:
[improved prompt]

Changes made:
- [change 1 and why]
- [change 2 and why]
```

## Task-to-Prompt Converter

```
Convert this task into an effective prompt:

Task: [natural language task description]

Consider:
- Who is the target user?
- What output format is needed?
- What constraints apply?
- What examples would help?

Prompt:
```

## Prompt Template Creator

```
Create a reusable prompt template for: [use case]

The template should have:
- Clear placeholders: {placeholder_name}
- Instructions that work with various inputs
- Consistent output format

Template:
---
[template here]
---

Example usage:
[filled template example]
```

## Few-Shot Example Generator

```
I need few-shot examples for this task:

Task: [task description]
Input format: [format]
Output format: [format]

Generate 3 high-quality examples:

Example 1:
Input: [diverse example 1]
Output: [correct output 1]

Example 2:
Input: [different case]
Output: [correct output 2]

Example 3:
Input: [edge case]
Output: [correct output 3]
```

## Prompt Debugger

```
This prompt isn't working as expected:

Prompt: [paste prompt]
Expected: [what you wanted]
Actual: [what you got]

Diagnose:
1. Why is the output different from expected?
2. What's ambiguous in the prompt?
3. What assumptions is the model making?

Fixed prompt:
[corrected version]
```

## System Prompt Builder

```
Create a system prompt for an AI assistant that:

Role: [what role should it play]
Personality: [how it should communicate]
Capabilities: [what it can do]
Limitations: [what it should avoid]
Output style: [formatting preferences]

System prompt:
---
[generated system prompt]
---
```

## Prompt A/B Tester

```
Compare these two prompts for [task]:

Prompt A:
[prompt A]

Prompt B:
[prompt B]

Test with input: [test input]

Output A:
[response to A]

Output B:
[response to B]

Analysis:
- Which is more effective?
- Why?
- Hybrid recommendation:
```
