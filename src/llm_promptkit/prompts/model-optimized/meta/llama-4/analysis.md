# Llama 4: Analysis

## Long-Document Analysis
```
Analyze this document in detail.

[paste document — leverage up to 10M context]

Provide:
1. Executive summary (3-5 sentences)
2. Key findings (bullet points)
3. Important data points and quotes
4. Implications and recommendations
5. Open questions

Be thorough — identify patterns that might not be obvious from a partial read.
```

## Multi-Document Synthesis
```
I have multiple documents to cross-reference.

Documents:
1. [Document A] — [brief description]
2. [Document B] — [brief description]
3. [Document C] — [brief description]

[Paste all documents — fits in 10M context]

Analyze:
1. Key themes across all documents
2. Areas of agreement
3. Contradictions or inconsistencies
4. Information unique to each document
5. Overall synthesis and conclusions
```

## Codebase Analysis
```
Analyze this codebase.

[Paste full source — leverage 10M context window]

Provide:
1. Architecture overview — how components connect
2. Code quality assessment
3. Dependency analysis — what depends on what
4. Potential bugs or inconsistencies
5. Performance bottlenecks
6. Security concerns
7. Improvement recommendations (prioritized)
```

## Research Reasoning
```
Reason through this question carefully.

Question: [research question]
Context: [relevant background]

Approach:
1. Restate the question precisely
2. Identify what evidence would answer it
3. Evaluate the available information
4. Consider alternative interpretations
5. Draw conclusions with confidence levels
6. Identify what additional information would help

Distinguish between what you know, what you infer, and what you assume.
```

---

**Llama 4 Analysis Tips:**
- 10M token context is the key differentiator — load entire document collections
- For best long-context results, place instructions at both start and end of prompt
- Scout is sufficient for straightforward summarization and extraction
- Maverick is better for complex reasoning across many documents
- Open-source: can be deployed in air-gapped environments for sensitive analysis