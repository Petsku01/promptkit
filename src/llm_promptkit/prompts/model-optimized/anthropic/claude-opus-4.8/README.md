---
category: "model-optimized"
title: "Claude Opus 4.8: Guide"
subcategory: "anthropic"
model: "claude-opus-4.8"
source: "promptkit-authored"
---
# Claude Opus 4.8: Guide

## Verified Model Profile

- Exact Claude API ID: `claude-opus-4-8`. The dotted folder name follows this repository's Claude-version convention; it is not the API identifier.
- Status in the vendor reference: active legacy model, released May 28, 2026. Anthropic recommends considering migration to Opus 5.5. This requested collection does not describe 4.8 as the newest Claude.
- Context window: 1M tokens. Maximum output: 128K tokens. The reference separately lists a 300K output beta for the Batch API; that is not the normal output allowance.
- Inputs: text and images. Output: text. Reliable knowledge cutoff: January 2026.
- Vendor-documented strengths include long-horizon agentic work, knowledge work, vision, and memory tasks. The prompting guide describes literal instruction following, effort-sensitive tool usage, and fewer default subagents.

## API Controls and Prompt Pairing

Thinking is off unless explicitly enabled with `thinking: {type: "adaptive"}`. Configure effort separately with `output_config.effort`; documented levels are `low`, `medium`, `high` (default), `xhigh`, and `max`. The model-specific guide recommends starting at `xhigh` for coding and agentic tasks and at least `high` for intelligence-sensitive work. It recommends starting with a 64K maximum output budget for `xhigh` or `max` workloads, then tuning; this is not a requirement to generate long user-facing answers.

The templates explicitly scope requirements across every section, specify when to retrieve evidence, and distinguish discovery from verification in code review. These choices address the documented literalism and tendency to reason instead of calling tools. They also avoid forced progress updates after a fixed number of calls.

For frontend tasks, supply concrete visual tokens rather than relying on the model's documented default house style. Computer/browser tools and subagents require an actual harness; naming them in a prompt does not create them. The vendor documents platform-specific tool versions, so check the model-specific guide before provisioning computer use.

## Prompt Files

- [Analysis](analysis.md): an evidence ledger for long-running research and image comparison.
- [Coding](coding.md): bounded autonomous implementation and coverage-first bug discovery.
- [Reasoning](reasoning.md): durable decision records and literal specification checks.

All fenced prompts are original promptkit/Petsku01-authored templates. Replace bracketed placeholders before use. This folder deliberately contains three prompt files and one README, not extra thinking or long-horizon files.

## Primary Sources

Verified against vendor documentation on 2026-11-01:

- [Claude Opus 4.8 model reference](https://platform.claude.com/docs/en/models/opus-4-8/overview)
- [Model-specific prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-4-8)
- [Effort configuration and per-model recommendations](https://platform.claude.com/docs/en/build-with-claude/effort)

Capability descriptions are vendor claims, not results of a promptkit live inference evaluation.
