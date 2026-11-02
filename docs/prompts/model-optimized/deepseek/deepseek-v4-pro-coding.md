---
category: "model-optimized"
title: "DeepSeek V4 Pro: Coding"
subcategory: "deepseek"
model: "deepseek-v4-pro"
source: "promptkit-authored"
---
[← Back to Model-Optimized Deepseek](../index.md)

# DeepSeek V4 Pro: Coding

## When to Use

Use this template when the hosted model ID is `deepseek-v4-pro` (documented serving version DeepSeek-V4-Pro-0813) and the job is a multi-step repository change, review of a large diff, or a 1M-context codebase question that still needs a patch. Vendor page: 1M context, 384K max output, thinking and non-thinking, JSON, tools, Responses and Anthropic APIs, FIM in non-thinking only, **no vision**, concurrency 500. Thinking defaults on with effort `high`. With `tools` present, every prior `reasoning_content` must be replayed or the API returns 400.

Do not use Flash-class bulk scaffolding here (see [v4-flash coding](../deepseek-v4-flash/coding.md)). Do not paste the retired stub’s LiveCodeBench 93.7, “1/7th of Opus,” or “MIT self-host” lines as if they were current hosted facts. Pro is a paid API SKU; open weights, if any, are a separate distribution.

## The Prompt

```
Implement [feature] in [repository snapshot or tree].

Acceptance: [observable behaviors]
Writable paths: [allowlist]
Public contracts: [APIs to preserve]
Commands: [test / type / lint]
Tools: [functions actually registered, or none]
Thinking: enabled in the request (default high). Replay full
reasoning_content on every subsequent tool turn.

Loop:
1. Inspect the current implementation and failing tests before editing.
2. Plan the minimal patch. Do not rewrite files outside the allowlist.
3. Apply the patch. After each logical step, run the named commands.
4. On failure, classify environment vs patch using the real stderr.
5. If tools are used, return complete tool IDs and results; never drop
   reasoning_content mid-loop.
6. Three similar failures with no new evidence: stop and report the blocker.

Deliver: root cause, files changed, exact commands and outputs, remaining
risk. Do not invent terminal output. Do not deploy. Do not attach screenshots
as if Pro accepted vision — it does not on the documented API.
```

## How It Works

Pro is the higher-priced, lower-concurrency hosted model with the same 1M/384K envelope as Flash but without vision. The prompt is an inspect–patch–run loop because thinking mode plus tools is the documented agent path, and omitting `reasoning_content` is a hard 400. Allowlists counter the stub’s “execute full agentic loops confidently” cost pep-talk, which is not an authorization boundary. FIM stays out of this chat template (beta completions, non-thinking, 4K). Temperature/presence/frequency are ignored in thinking mode per DeepSeek; do not ask the model to “set temperature 0.” The 1M window can hold a medium tree, but sending the whole tree is still a budget choice, not a quality guarantee.

## Variables

- `[feature]`: the change.
- `[repository snapshot or tree]`: what the model can see.
- `[observable behaviors]`: acceptance.
- `[allowlist]`: writable paths.
- `[APIs to preserve]`: compatibility freeze.
- `[test / type / lint]`: real commands.
- `[functions actually registered, or none]`: tool surface.

## Related

Companion: [reasoning](reasoning.md). Flash sibling: `deepseek-v4-flash/coding.md`. Champion: `deepseek-v4.1-flash-1017/coding.md`.

Grounded 2026-11-02 against [pricing](https://api-docs.deepseek.com/quick_start/pricing/) and [thinking mode](https://api-docs.deepseek.com/guides/thinking_mode/).

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | FOLLOWED: structural smoke passed |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED: structural smoke passed |
