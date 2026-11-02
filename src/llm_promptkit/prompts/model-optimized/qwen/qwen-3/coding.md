---
category: "model-optimized"
title: "Qwen 3: Coding"
subcategory: "qwen"
model: "qwen-3"
source: "promptkit-authored"
---
# Qwen 3: Coding

## When to Use

Use this template on a Qwen3 instruct/thinking checkpoint (dense 0.6B–32B or MoE 30B-A3B / 235B-A22B, including the later Qwen3-2507 instruct and thinking splits) when the job is to write, repair, or review code. Qwen3’s documented SKU is hybrid thinking: thinking mode for math, logic, and coding; non-thinking mode for fast chat. Thinking is a tokenizer / serving switch (`enable_thinking`, SGLang `--reasoning-parser qwen3`, vLLM reasoning parser), not a fake field you paste into the user message. Soft per-turn control, when thinking is enabled, is `/think` and `/no_think` in the user or system text.

Do not use this file for Qwen3.8 flagship agent loops (see `qwen3.8-2.4t-a95b/coding.md`) or for Qwen3.5 vision-language 4B/9B jobs. Do not paste vendor HumanEval-style tables into the prompt. Context is 32K natively on the small dense cards and 128K on 8B+ / MoE in the April 2025 blog; Qwen3-8B documents 32,768 native and 131,072 with YaRN. Stay inside the server you actually run.

## The Prompt

```
Write or repair [language] code for [purpose].

Interface:
- Inputs: [parameters]
- Outputs: [return or side effects]
- Errors: [what must raise or return]

Constraints:
- Edge cases: [list]
- Style: [project conventions or "standard library only"]
- Editable surface: [snippet or files]
- Runtime: [versions]

Existing code or error (optional):
[paste]

Thinking: set enable_thinking / reasoning-parser in the client for this
Qwen3 checkpoint. You may append /think or /no_think for this turn only
when the server still honors those tags. Do not emit a fake API parameter.

Procedure:
1. Restate the interface and the edges you will handle.
2. If existing code is present, name the defect in one sentence before
   editing. Do not rewrite unrelated functions.
3. Emit one complete, compilable artifact (or a unified diff).
4. Provide tests in [framework]: happy path, edge, error. Mark them as
   suggested unless a harness ran them.
5. If a constraint cannot be met, stop and say which one.

Do not open with praise. Do not invent passing test output. Do not claim
a tool ran unless this environment executed it.
```

## How It Works

The retired stub was four unlabeled skeletons (generate / explain / debug / review) with no stop rule. This rewrite binds those jobs to one interface-plus-honest-verification procedure. Qwen3 will happily emit code-shaped text in non-thinking mode; for non-trivial algorithms keep thinking enabled in the client rather than writing “think step by step” as a substitute for the switch. `/think` and `/no_think` only work when `enable_thinking` is on; the later Instruct-2507 cards do not emit `<think>` blocks and no longer need `enable_thinking=False`. Parse `<think>` with the card’s `</think>` token (151668) if you need the final answer only. Agent/MCP tool use is a Qwen-Agent or function-calling setup, not something this prompt enables by naming MCP. Dense 0.6B/1.7B/4B cards are 32K native; 8B+ and both MoE sizes are 128K in the April 2025 blog—do not paste a 235B-A22B repo into a 4B window. Stop when the interface cannot be met. This is the pre-3.8 coding SKU, not a 3.8 substitute.

## Variables

- `[language]` / `[purpose]`: language and goal.
- `[parameters]` / `[return or side effects]` / `[what must raise or return]`: contract.
- `[list]`: edges the author cares about.
- `[project conventions or "standard library only"]`: style freeze.
- `[snippet or files]`: write scope.
- `[versions]`: interpreter, compiler, or framework freeze.
- `[framework]`: pytest, junit, jest, or none.

## Related

Sibling: [multilingual](multilingual.md). Later Qwen3.5 coding: `../qwen-3.5/coding.md`. Current Qwen champion: `../qwen3.8-2.4t-a95b/coding.md`.

Grounded 2026-11-02 against the [Qwen3 blog](https://qwenlm.github.io/blog/qwen3/), [Qwen3 GitHub README](https://github.com/QwenLM/Qwen3), and [Qwen3-8B model card](https://huggingface.co/Qwen/Qwen3-8B). Capability notes are vendor documentation, not promptkit live scores.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | PARTIAL: thinking-cap truncation |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED: structural smoke passed |
