---
category: "model-optimized"
title: "Qwen 3: Multilingual"
subcategory: "qwen"
model: "qwen-3"
source: "promptkit-authored"
---
[← Back to Model-Optimized Qwen](../index.md)

# Qwen 3: Multilingual

## When to Use

Use this template when a Qwen3 checkpoint must translate, follow instructions, or analyze text across languages. The April 2025 Qwen3 blog lists **119 languages and dialects** (Indo-European through Sino-Tibetan, Afro-Asiatic, Austronesian, Dravidian, Turkic, Tai-Kadai, Uralic, Austroasiatic, plus Japanese, Korean, and others). GitHub’s Qwen3 README restates “100+ languages and dialects” with multilingual instruction following and translation as a highlight. This is the catalog slot that Qwen2.5 leftovers and Qwen3.8 champions do not replace.

Name source and target languages explicitly. Do not assume every listed dialect is equally strong; the blog is coverage, not a per-language score. For code comments in another language, still keep the code itself in the project’s language. Skip this file for Qwen3.5’s later 201-language VL cards and for 3.8 long-horizon agents.

## The Prompt

```
Task type: [translate | instruction-follow | analyze | write]
Source language: [language or "detect; then name it"]
Target language: [language for the entire reply]
Register: [formal / informal / technical]
Script preference: [e.g. Simplified Chinese, Traditional Chinese, or n/a]

Source text:
[paste]

Constraints:
- Preserve meaning, numbers, names, and markup.
- Do not silently mix languages in the reply except for proper nouns
  that have no established target form.
- If a span cannot be translated without guessing jargon, keep the
  source span and mark it [untranslated: reason].
- If the source language is not among Qwen3’s documented families or
  you cannot identify it, say so instead of inventing a translation.

Output:
1. Detected source language (one name).
2. The target-language artifact only, in the requested register.
3. A short notes list: untranslated spans, ambiguous idioms, and
   script choices. Empty if none.

Do not add an English preamble unless the target language is English.
Do not romanize unless asked. Stop if the source is empty or not text.
```

## How It Works

The retired stub was four one-liners (translate / write / analyze / comment code) with no stop rule and no script handling. Qwen3’s documented value is breadth plus instruction following, so the prompt forces an explicit language pair, a single-language reply, and an insufficiency path for unidentified or untranslatable spans. “Detect then name” stops the model from answering in English by default. Markup preservation matters because multilingual jobs often wrap HTML or markdown. Script preference is required for Chinese because the blog lists Simplified, Traditional, and Cantonese as separate rows. Thinking mode is optional here; translation is usually `/no_think` or `enable_thinking=False` unless the source is a legal or technical argument that needs reasoning. Code comments in a second language still keep identifiers in the project language so the file compiles. This prompt never claims a BLEU, COMET, or per-dialect score; the 119-language table is coverage, not an eval we ran.

## Stop rules

Stop when the source is empty, the language cannot be named, or a required script choice is missing. Do not fall back to English unless English is the target. Do not claim a dialect is “supported” beyond the blog’s coverage table. Do not mix registers inside one reply. If the user asked for comments in language L on code, keep identifiers and APIs in the codebase language. This file does not enable thinking, MCP, or Qwen-Agent; those are client settings documented on the Qwen3 cards.

## Variables

- `[translate | instruction-follow | analyze | write]`: job type.
- `[language or "detect; then name it"]`: source.
- `[language for the entire reply]`: target.
- `[formal / informal / technical]`: register.
- `[e.g. Simplified Chinese, Traditional Chinese, or n/a]`: script.
- `[paste]`: source text only.

## Related

Sibling: [coding](coding.md). Qwen3.5 JSON/basic: `../qwen-3.5/`. Current Qwen champion: `../qwen3.8-2.4t-a95b/`.

Grounded 2026-11-02 against the [Qwen3 blog](https://qwenlm.github.io/blog/qwen3/) (119-language table) and [Qwen3 GitHub README](https://github.com/QwenLM/Qwen3). Language lists are vendor documentation, not promptkit evals.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
