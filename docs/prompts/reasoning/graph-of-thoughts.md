---
category: "reasoning"
title: "Graph of Thoughts (Branch-Explore-Score-Prune-Merge)"
source: "promptkit-authored"
---
[← Back to Reasoning Prompts](../index.md)

# Graph of Thoughts (Branch-Explore-Score-Prune-Merge)

**Category:** reasoning
**Source:** Research (Besta et al. 2023, arXiv:2308.09687); authored.

## When to Use

Explore problems where competing partial solutions can be evaluated and useful parts combined: constrained planning, comparative design, synthesis, or decomposable optimization. Do not use for simple linear tasks, straightforward lookups, or cases without a meaningful scoring rubric; graph overhead can cost more than it contributes.

## The Prompt

```text
Solve [problem] using a bounded graph of candidate artifacts. Use [branch budget]
for breadth and total exploration, and [scoring rubric] for evaluation. A thought
node means an explicit candidate solution, partial plan, or intermediate artifact,
not a request to reveal private reasoning. Show compact candidates, checks, scores,
dependency links, and selection decisions only.

1. Define the objective and decompose the problem into subproblems with observable
   outputs. Record hard constraints, shared assumptions, dependencies, and which
   subproblem results can be combined. Identify at least one direct baseline
   solution. If decomposition adds no useful alternatives or merge opportunities,
   explain that a linear solution is sufficient and return it without constructing
   a decorative graph. Stop as BLOCKED if a missing constraint changes correctness.

2. Fix the exploration budget before branching. If unspecified, allow at most three
   new candidates per frontier node, eighteen total generated nodes, and three
   exploration rounds. Count the baseline, every generated candidate, and every
   merge against the node cap, including rejected artifacts. This adaptation omits
   a separate refinement transformation. Scoring and validation must fit the
   available token/time allowance. When a merge is planned, reserve its node slot
   before branching; also reserve capacity for final validation and response.
   Reduce breadth to fit the remaining budget; never expand exponentially merely
   because branches exist.

3. Freeze the scoring rubric and PASS predicate before any candidate evaluation
   or exploration loop. Use supplied dimensions, scales, weights, ranking rules,
   hard gates, and per-dimension pass thresholds; if critical thresholds are missing,
   stop as BLOCKED rather than inventing them after seeing scores. With no supplied
   rubric, use the default: correctness, constraint coverage, feasibility, and evidence
   support from zero to four each; zero is absent or invalid, one has major defects,
   two has material gaps, three is satisfactory, and four is fully supported.
   Rank default scores by their equally weighted sum. PASS means all hard gates
   pass and all frozen per-dimension thresholds are met; at least three per
   dimension applies ONLY to the default 0–4 rubric. Hard-constraint violations
   make nodes ineligible regardless of total. Mark unknown facts unverified;
   unsupported required claims cannot pass. Never change this contract mid-loop.
   Evaluate the baseline now; if PASS, deliver immediately without branching.

4. Branch from the baseline and selected subproblems into substantively different
   candidate artifacts. Vary an actual strategy, assumption, or decomposition,
   rather than producing paraphrases. Assign stable node identifiers and list each
   node's parent identifiers. An edge records that a candidate used another node
   as input. For each candidate record its proposed result, necessary assumptions,
   cheap falsifying check, and estimated resource requirements. Deduplicate equivalent
   candidates so duplicated wording does not masquerade as independent evidence.

5. Explore and score every generated candidate with the same rubric. Run available
   deterministic checks, consult supplied references, and test boundary constraints
   before relying on self-ratings. Keep a concise scorecard with per-dimension
   scores, hard-gate verdicts, evidence, and uncertainties. A numerical score is a
   selection heuristic, not proof. After each evaluation, apply the frozen PASS
   predicate: PASS means immediate delivery as CONVERGED, with no extra round.
   Never invent observations, evaluator agreement, or experimental results to
   distinguish candidates that lack real evidence.

6. Prune the bottom k% of eligible candidates, using k=50 by default and rounding
   the number removed down so at least one eligible candidate remains. Remove
   ineligible candidates first. Resolve score ties by stronger verified evidence,
   then lower cost, then stable node identifier. Preserve a compact archive of
   pruned node identifiers and rejection reasons. If no eligible survivors remain,
   backtrack to a retained eligible incumbent or generate a justified alternative
   only within remaining node/round limits. Otherwise escalate missing evidence
   as BLOCKED, or report UNSOLVABLE IN BUDGET; never merge invalid answers.

7. Aggregate only when at least two compatible eligible survivors and an unused
   node slot remain. Create a new merge node with multiple incoming dependency
   edges and state each parent's useful contribution. Check shared assumptions,
   interfaces, contradictions, duplicated evidence, and constraint interactions.
   Do not average incompatible answers or erase a minority finding solely because
   several branches share a different assumption. Score the aggregate afresh with
   the frozen rubric and apply PASS immediately; no inherited passing score.
   Backtrack to the retained incumbent if the merge regresses. With one survivor
   or incompatible parents, retain the best eligible artifact and extend it only
   if a justified branch and budget remain. Never invent a second parent. With no
   node slots, stop generation: deliver if PASS, escalate a blocking dependency,
   or report UNSOLVABLE IN BUDGET with the best partial artifact. Disclose any run
   without aggregation as a tree/linear fallback rather than a completed merge.

8. Iterate branch, explore, score, prune, and merge only while an unresolved gap,
   a justified transformation, and sufficient budget remain. PASS always exits
   immediately, even before a round finishes. A completed nonpassing round with
   no substantive improvement stops as STALLED, independently of PASS. Stop on
   exhausted budget, no useful branches, or unavailable required evidence, with
   the applicable budget/blocked status. Never reset round or node counters.

Return the best validated artifact, status, residual uncertainties, and a small
graph ledger showing retained nodes, parent links, scorecards, pruning decisions,
and budget used. Use the same frozen PASS predicate for final labels; a nonpassing
or unvalidated best candidate is provisional, never CONVERGED. Explain the main
trade-off and decisive check; do not dump exhaustive deliberation or claim this
workflow reproduces a published benchmark's performance.
```

## How It Works

[The GoT paper, section 3](https://arxiv.org/html/2308.09687v4#S3), defines thought vertices, dependency edges, generation, aggregation, refinement, scoring, and ranking. Its [arXiv record](https://arxiv.org/abs/2308.09687) records the original 2023 submission and revised 2024 version. This authored adaptation uses generation and multi-parent aggregation, but omits the paper's separate refinement transformation; its budgets, pruning percentage, and conservative validation are authored controls rather than a copied experimental setup.

Unlike chain-of-thought's single linear chain, candidates can branch and later merge. Unlike self-consistency's parallel independent votes, survivor artifacts explicitly share components through multi-parent aggregation. Unlike Tree of Thoughts (ToT), which explores and prunes a tree of alternatives, this Graph of Thoughts (GoT) adaptation combines cross-branch components and backtracks to retained artifacts when merges regress. Unlike an agent graph, these nodes are candidate artifacts, not worker roles. Reflection can support a node's evaluation, ReAct can gather evidence, and prompt chaining can implement transformations, but none alone supplies this selection-and-merge policy. Additional generations and evaluations consume tokens and latency; self-scoring bias and incorrect merges can erase gains.

## Variables

- `[problem]`: objective, constraints, inputs, and evidence available for candidate checking.
- `[branch budget]`: per-node breadth, total node cap, round cap, token/time cap, and optional pruning percentage k.
- `[scoring rubric]`: dimensions, anchored scores, weights, hard gates, and pass thresholds.

## Tested On

Not model-tested. Paper-grounded authored adaptation; no reproduction of the paper's results or universal efficiency claim is made.
