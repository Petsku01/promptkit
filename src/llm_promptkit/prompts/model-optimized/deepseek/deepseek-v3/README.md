# DeepSeek V3

## Features

- **Context:** 128K tokens in the official DeepSeek-V3 model card.
- **Architecture:** mixture of experts, 671B total parameters and 37B activated per token.
- **Scope:** original V3 chat/instruct workflows for analysis, coding, and mathematics. Vendor evaluation results are not measurements of these templates.

This is a historical model-specific guide for local weights or a remaining V3 deployment, not the specification of today's hosted DeepSeek service. The current hosted IDs documented in the audit are `deepseek-flash` and `deepseek-v4-pro`; select their corresponding V4-family guides instead when those are the models actually serving the request. A provider alias alone does not establish the underlying checkpoint.

## Prompts by theme

| Theme | File |
|-------|------|
| Analysis | [analysis.md](analysis.md) |
| Coding | [coding.md](coding.md) |
| JSON | [json-output.md](json-output.md) |
| Math | [math.md](math.md) |

Choose the file by the required artifact rather than concatenating all workflows. Supply the relevant source text, interface, constraints, and an explicit stopping condition. The coding template separates generated code from suggested tests; it does not claim to execute them. Mathematical answers should retain assumptions and a checkable result.

V3 is a normal chat model: do not import R1's no-system-prompt guidance or V4's thinking-mode API controls without checking the actual server. Configure context and sampling in the client, budget input plus output within the deployed window, and validate structured data outside the model. These re-authored workflows remain not model-tested; no success rate is claimed.

## Primary Sources

Audit-verified 2026-11-02: [DeepSeek-V3 model card](https://huggingface.co/deepseek-ai/DeepSeek-V3) and [hosted model documentation](https://api-docs.deepseek.com/quick_start/pricing/).
