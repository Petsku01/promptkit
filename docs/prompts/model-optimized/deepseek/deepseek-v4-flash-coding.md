---
category: "model-optimized"
title: "DeepSeek V4 Flash: Coding"
subcategory: "deepseek"
model: "deepseek-v4-flash"
source: "promptkit-authored"
---
[← Back to Model-Optimized Deepseek](../index.md)

# DeepSeek V4 Flash: Coding

## When to Use

Use this template for high-throughput coding on the Flash line: small functions, bulk transforms, test generation, and quick debug. DeepSeek’s current hosted ID is `deepseek-flash`, served by DeepSeek-V4.1-Flash-1017. The legacy names `deepseek-v4-flash` and `deepseek-v4-flash-vision-exp` are still accepted but the original checkpoints are retired; those requests are billed at Flash prices and executed by 1017. Documented hosted traits: 1M context, 384K max output, JSON, tools, Responses and Anthropic APIs, vision on Flash, FIM in **non-thinking mode only**. Thinking is on by default with effort `high`.

Prefer this folder’s living [analysis](analysis.md) for corpus Q&A, V4 Pro for slower/heavier agent loops, and `deepseek-v4.1-flash-1017/coding.md` when you want the champion 1017-specific harness prompts. Do not repeat the retired stub’s “35× cheaper than Opus” or “284B/13B MoE” claims—those are not on the current pricing page.

## The Prompt

```
Generate or repair code for: [description]

Language / style: [language, conventions]
Files to emit: [list of paths and one-line roles]
Thinking: keep the API default unless this is pure FIM/scaffold, in which
case disable thinking in the request (not in this text). FIM is non-thinking
only and capped at 4K tokens on the beta completions URL.

Requirements:
- [requirement]
- [requirement]

Rules:
1. Output each file as a heading plus a complete code block. No tutorial.
2. Handle the named edge cases. Do not add extra files or frameworks.
3. If debugging, state root cause in two sentences, then the minimal diff.
4. If a tool harness is present, run [test command] and paste real output.
   If not, label the code UNVERIFIED.
5. Do not invent benchmark scores or claim the legacy v4-flash weights ran.

Stop when every listed file is complete or a missing requirement is named.
```

## How It Works

Flash is the cheap, concurrent hosted SKU (docs: 2500 concurrency vs Pro 500). The prompt therefore optimizes for complete, minimal files and a two-sentence debug note instead of an Opus-style autonomous protocol. Thinking stays an API flag: for FIM, DeepSeek requires non-thinking and `base_url=https://api.deepseek.com/beta` with `prompt`/`suffix`, which this chat template does not fake. Alias honesty matters: calling `deepseek-v4-flash` today is not a way to pin the old checkpoint. Tool results must be real; the 1M window does not replace a compiler. Vision is available on Flash if you attach an image of the bug, but only if the client sends media—the prompt will not hallucinate pixels.

## Variables

- `[description]`: the coding job.
- `[language, conventions]`: language and style freeze.
- `[list of paths and one-line roles]`: the exact emit list.
- `[requirement]`: behavioral musts.
- `[test command]`: optional harness command.

## Related

Living leftover: [analysis](analysis.md). Heavier coding: [../deepseek-v4-pro/coding.md](../deepseek-v4-pro/coding.md). Champion: `deepseek-v4.1-flash-1017/coding.md`.

Grounded 2026-11-02 against [Models & Pricing](https://api-docs.deepseek.com/quick_start/pricing/), [thinking mode](https://api-docs.deepseek.com/guides/thinking_mode/), and [FIM](https://api-docs.deepseek.com/guides/fim_completion/).

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | PARTIAL: thinking-cap truncation |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED: structural smoke passed |
