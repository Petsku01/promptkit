---
category: "reasoning"
title: "Self-Discover Select-Adapt-Implement-Solve"
license: "MIT"
---
# Self-Discover Select-Adapt-Implement-Solve

**Category:** reasoning
**Source:** Adapted from https://github.com/FareedKhan-dev/all-agentic-architectures/blob/main/src/agentic_architectures/architectures/self_discover.py (MIT, Fareed Khan). Method origin: Zhou et al., Self-Discover: Large Language Models Self-Compose Reasoning Structures (Google DeepMind, 2024), https://arxiv.org/abs/2402.03620.

Copyright (c) 2025 Fareed Khan. Full permission and warranty notice: [NOTICE.md](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md). This is not an official paper implementation. LangSmith Hub Self-Discover templates are not copied.

## When to Use

Compose a finite reasoning recipe from a module library, specialize it to the task, then execute a typed plan once. Use when solution structure matters more than extra search branches or iterative draft refinement.

## The Prompt

```text
Compose and execute a reasoning structure for [task] using [module library]
under [selection bound]. Stages run once, in order: SELECT, ADAPT, IMPLEMENT,
SOLVE. Do not solve during SELECT, ADAPT, or IMPLEMENT. Show concise stage
artifacts, not private chain-of-thought. Modules do not make an answer correct
by themselves.

Default module library (0-based ids; replace only if [module library] is
supplied in full):
[0] Critical thinking — question assumptions and surface biases
[1] Break the problem into sub-problems and solve each
[2] Identify the type of problem (logic, math, classification, planning, ...)
[3] Identify the goal — what the final answer must contain
[4] List relevant facts, constraints, and unknowns
[5] Consider analogies — what problem is this structurally similar to
[6] Brainstorm alternative interpretations of the question
[7] Step-by-step reasoning from premises to conclusion
[8] Consider counterexamples that would falsify a candidate answer
[9] Make a table, list, or diagram to organize the information
[10] Reverse-engineer from a candidate answer back to the premises
[11] Evaluate trade-offs between competing options explicitly
[12] Devise an algorithm or procedure that always finds the answer
[13] Synthesize multiple perspectives or stakeholder views
[14] Check consistency — does the candidate satisfy EVERY constraint
[15] Self-verify — solve a second way and compare the two answers

Unified selection bound: pick 3 to 6 inclusive unique in-range module ids.
Do not use a looser 2–8 window. Duplicate ids, empty lists, and any id
outside 0..N-1 are invalid. Reject the stage rather than silently dropping
ids into an empty plan.

1. SELECT. Return selected_ids, the corresponding module texts, and a one-
   sentence rationale. Do not solve.

2. ADAPT. Produce exactly one adapted phrasing per selected module, same
   order, replacing generic words with nouns and verbs from [task]. Copy
   each original module text verbatim beside its adaptation. Count(adapt)
   must equal count(selected_ids). Do not solve.

3. IMPLEMENT. Translate adapted modules into a plan of 2 to 8 steps. Each
   step has step_number (1-indexed), description referencing adapted
   module(s), and expected_output type. State final_answer_format. Do not
   solve.

4. SOLVE. Execute the plan. step_outputs must have the same length as
   plan steps, one concise string per step. final_answer must match
   final_answer_format with no preface. If required evidence is missing,
   stop with BLOCKED and keep step_outputs aligned to steps attempted.

Return selected_ids, adaptations, plan, step_outputs, final_answer or
BLOCKED, and which mechanical checks passed (nonempty in-range unique ids,
one adapt per id, step_outputs arity, format). Invalid SELECT does not
continue.
```

## How It Works

The Fareed Khan Self-Discover port runs SELECT → ADAPT → IMPLEMENT → SOLVE as a finite DAG over a 16-module subset of the paper's atomic reasoning modules. This adaptation keeps those contracts, rejects empty or out-of-range selections instead of clamping into an empty plan, requires one adaptation per selected id, and requires step_outputs length to match the plan. The module-count rule is unified at 3–6 unique in-range ids (not a mix of prompt 3–6 and schema 2–8). Hub templates are unused.

Unlike Meta-Prompting, the library is finite and selected by id rather than generating unconstrained new prompts. Unlike [Decomposition (Least-to-Most)](decomposition.md) and prompt chaining, modules are specialized then executed under a typed output contract rather than a fixed stage list. Unlike [Refinement Loop](refinement-loop.md) and [Graph of Thoughts](graph-of-thoughts.md), there is no iterative rescoring or branch-merge search: the recipe is composed once. Unlike [Persistent Skill Evolution Loop](../system/persistent-skill-evolution.md), nothing is promoted into a durable skill store. This is not claimed to be DeepMind's official implementation.

## Variables

- `[task]`: problem statement, required answer format, and available evidence.
- `[module library]`: optional replacement list; default is the 16 modules above.
- `[selection bound]`: inclusive 3–6 unique in-range ids; not overridable to 2–8.

## Tested On

Not model-tested. Curated adaptation of an unofficial implementation of Zhou et al. 2024; no paper-reproduction or accuracy claim is made.
