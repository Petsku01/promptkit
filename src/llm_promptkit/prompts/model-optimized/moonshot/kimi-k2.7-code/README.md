# Kimi K2.7 Code

PromptKit-authored English workflows, not copied vendor prompts or measured performance claims. Prompt frontmatter records `source: "promptkit-authored"`.

## Verified model characteristics

- Official checkpoint: `moonshotai/Kimi-K2.7-Code`. A coding-focused agentic model built on K2.6, with a 256K context and MoonViT visual input. The vendor reports approximately 30% less thinking-token usage than K2.6; this is not a guarantee for these templates. [1]
- Model card: 1T total / 32B active parameters, MoE with MLA. Documented evaluation covers production software engineering across more than ten languages and MCP tool environments. [1]
- Native image and video input are documented, but video chat is experimental and officially API-only in the deployment caveat. Do not assume identical capabilities in third-party deployments. [1]

## API and harness settings

- Thinking and `preserve_thinking` are forced on; Instant mode is unsupported. Preserve returned reasoning fields and tool-call history rather than retaining only final text. Interleaved thinking and multi-step tool calls are documented. [1]
- Recommended sampling: `temperature=1.0`, `top_p=0.95`. The card uses a 262,144-token context in evaluations. These are client-side settings, not prompt instructions. [1]
- The official platform provides OpenAI/Anthropic-compatible APIs. vLLM, SGLang, and KTransformers are listed deployment options; the card specifies `transformers>=4.57.1,<5.0.0`. Verify compatibility for the engine actually used. [1]
- Ollama's exact cloud tag is `kimi-k2.7-code:cloud`, listed with 256K context and text/image input. Provider tags are not interchangeable with checkpoint IDs. [2]

## Template selection

- [Analysis](analysis.md): production incident reconstruction and cross-language change maps.
- [Coding](coding.md): stateful MCP execution and visual regression repair.
- [Reasoning](reasoning.md): behavioral contracts and discriminating engineering experiments.

The prompts favor short state summaries and executable checks to complement the coding-focused, persistent-thinking workflow. They cannot enable tools or preserved thinking in a client that drops those fields.

## Sources

[1] https://huggingface.co/moonshotai/Kimi-K2.7-Code/raw/main/README.md

[2] https://ollama.com/library/kimi-k2.7-code
