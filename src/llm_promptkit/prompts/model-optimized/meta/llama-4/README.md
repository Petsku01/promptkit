# Llama 4 Prompting Guide

## Model Characteristics
- **Architecture:** MoE (Mixture of Experts)
- **Variants:**
  - **Scout:** 17B active params, 109B total — efficient, single-GPU deployment
  - **Maverick:** 400B total params — flagship quality, best results
- **Context:** Up to 10M tokens
- **Strengths:** Massive context, open-source, strong reasoning, tool use, multimodal
- **Best for:** Long-document analysis, open-source deployments, cost-efficient production

---

## Prompt Files

| Theme | File | Description |
|-------|------|-------------|
| Coding | [coding.md](coding.md) | Code generation, review, debugging |
| Analysis | [analysis.md](analysis.md) | Long-context reasoning, document analysis |
| Long Context | [long-context.md](long-context.md) | Leveraging the 10M token window |

## Prompting Tips

- Llama 4 follows instructions well — be direct and explicit about output format
- MoE architecture activates relevant experts — describe your domain clearly
- For long-context tasks, put the most important instructions at the beginning and end
- Scout is best for fast, cost-efficient work; Maverick for maximum quality
- Tool use is supported — define tools explicitly in the prompt
- Works great self-hosted — ideal for privacy-sensitive or air-gapped deployments