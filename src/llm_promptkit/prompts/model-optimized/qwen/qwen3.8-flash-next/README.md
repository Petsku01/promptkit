# Qwen3.8-Flash-Next

PromptKit-authored English templates for the project's Strata model. “Strata” names the evidence-layering workflow here; it is not a vendor capability or API setting.

## Verified model characteristics

- Exact checkpoint: `Qwen/Qwen3.8-Flash-Next`, an experimental architectural preview for Qwen4 with a vision encoder. The card reports 125B language-model parameters with 6B activated, plus 51B n-gram embedding parameters and 4B MTP parameters. [1]
- Hybrid layout: Gated DeltaNet plus micro-block-level Qwen Sparse Attention, with Gated Residual and n-gram embeddings. MTP has one layer trained with multiple steps. These are architecture/serving properties, not prompt toggles. [1]
- Native context is 262,144 tokens (256K), extensible to 1,000,000 with explicit serving configuration such as supported YaRN scaling. The managed Qwen3.8-Flash product defaults to 1M and has built-in tools; do not conflate it with these weights. [1]
- Text, image, and video examples are documented, alongside agentic coding, office tasks, visual web development, and long-video evaluation. These examples do not guarantee performance on a particular prompt. [1]

## API and harness settings

- Thinking and `preserve_thinking` default on. Supported `reasoning_effort`: `xhigh` (default), `medium`, `low`. Compatible self-hosted APIs use `extra_body.chat_template_kwargs` for `enable_thinking` and `preserve_thinking`; Qwen Cloud uses direct `extra_body` fields with its own managed model ID. [1]
- Thinking sampling: `temperature=1.0`, `top_p=0.95`, `top_k=20`, `min_p=0.0`, `presence_penalty=0.0`, `repetition_penalty=1.0`. [1]
- Non-thinking is supported: set `enable_thinking=False`; recommended sampling changes to `temperature=0.7`, `top_p=0.80`, and `presence_penalty=1.5`, retaining the other listed defaults. Support varies by inference framework. [1]
- Preserve returned reasoning/history in an agent harness when using preserved thinking. Lower effort can increase total task latency if it causes retries; measure end-to-end work rather than assuming faster turns mean faster completion. [1]
- Budget input plus output against the configured context. Enable extended context only when needed: the card warns static YaRN may affect shorter-text performance. [1]

## Template selection

- [Analysis](analysis.md): Strata evidence layering and sampling-aware video audits.
- [Coding](coding.md): tool-round-budgeted patches and working visual application slices.
- [Reasoning](reasoning.md): delta decision ledgers and checked visual constraints.

Prompts do not configure DeltaNet, MTP, frame sampling, or context extension. Configure those in the actual serving engine and verify its supported options.

## Sources

[1] https://huggingface.co/Qwen/Qwen3.8-Flash-Next/raw/main/README.md
