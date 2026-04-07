# Retrieval-Augmented Context

**Use case:** Providing relevant documents as context

**Pattern:** RAG-style context injection

---

## Quick Version (~80 tokens)

```
CONTEXT DOCUMENTS:

[Doc 1] Q3 Sales: $2.4M revenue, +15% YoY
[Doc 2] Customer feedback: Churn due to pricing

Use these to answer: Why did churn increase?
```

---

## Extended Version (~350 tokens)

```
RETRIEVAL-AUGMENTED GENERATION PROTOCOL:

You have access to retrieved documents. Use them to ground your response.

CONTEXT DOCUMENTS:

Document [sales-report-q3]:
"Q3 2026 revenue: $2.4M (+15% YoY). Enterprise segment grew 22%, SMB declined 8%. Customer acquisition cost increased to $450 from $320."

Document [customer-survey-october]:
"Top complaints: 1) Pricing too high vs competitors (42%), 2) Missing feature X (31%), 3) Support response time (27%)"

Document [competitor-analysis]:
"Competitor Y launched similar product at 60% of our price in August 2026."

USAGE INSTRUCTIONS:

1. CITE SOURCES: Reference documents by ID when making claims
   ✓ "Churn increased due to pricing (customer-survey-october, competitor-analysis)"
   ✗ "Churn increased due to pricing"

2. SYNTHESIZE: Combine information across documents
   ✓ "Pricing concerns (42% of feedback) combined with competitor Y's 40% price cut in August explains SMB decline"

3. ACKNOWLEDGE LIMITS: If context doesn't answer the question
   ✓ "Context doesn't explain Enterprise segment growth drivers"

4. DON'T HALLUCINATE: Only use facts from provided documents
   ✗ "Q4 projections show recovery" (not in context)

5. PRIORITIZE: Most relevant documents first

RESPONSE FORMAT:

Answer: [Your synthesized answer]

Sources:
- sales-report-q3: [specific claim supported]
- customer-survey-october: [specific claim supported]
- competitor-analysis: [specific claim supported]

[If applicable] Information not found in context: [what's missing]
```

---

## Metadata

- **Author:** Based on RAG best practices (2026)
- **Tags:** rag, context, retrieval, grounding
- **Models:** All
- **Version:** 1.0
