[← Back to Defensive Prompts](../index.md)

# Hallucination Reducer

**Category:** defensive
**Source:** Best practices

## When to Use

When you need factual accuracy and want to prevent confident nonsense.

## The Prompt

```
Answer the following question. Important rules:

1. If you don't know something, say "I don't know" - never guess
2. If you're uncertain, say "I'm not certain, but..." and explain your confidence level
3. Distinguish clearly between:
   - Facts you're confident about
   - Inferences you're making
   - Things you're uncertain about
4. If the question asks about recent events, remind me your knowledge has a cutoff date
5. Cite sources or explain how you know something when possible

Question: [INSERT QUESTION]
```

## How It Works

LLMs are trained to be helpful, which makes them prone to confident fabrication. This prompt:
- Gives explicit permission to say "I don't know"
- Requires confidence labeling
- Forces source attribution

## Variations

```
# Stricter version
Before answering, rate your confidence (1-10) and explain why.
If confidence < 7, say so explicitly.
```

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| GPT-4 | Yes | Responds well to uncertainty framing |
| Claude | Yes | Naturally good at this |
| Llama 3 | Partial | May still confabulate |
