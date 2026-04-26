[← Back to Output Prompts](../index.md)

# XML Tag Framing

**Category:** output
**Source:** Anthropic best practices

## When to Use

Passing complex, multi-part instructions and context to the LLM cleanly.

## The Prompt

```
You will evaluate a document based on specific rules.

<rules>
1. Rule A...
2. Rule B...
</rules>

<document>
[Insert document text here]
</document>

Based on the <rules>, evaluate the <document>. Provide your final verdict inside <verdict> tags.
```

## How It Works

LLMs are heavily trained on HTML/XML. Using pseudo-XML tags sharply delineates instructions from data, preventing prompt injection and improving instruction following.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| Claude | Yes | Recommended by Anthropic |
| GPT-4 | Yes | Works well |
| Llama 3 | Yes | Good |
