# RAG (Retrieval-Augmented Generation) Pattern

## Description

Answer questions by retrieving relevant context from a knowledge base and grounding responses in that evidence.

## When to use

When answering questions that require specific, up-to-date, or domain-specific knowledge not in the model's training data.

## When to avoid

General knowledge questions where the model has sufficient expertise, or when retrieval latency/cost is prohibitive.

## Template

```
Context:
```
[Retrieved documents or knowledge base content]
```

Question: [User's question]

Instructions:
- Answer based strictly on the provided context
- If the context doesn't contain the answer, say "I don't have sufficient information"
- Cite specific sources when making claims
- Be concise but complete
- Do not hallucinate information not in the context
```

## Example

```
Context:
```
Document 1 (Product Manual v2.3):
The Enterprise plan includes unlimited users, SSO integration, and 99.9% SLA uptime guarantee. Price: $49/user/month billed annually.

Document 2 (FAQ - Last updated 2025-03-15):
Q: Can I upgrade from Pro to Enterprise mid-year?
A: Yes, upgrades are prorated based on remaining contract term.
```

Question: What happens if I upgrade from Pro to Enterprise after 6 months?

Instructions:
- Answer based strictly on the provided context
- If the context doesn't contain the answer, say "I don't have sufficient information"
- Cite specific sources when making claims
- Be concise but complete
- Do not hallucinate information not in the context
```

## Variations

- **Multi-hop RAG**: Retrieve, then use findings to retrieve more
- **Hybrid retrieval**: Combine keyword + semantic search
- **Self-ask**: Model asks clarifying questions before retrieval
- **Re-ranking**: Reorder retrieved items by relevance

## Tags

rag, retrieval, knowledge-base, context, grounding
