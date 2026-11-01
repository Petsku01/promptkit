# Kimi K3

Original English templates authored for PromptKit; `source: "promptkit-authored"` denotes prompt authorship, not vendor authorship. These are workflow suggestions, not benchmarked performance guarantees.

## Verified model characteristics

- Exact checkpoint: `moonshotai/Kimi-K3`; official API ID: `kimi-k3`. The current quickstart calls it the previous-generation flagship, not the newest Kimi model. [1][2]
- Context: 1,048,576 tokens in the model card; native visual understanding and long-horizon coding, terminal orchestration, and knowledge work are documented. [1]
- Architecture: 2.8T total / 104B activated parameters, Kimi Delta Attention plus gated MLA, Attention Residuals, and Stable LatentMoE. Architecture is not a user-facing prompt switch. [1]

## API and harness settings

- Official base URL: `https://api.moonshot.ai/v1`. Thinking is always enabled; top-level `reasoning_effort` accepts `low`, `high`, `max` (default `max`). [2]
- Preserve the complete returned assistant message, including `reasoning_content` and `tool_calls`, unchanged in subsequent turns. This is a client responsibility, not something prose in a prompt enables. [1][2]
- The official quickstart fixes `temperature=1.0`, `top_p=0.95`, `n=1`, and both presence/frequency penalties at zero; omit these fields rather than treating benchmark sampling settings as adjustable API knobs. [2]
- Official vision input uses base64 or `ms://<file-id>`, not public image URLs; message content must be an array. Strict JSON Schema constrains final `content`, not reasoning output. [2]
- Ollama lists `kimi-k3:cloud` with a 1M context; its tag and API contract are separate from Moonshot's. [3]

## Template selection

- [Analysis](analysis.md): corpus reconciliation and visual/report discrepancy auditing.
- [Coding](coding.md): milestone-based migrations and screenshot-driven interface repair.
- [Reasoning](reasoning.md): authoritative constraints and falsifiable tool-grounded research.

Long context does not guarantee complete retrieval. Supply stable evidence IDs, reserve output space, and explicitly report truncated inputs. Tool execution requires an actual tool-enabled harness.

## Sources

[1] https://huggingface.co/moonshotai/Kimi-K3/raw/main/README.md

[2] https://platform.kimi.ai/docs/guide/kimi-k3-quickstart

[3] https://ollama.com/library/kimi-k3
