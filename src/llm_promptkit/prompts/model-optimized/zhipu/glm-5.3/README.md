# GLM-5.3

Original PromptKit templates for Z.ai/Zhipu's `glm-5.3`, with `source: "promptkit-authored"`. The `zhipu` directory is the vendor namespace used by these templates; the official Hugging Face organization is `zai-org`.

## Verified model characteristics

- Exact official API ID: `glm-5.3`; official HF listing includes `zai-org/GLM-5.3`. The model documentation emphasizes complex software engineering, terminal work, and long-horizon agent tasks. [1][2]
- Text-only input, 1M-token context, maximum output length 128K tokens. Do not transfer GLM-5.3-Flash's visual capability to this model. [1]
- The vendor states GLM-5.3 uses the same base as GLM-5.2, with improvements driven by post-training. Function calling, context caching, streaming, and structured output are documented. [1]

## API and harness settings

- Reasoning is always enabled. `thinking.type` supports only `enabled`; `reasoning_effort` accepts `low`, `high`, `max` (default `max`). The vendor recommends `max` for complex coding. [1]
- An older request using `thinking.type="disabled"` must migrate to `enabled` with effort `low`; disabling reasoning after changing the model ID causes request failure. Prompt wording cannot override this API contract. [1]
- Official examples set `max_tokens=4096` and `temperature=1.0`; these are example request settings, not a universal tuning prescription. Budget output within the documented 128K ceiling and actual account constraints. [1]
- The documentation lists OpenAI Chat Completion, Responses, and Anthropic protocols with distinct endpoints, and notes protocol restrictions for accounts with GLM Coding Plan history. Confirm the endpoint for the actual subscription; do not interchange coding and general API routes blindly. [1]
- Use the returned function-call IDs and complete arguments in the client, execute only permitted functions, and return real tool results. A JSON-only prompt does not itself enable structured-output enforcement: configure the supported API mechanism and validate the final output. [1]

## Template selection

- [Analysis](analysis.md): read-only operational diagnosis and structured completion audits.
- [Coding](coding.md): end-to-end ownership and measured infrastructure optimization.
- [Reasoning](reasoning.md): safe tool sequencing and acceptance-criteria consistency checks.

The prompts exploit documented tool-oriented workflows without claiming that architecture, context length, or vendor benchmark gains guarantee success. They require a tool-capable harness for execution.

## Sources

[1] https://docs.z.ai/guides/llm/glm-5.3

[2] https://huggingface.co/api/models?author=zai-org&search=GLM-5&limit=20
