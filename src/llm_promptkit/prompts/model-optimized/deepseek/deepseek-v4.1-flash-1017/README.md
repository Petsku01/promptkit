# DeepSeek V4.1 Flash 1017

Original `promptkit-authored` templates for the documented October 17 checkpoint. The existing `deepseek-v4-pro` and `deepseek-v4-flash` folders are deliberately unchanged.

## Verified model characteristics

- Exact checkpoint: `deepseek-ai/DeepSeek-V4.1-Flash-1017`; the official hosted API calls this model `deepseek-flash`. The pricing page identifies the serving version as `DeepSeek-V4.1-Flash-1017`. [1][2]
- The model card describes improved reasoning, coding, agentic work, and visual benchmarks, with reduced execution time and output length relative to V4.1-Flash. These are vendor-reported comparisons, not guarantees for these templates. [1]
- Context: 1M tokens. The hosted API lists a maximum output of 384K, JSON output, tool calls, Responses and Anthropic APIs, and vision. FIM completion is non-thinking-only. [2]
- Legacy hosted IDs `deepseek-v4-flash` and `deepseek-v4-flash-vision-exp` remain accepted but route to this newer serving model. Do not confuse an accepted alias with the original retired checkpoint. [2]

## API and harness settings

- OpenAI-format base URL: `https://api.deepseek.com`; model `deepseek-flash`. Thinking defaults enabled with `high` effort; supported effort levels are `low`, `high`, `max`. With the OpenAI SDK, set `extra_body={"thinking":{"type":"enabled"}}` and top-level `reasoning_effort`. [2][3]
- In hosted thinking mode, `temperature`, `presence_penalty`, and `frequency_penalty` have no effect. For Flash, `top_p` is effective only in thinking mode and is clamped to 0.95–1.0; non-thinking mode fixes it at 1.0. [3]
- When requests carry `tools`, fully return every previous assistant `reasoning_content`, including turns without tool calls; omitting it can cause HTTP 400. Without `tools`, previous reasoning is ignored even if returned. Preserve complete tool IDs and results in the harness. [3]
- Self-hosted recommendations differ: the model card lists `temperature=1.0`, `top_p=1.0`, 1M context, and `max_tokens>=256K`. Do not apply self-hosted sampling advice as if hosted thinking mode honored all those parameters. [1][3]
- This release has no Jinja chat template: use the documented reference encoding or `deepseek-recipe` for raw/local prompt formatting. Standard hosted API clients handle the protocol separately. [1]

## Template selection

- [Analysis](analysis.md): mixed visual/text evidence and compact corpus triage.
- [Coding](coding.md): harness-verified fixes and visual-to-service-boundary debugging.
- [Reasoning](reasoning.md): independent verifiers and tool-scope consistency checks.

These prompts require actual tools for execution claims; they do not instantiate search/fetch services or configure thinking mode.

## Sources

[1] https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017/raw/main/README.md

[2] https://api-docs.deepseek.com/quick_start/pricing/

[3] https://api-docs.deepseek.com/guides/thinking_mode/
