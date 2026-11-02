---
category: "model-optimized"
title: "Qwen 3.5: Coding"
subcategory: "qwen"
model: "qwen-3.5"
source: "promptkit-authored"
---
# Qwen 3.5: Coding

## When to Use

Use this template on `Qwen/Qwen3.5-4B` or `Qwen/Qwen3.5-9B` (and same-family serving IDs) for a single function, fix, or review. These are native multimodal cards with a vision encoder; a screenshot of a UI failure is valid input, a caption of a missing screenshot is not. Thinking is on by default. The model card’s **precise coding** sampling is temperature **0.6**, top_p **0.95**, top_k **20**, presence_penalty **0.0**—set that in the client, not in the user text. Tool-calling parsers on the card are `qwen3` reasoning + `qwen3_coder` tool-call; they do nothing unless the server launched them.

This is not Qwen3-Coder 2.5, not Qwen3 dense 32B, and not Qwen3.8-2.4T. Keep the change local. Prefer [json-output](json-output.md) when the deliverable is structured data, [basic](basic.md) when there is no code.

## The Prompt

```
Write or repair [language] code for [purpose].

Interface:
- Inputs: [parameters]
- Outputs: [return or side effects]
- Errors: [what must raise or return]

Constraints:
- Edge cases: [list]
- Style: [conventions]
- Editable surface: [snippet or files]
- Screenshot of the failure: [attached | none]

Existing code or error (optional):
[paste]

Client settings (do not echo): thinking on for non-trivial code; for
precise coding use the card’s temperature 0.6 / top_p 0.95 / top_k 20.
Tool calling only if this server started with a qwen3_coder parser.

Procedure:
1. Restate the interface. If a screenshot is attached, map the visible
   failure to a code path before editing. If it is missing, do not
   invent UI copy.
2. If existing code is present, name the defect in one sentence.
3. Emit one complete, compilable artifact or a unified diff. Match
   surrounding style. No new dependencies unless named.
4. Tests in [framework]: happy, edge, error. Mark suggested unless a
   harness ran them.
5. If the interface cannot be met on this 4B/9B SKU without a larger
   model, say so and stop. No pseudo-code disguised as a solution.

Do not invent passing test output. Do not claim MTP or YaRN ran.
```

## How It Works

The retired “simplified coding” stub assumed a sub-8B toy model and capped output at 20 lines. Official Qwen3.5-4B/9B cards are hybrid Gated-DeltaNet + sparse-MoE vision-language models with 262K native context; the limit that matters is *task size*, not a fake 20-line rule. The card still warns that thinking quality wants at least 128K of usable context if you hit OOM, shrink the window carefully. Thinking traces should stay out of multi-turn history (card best practice 4). Recommended max output for ordinary queries is 32,768 tokens; contest-style problems on the card go up to 81,920—those are server `max_tokens`, not prompt magic. MTP is a serving flag (`speculative-algo` / `qwen3_next_mtp`), not a prompt. Vision helps when the bug is on screen; it does not replace a compiler. `--language-model-only` in vLLM skips the vision encoder when you have no images. Stop when the SKU is the wrong size for the job rather than emitting a tutorial. Champion coding lives under Qwen3.8.

## Stop rules

Stop when the interface cannot compile on the stated runtime, when a required screenshot is missing, or when the change needs a larger Qwen3.8-class agent loop. Do not emit a 20-line cap; that was the retired stub, not the 4B/9B card. Do not enable YaRN from prose. Do not leave `<think>` in a patch you intend to apply. Precise-coding sampling (temperature 0.6) is a client setting. Tool parsers (`qwen3_coder`) stay off unless the server started with them.

## Variables

- `[language]` / `[purpose]`: language and goal.
- `[parameters]` / `[return or side effects]` / `[what must raise or return]`: contract.
- `[list]`: edges.
- `[conventions]`: style freeze.
- `[snippet or files]`: write scope.
- `[attached | none]`: media honesty.
- `[framework]`: test runner or none.

## Related

[basic](basic.md), [json-output](json-output.md). Qwen3 coding: `../qwen-3/coding.md`. Champion: `../qwen3.8-2.4t-a95b/coding.md`.

Grounded 2026-11-02 against [Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B) (coding sampling, thinking default, vision encoder, tool-call parser names). Benchmark figures on that card are not copied as promptkit scores.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | PARTIAL: thinking-cap truncation |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED: structural smoke passed |
