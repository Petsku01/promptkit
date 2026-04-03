# Tree of Thoughts (ToT)

**Category:** reasoning
**Source:** Research (Yao et al. 2023)

## When to Use

Strategic decision making, architecture design, or multi-path problem solving.

## The Prompt

```
Imagine three different independent experts are answering this question: [Insert question].

All experts will write down 1 step of their thinking, then share it with the group.
Then all experts will go on to the next step, etc.
If any expert realizes they're wrong at any point then they leave.

The question is: [Insert question]
```

## How It Works

It forces the model to explore multiple reasoning paths concurrently, evaluate them against each other, and prune dead ends, simulating a more robust search algorithm than linear CoT.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| GPT-4 | Yes | Excellent |
| Claude | Yes | Excellent |
| Llama 3 | Partial | May need guidance |
