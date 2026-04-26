[← Back to Model-Optimized Prompts](../index.md)

# Command R: RAG (Retrieval Augmented Generation)

## Basic RAG

```
Answer based on the documents below.

Documents:
[Document 1]
---
[Document 2]
---

Question: [question]

Instructions:
- Answer only from documents
- Cite sources [Doc 1], [Doc 2]
- Say "not found" if not in documents

Answer:
```

## Multi-document QA

```
Use these sources to answer:

Source A: [content]
Source B: [content]
Source C: [content]

Question: [question]

Response format:
- Answer with citations
- Note any contradictions between sources
- Indicate confidence level
```

## Summarize with Sources

```
Summarize the key points from these documents:

[paste documents]

Format:
- Main points (with source citations)
- Common themes
- Contradictions (if any)
```

## Fact Checking

```
Verify this claim using the sources:

Claim: [claim to check]

Sources:
[paste sources]

Analysis:
- Supported: yes/no/partial
- Evidence: [cite specific parts]
- Confidence: high/medium/low
```

## Extract and Cite

```
Extract information about [topic] with citations:

Documents:
[paste documents]

Format each finding as:
"[finding]" - Source: [source name]
```
