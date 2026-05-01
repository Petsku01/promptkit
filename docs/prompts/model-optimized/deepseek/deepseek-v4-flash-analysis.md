[← Back to Model-Optimized Deepseek](../index.md)

# DeepSeek V4 Flash: Analysis

## High-Volume Document Analysis
```
Analyze these documents for: [what you're looking for]

Documents: [paste or list — leverage 1M context]
Focus: [key questions to answer]

For each document:
1. Key findings
2. Relevance to: [topic]
3. Data points worth noting
4. Potential issues or contradictions

Summarize findings across all documents.
Flag anything that needs deeper investigation.
```

## Fast Codebase Q&A
```
Answer questions about this codebase:

Source: [paste relevant files — fits in 1M context]

Questions:
1. [question]
2. [question]
3. [question]

For each answer:
- Cite specific files and line numbers
- Include relevant code snippets
- Note any caveats or edge cases
```

## Data Extraction & Structuring
```
Extract structured data from this content:

Content: [paste unstructured text/data]
Target format: [JSON / CSV / table schema]
Fields to extract: [list fields]

Rules:
- Normalize values to [format]
- Handle missing data as [null/N/A/skip]
- Deduplicate entries
- Validate against schema

Output the structured data.
```

## Batch Text Processing
```
Process each of the following texts:

Texts:
1. [text]
2. [text]
3. [text]

Task: [summarize / translate / classify / extract / rewrite]

Format for each:
- Index number
- Result
- Confidence: high/medium/low

Process all texts consistently.
```

---
**DeepSeek V4 Flash Analysis Tips:**
- Best for high-throughput analysis tasks where speed matters
- 1M context window — can process entire document sets at once
- ~35× cheaper input than Claude Opus — use for volume
- Good for: batch classification, extraction, summarization, Q&A
- Switch to V4 Pro for tasks requiring deeper reasoning
- API: `deepseek-chat` for Flash, use temperature=0 for extraction tasks