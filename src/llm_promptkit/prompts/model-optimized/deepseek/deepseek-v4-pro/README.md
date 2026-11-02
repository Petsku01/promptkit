---
category: "model-optimized"
title: "DeepSeek V4 Pro: Guide"
subcategory: "deepseek"
model: "deepseek-v4-pro"
source: "promptkit-authored"
---
# DeepSeek V4 Pro: Guide

## Verified Model Profile

- Hosted ID: `deepseek-v4-pro`. Serving version on the pricing page: DeepSeek-V4-Pro-0813.
- 1M context, 384K max output. Thinking and non-thinking. JSON, tools, Responses API, Anthropic API. FIM non-thinking only. **Vision not supported.** Concurrency 500.
- Thinking default on, effort `high`. In thinking mode, temperature/presence/frequency are ignored; `top_p` is ignored (0.95 with tools, else 1.0).

## API Controls

Enable thinking in the request. If the client sends `tools`, replay every prior `reasoning_content` (including non-tool turns) or the API returns 400. Do not put effort strings in the user prompt. Do not send images.

## Prompt Files

- [Coding](coding.md): allowlisted, tool-replay-safe repository loops.
- [Reasoning](reasoning.md): long-context decisions with visible checks (hidden CoT is not replayed without tools).

Two prompt files plus this guide. Original promptkit/Petsku01 templates. Not a substitute for R1 open-weight protocol. Use Flash when you need vision or higher concurrency; use Pro when the job is a long thinking loop or a 1M-context patch without images.

## Primary Sources

Verified 2026-11-02:

- [Models & Pricing](https://api-docs.deepseek.com/quick_start/pricing/)
- [Thinking mode](https://api-docs.deepseek.com/guides/thinking_mode/)
- [Your first API call](https://api-docs.deepseek.com/)
