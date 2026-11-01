---
category: "model-optimized"
title: "GPT-6.1 Sol: Guide"
subcategory: "openai"
model: "gpt-6.1-sol"
source: "promptkit-authored"
---
# GPT-6.1 Sol: Guide

## Verified Model Profile

- Exact API model ID: `gpt-6.1-sol`. The requested unsuffixed `gpt-6.1` documentation URL returned 404; this folder uses the vendor's documented model ID instead.
- API context window: 1,050,000 tokens, with a maximum input of 922,000 tokens and maximum output of 128,000 tokens. These are distinct limits, not additive allowances for arbitrary requests. The vendor separately documents a default 500K context in Codex and ChatGPT Work.
- Input: text and images. Output: text. Audio and video input are unsupported.
- Intended strengths: complex coding, computer use, and professional work. Supported capabilities include structured outputs, function calling, file search, web search, and prompt caching.
- Tool calling requires the Responses API, even though text-only Chat Completions is supported. Tools must be enabled and executed by the surrounding application; these prompts do not grant tools or permissions.

## API Controls and Prompt Pairing

Set `reasoning.effort` in the request to `low`, `medium` (default), `high`, `xhigh`, or `max`. Neither `none` nor a prose instruction is a documented way to disable reasoning on this model. Start with `medium` and evaluate a higher setting on difficult planning or code tasks; more effort does not guarantee correctness.

Use the Responses API for the coding agent and retrieval-backed analysis prompts. Supply the tool definitions, execution environment, and approval policy separately. Supported tools include code interpreter, hosted shell, apply patch, computer use, MCP, and tool search. Availability and permissions remain application-specific.

For structured applications, configure a supported output schema separately from the natural-language prompt. API inputs above 272K tokens incur the documented long-context surcharge; avoid sending an entire repository when targeted retrieval suffices.

## Prompt Files

- [Analysis](analysis.md): source-linked operational decisions and large-context contradiction audits.
- [Coding](coding.md): executable implementation workflows and Responses API tool-contract migration.
- [Reasoning](reasoning.md): constraint validation and decision-reversal thresholds.

Replace bracketed placeholders and copy the desired fenced prompt. Prompts are original promptkit/Petsku01-authored templates, not vendor prompt excerpts. The collection contains exactly three prompt files plus this guide.

## Primary Sources

Verified against vendor documentation on 2026-11-01:

- [OpenAI model catalog](https://developers.openai.com/api/docs/models.md)
- [GPT-6.1 Sol model reference](https://developers.openai.com/api/docs/models/gpt-6.1-sol.md)

The specifications above describe the documented API model, not an inference benchmark performed by promptkit. No live model-quality evaluation is claimed.
