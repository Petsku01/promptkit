---
category: "model-optimized"
title: "DeepSeek-R1: Coding"
subcategory: "deepseek"
model: "deepseek-r1"
source: "promptkit-authored"
---
# DeepSeek-R1: Coding

## When to Use

Use this template on open-weight DeepSeek-R1 (or an R1 distill) when the job is algorithm design, debugging, or a self-contained coding puzzle that benefits from a long hidden chain of thought. The Hugging Face model card (`deepseek-ai/DeepSeek-R1`) describes a 671B-total / 37B-active MoE with 128K context, MIT-licensed weights, and vendor-reported strength on math, code, and reasoning. Official usage recommendations: temperature 0.5–0.7 (0.6 suggested), **no system prompt**, all instructions in the user message, and do not suppress `<think>` blocks. For math-like coding problems, ask for a boxed or clearly delimited final artifact.

Do not use this file against the current hosted DeepSeek chat IDs (`deepseek-flash`, `deepseek-v4-pro`); those are V4.x thinking-mode APIs with different `reasoning_content` rules. Do not paste a heavy system persona. Do not claim HumanEval or LiveCodeBench numbers as promptkit results—the card’s tables are vendor evaluations.

## The Prompt

Put this entire block in the **user** message. Leave the system prompt empty.

```
Write [language] code for [task].

Hard constraints:
- Time: [complexity or latency bound]
- Space: [bound]
- Interface: [function signature or CLI]
- Forbidden: [libraries or side effects]

Failing evidence (optional):
[error, repro, or test names]

Work inside your thinking block first. Then, after thinking, emit only:
1. A short list of edge cases you will handle.
2. One complete code block that meets the interface.
3. Complexity in big-O for time and space.
4. Three tests: happy path, empty/zero, and a failure case. Do not mark them
   passed unless a harness actually ran them.

If the constraints conflict, stop and name the conflict. Do not ship partial
code that violates a hard constraint. Do not explain the thinking process
again in the visible answer.
```

Prefix the assistant turn with `<think>` if the runtime allows forced prefixes (the card recommends starting outputs with `"<think>\n"` so the model does not skip reasoning).

## How It Works

R1 was trained to emit a reasoning trace before the answer. System prompts and “skip thinking / be brief” instructions are documented failure modes: the card warns that empty `<think></think>` shortcuts hurt quality. Putting every requirement in the user message, demanding a conflict stop, and separating the visible artifact from the think block matches that protocol. Coding is framed as constraints plus a falsifiable interface so the long CoT has something to check against, unlike the retired stub’s “write an algorithm” one-liner. Temperature remains a sampler setting, not a sentence in the prompt. Distill checkpoints (Qwen/Llama based) use this same user-only pattern but their licenses follow the base model, not R1’s MIT card—call that out in the harness, not in the fenced text.

## Variables

- `[language]` / `[task]`: language and the exact problem.
- `[complexity or latency bound]` / `[bound]`: measurable limits.
- `[function signature or CLI]`: the contract.
- `[libraries or side effects]`: hard bans.
- `[error, repro, or test names]`: optional debug evidence.

## Related

Companion: [reasoning](reasoning.md). Hosted V3/V4 coding lives in `deepseek-v3/coding.md`, `deepseek-v4-flash/coding.md`, and `deepseek-v4-pro/coding.md`. Current flash champion: `deepseek-v4.1-flash-1017/coding.md`.

Grounded 2026-11-02 against [DeepSeek-R1 on Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-R1) (usage recommendations in section 6). Vendor eval tables are not copied as our scores.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | FOLLOWED: structural smoke passed |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED: structural smoke passed |
