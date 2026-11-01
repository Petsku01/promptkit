# Qwen3.8-2.4T-A95B

Original PromptKit templates for the exact open-weight Qwen3.8 flagship checkpoint, not an ambiguous `qwen3.8` provider alias. Frontmatter uses the lowercase directory slug required by this repository.

## Verified model characteristics

- Exact checkpoint: `Qwen/Qwen3.8-2.4T-A95B`; 2.4T total / 95B active parameters. The card documents improvements in coding, professional work, research, and long-horizon agent execution. [1]
- Hybrid layout: three Gated DeltaNet blocks followed by one Gated Attention block, repeated across 92 layers, with MoE and multi-step-trained MTP. Neither DeltaNet nor MTP is enabled by natural-language prompting. [1]
- Native context: 262,144 tokens; extensible up to 1,010,000 with supported serving configuration. Do not assume the extended capacity on a default server. [1]
- This checkpoint is text-only and always thinking. The managed Qwen3.8-Max product adds vision and non-thinking support and defaults to 1M context; those product features must not be attributed to these open weights. [1]

## API and harness settings

- `reasoning_effort`: `xhigh` (default), `medium`, or `low`. `preserve_thinking` defaults on. For compatible self-hosted Chat Completions servers, the card places `enable_thinking` and `preserve_thinking` under `extra_body.chat_template_kwargs`; do not disable thinking for this checkpoint. [1]
- Recommended sampling: `temperature=1.0`, `top_p=0.95`, `top_k=20`, `min_p=0.0`, `presence_penalty=0.0`, `repetition_penalty=1.0`. Parameter support varies by framework. [1]
- Qwen Cloud uses direct `extra_body` thinking fields instead of the nested template fields and requires its own managed model ID. Preserve reasoning history as supported by the selected harness; a prompt cannot repair dropped API fields. [1]
- Allocate input and output within the server's actual context limit. MTP serving support and measured latency are deployment properties, not guarantees made by these templates.

## Template selection

- [Analysis](analysis.md): sourced decision matrices and feedback-aware workflow reviews.
- [Coding](coding.md): research implementation and repository-level integration.
- [Reasoning](reasoning.md): countercase testing and dependency-aware recovery.

All prompts are `promptkit-authored`; no performance evaluation of these particular templates is claimed.

## Sources

[1] https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/raw/main/README.md
