---
category: "model-optimized"
title: "DeepSeek V4 Flash: Guide"
subcategory: "deepseek"
model: "deepseek-v4-flash"
source: "promptkit-authored"
---
# DeepSeek V4 Flash: Guide

## Verified Model Profile

- Hosted ID to send: `deepseek-flash` (DeepSeek-V4.1-Flash-1017). Legacy IDs `deepseek-v4-flash` and `deepseek-v4-flash-vision-exp` are still accepted but the original models are retired; traffic is served by 1017 at Flash prices.
- 1M context, 384K max output. JSON, tools, Responses API, Anthropic API, vision. FIM: non-thinking only, beta `https://api.deepseek.com/beta`, 4K max tokens.
- Thinking default on, effort `high`. Concurrency documented at 2500. OpenAI base `https://api.deepseek.com`.

This folder keeps the v4-flash name for catalog continuity. For 1017-specific champion prompts see `deepseek-v4.1-flash-1017/`.

## API Controls

Set `thinking.type` and `reasoning_effort` in the request (`extra_body` on the OpenAI Python SDK). Replay `reasoning_content` whenever `tools` is present. Disable thinking for FIM. Temperature has no effect in thinking mode.

## Prompt Files

- [Analysis](analysis.md): living high-volume corpus and codebase Q&A.
- [Coding](coding.md): fast generate/debug/batch files with alias and FIM honesty.

Two prompt files plus this guide.

## Primary Sources

Verified 2026-11-02:

- [Models & Pricing](https://api-docs.deepseek.com/quick_start/pricing/)
- [Thinking mode](https://api-docs.deepseek.com/guides/thinking_mode/)
- [FIM completion](https://api-docs.deepseek.com/guides/fim_completion/)
