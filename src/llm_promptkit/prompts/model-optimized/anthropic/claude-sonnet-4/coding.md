---
category: "model-optimized"
title: "Claude Sonnet 4: Coding"
subcategory: "anthropic"
model: "claude-sonnet-4"
source: "promptkit-authored"
---
# Claude Sonnet 4: Coding

## When to Use

Use this template for residual `claude-sonnet-4-20250514` coding sessions: generate, review, or debug a focused change with XML-separated requirements. On Anthropic-operated platforms that snapshot is retired (deprecated 2026-04-14, retired 2026-06-15); the documented replacement is `claude-sonnet-5-5`. Keep the file as the Sonnet 4 prompting SKU for eval harnesses, partner runtimes that still list the ID, and comparisons against later Sonnet 4.5/4.6/5.x folders. Do not report a live Anthropic API success against the retired ID.

Sonnet 4 was positioned as the speed/intelligence middle of the Claude 4 line. This prompt therefore stays narrower than Opus 4.7 coding: one task, explicit constraints, tests named, no “full autonomy for hours.” Prefer Opus 4.7/4.8 templates for long-horizon agents. XML tags remain Anthropic’s documented way to keep task, code, and review criteria from blending.

## The Prompt

```xml
<task>
Implement or repair [feature] in [language] for [codebase or snippet].
</task>

<requirements>
- Behavior: [observable result]
- Interfaces: [functions, types, HTTP contracts]
- Tests: [framework and cases that must pass]
</requirements>

<constraints>
- Editable surface: [files or snippet only]
- Compatibility: [versions / public API]
- Style: follow existing patterns; no drive-by refactors
- Tools: [shell/patch available or none]
</constraints>

<code_or_tree>
[paste the relevant code, diff, or tree]
</code_or_tree>

<instructions>
1. Restate the behavior and name the files you will touch.
2. If tools exist, inspect before editing. If they do not, produce a complete
   patch and label it unverified.
3. Implement the smallest change that meets every requirement.
4. Add or update tests named in <requirements>. Do not claim a test passed
   unless this environment ran it.
5. For reviews instead of implementations: cite location, expected vs actual,
   severity (blocker / major / minor), and a concrete fix. Skip nits unless
   asked.
6. Stop after the output contract. No preamble, no extra features.
</instructions>

<output>
<summary>[what changed]</summary>
<code>[patch or full files]</code>
<verification>[commands run and real outcomes, or "not run"]</verification>
<risks>[residuals]</risks>
</output>
```

## How It Works

The retired Sonnet 4 stub asked for “code with tests” without a stop rule, so models padded explanations and skipped verification. This rewrite keeps XML regions (Anthropic prompting practice) and adds an inspect → smallest patch → named tests → honest verification trail. The unverified label exists because many Sonnet 4 leftovers are snippet-only chats with no harness. Review mode is the same skeleton with a severity scale so “be concise” does not delete blockers. Nothing here reactivates a retired model ID, sets temperature (removed for current Claude API versions on later models; do not cargo-cult sampling into 4.x prompts either unless the runtime still honors it), or claims Sonnet 4 is cheaper/faster than a live 5.5 SKU as a measured fact—only as the historical product position.

## Variables

- `[feature]`: one coding outcome, not a roadmap.
- `[language]` / `[codebase or snippet]`: runtime and the text the model can actually see.
- `[observable result]`: acceptance in user or API terms.
- `[functions, types, HTTP contracts]`: the freeze-list.
- `[framework and cases that must pass]`: real test names.
- `[files or snippet only]`: write scope.
- `[shell/patch available or none]`: determines whether verification can be claimed.

## Related

Companion in this folder: [reasoning](reasoning.md). Later Sonnet prompting lives under active 4.6/5.x docs; 3.7 coding remains a separate hybrid-thinking SKU.

Grounded 2026-11-02 against [model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations) and [prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices).

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | FOLLOWED: structural smoke passed |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED: structural smoke passed |
