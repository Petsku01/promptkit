# Self-Consistency

**Category:** reasoning
**Source:** Research (Wang et al. 2022)

## When to Use

When you need high confidence in an answer, especially for math, logic, or factual questions.

## The Prompt

```
Solve this problem using three different approaches. Show your work for each approach, then compare the answers.

Problem: [INSERT PROBLEM]

Approach 1: [solve]
Approach 2: [solve using different method]
Approach 3: [solve using another method]

Compare: Which answers agree? What is the most likely correct answer?

Final Answer: [the answer that appears most consistently]
```

## How It Works

By solving the same problem multiple ways, errors in one approach get caught by the others. The answer that appears most frequently across approaches is most likely correct. This mimics ensemble methods in ML.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| GPT-4 | Yes | Excellent for math |
| Claude | Yes | Very thorough |
| Llama 3 | Yes | Good |
