---
category: "system"
title: "Agent Graph With Cycles (Node-Edge Orchestration)"
source: "promptkit-authored"
---
[← Back to System Prompts](../index.md)

# Agent Graph With Cycles (Node-Edge Orchestration)

**Category:** system
**Source:** Grounded in LangGraph docs; authored.

## When to Use

Orchestrate a stateful worker/reviewer workflow that must revisit earlier work under explicit routing and termination rules. Use when role separation, durable state, and escalation justify the coordination cost; prefer a single bounded refinement loop for a small one-agent task.

## The Prompt

```text
Orchestrate [nodes] as a directed agent graph with cycles. Use [state schema]
as the explicit state-passing contract and [max cycles] as a hard business-cycle
limit. Nodes are execution roles or deterministic functions, not candidate thoughts.
Do not claim actual agents or runtime execution exist unless supplied tools run
them. Without an executor, return a clearly labeled orchestration specification
and identify which transitions have not been exercised.

1. Validate the graph contract before running. For each node provide its identifier,
   role, allowed tools, required input fields, output fields, validation rules,
   timeout, and side-effect permissions. Require distinct worker and reviewer nodes
   plus a controller and a dead-letter/escalation destination. The worker proposes
   an artifact and supporting evidence; the reviewer evaluates that exact artifact
   version against fixed acceptance checks; the controller applies routing rules.
   Missing critical schema fields or approval boundaries block execution.

2. Define typed shared state explicitly. Include run identifier, artifact version,
   current artifact, acceptance criteria, unresolved defects, measured gap, cycle
   count, remaining budget, evidence references, reviewer verdict, status, and error
   history. Mark each field's owner and update policy: immutable, replace, append,
   or deterministic merge. Accumulate evidence, completed transition records, cost,
   and historical defects with stable identifiers. Replace current artifact and
   active defect list per cycle. Reset reviewer verdict and transient tool errors
   for every new artifact version; never erase their historical records.

3. State how partial updates combine. Do not assume an empty list clears an
   accumulating field; use an explicit replacement/reset operation in the executor.
   Validate updates before publishing the next state snapshot. Give parallel writers
   disjoint keys or a deterministic conflict policy, and let downstream nodes consume
   the completed snapshot rather than partially written sibling results. Keep secrets
   out of shared logs and user-visible traces. Record idempotency keys for side
   effects so replay or retry cannot duplicate external actions.

4. Specify a routing table with exclusive guards and controller-owned dispatch:
   - START -> controller: validate initial state and admission gates.
   - controller -> worker: dispatch only if the termination gate permits a round.
   - worker -> reviewer: review that returned version only if the gate permits it.
   - reviewer -> controller: every verdict returns here for binding and routing.
   - controller -> success/END: validated current-version approval meets all gates.
   - controller -> worker: revision is justified and continuation gates all pass.
   - any executable node -> dead-letter: failure preempts every normal edge;
     never send to failure and success/revision simultaneously.
   The CYCLIC path is worker -> reviewer -> controller -> worker, never a direct
   reviewer-to-worker handoff. Only the controller increments cycle count, exactly
   once before dispatching each worker/reviewer round, including rejected work.
   Nodes and executor retries cannot reset it. Do not start a round above the cap.

5. Enforce reviewer veto and no self-approval. Only the reviewer may publish an
   approval verdict for the current artifact version, citing acceptance evidence.
   The worker cannot set approval, remove a veto, modify acceptance criteria, or
   route directly to success. Any critical unresolved defect is a veto regardless
   of a favorable average score. Changed artifacts invalidate old verdicts. Distinct
   role names alone do not establish independent evaluation: use a separate reviewer
   invocation or human when supported, and disclose when only role simulation is
   available. The controller checks both verdict identity and version binding.

6. Freeze the gap metric and its evidence source before the first round. Default:
   gap equals the count of failed mandatory acceptance checks in the reviewer's
   current-version check ledger, with a tool-result or reference for each verdict;
   missing evidence counts as a failed check. Freeze check identifiers and any
   explicit critical-defect weights. The first validated review establishes baseline
   gap; only subsequent current-version reviewed revisions must strictly reduce it
   without adding critical defects. Record previous/current gap per completed cycle.
   Never compare stale review state after a worker update. Do not substitute word
   count, activity, or changed explanations for acceptance progress. Preserve the
   best reviewed artifact separately from rejected revisions.

7. Run the termination gate after every node and before each dispatch; it ALWAYS
   overrides cycle continuation. Use three rounds if max cycles is unspecified.
   Evaluate applicable rules in this order:
   a. Schema, safety, authority, or over-budget execution violations fail closed to
      dead-letter. Exhausted resources or persistent errors prohibit more work.
   b. On a validated current-version review, success requires zero mandatory
      failures, reviewer approval, verified evidence, and satisfied safety gates.
      Approval on the last allowed round succeeds; the cap is not retroactive.
   c. For a nonpassing current-version review, establish the initial baseline or
      test strict gap improvement. Route stalled, blocked, evidence-missing, or
      cycle/resource-exhausted work to dead-letter; otherwise allow another round.
   d. After non-review nodes, check only applicable structural/resource guards,
      not progress or approval from stale verdicts. A reviewer may finish an already
      admitted final round at cycle_count == max cycles if remaining resources
      permit; never dispatch another worker at that count. An optional final review
      is allowed only when the termination gate passes, never as an extra round
      after success or dead-letter. Terminal states have no continuation edges.
   Distinguish business cycles from runtime super-steps: set the executor step
   ceiling separately to accommodate sequential nodes and bound accidental loops.

8. Handle failure topology explicitly. Capture node identifier, input/artifact
   version, error category, completed side effects, and safe recovery checkpoint.
   Permit only bounded executor retries for demonstrated transient failures with
   idempotent operations; they still consume resource budget and are not new
   review approvals. Persistent errors, reviewer/controller disagreement, or an
   invalid state transition follow the escalation edge to a human or designated
   supervisor. Dead-letter is terminal for this run; do not automatically requeue
   it into the same cycle with fresh counters.

Return the delivered artifact or best reviewed partial result, terminal status,
node/edge contract, compact transition ledger, cycle and resource usage, gap
measurements, reviewer verdict, and unresolved issues with escalation ownership.
Distinguish specified, executed, reviewed, and approved work. A halted runtime
without approval is not a successful task, and an orchestration diagram is not
execution evidence.
```

## How It Works

[LangGraph's Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api) describes state, nodes, edges, conditional routing, per-field reducers, and reset semantics. Its [Pregel runtime documentation](https://docs.langchain.com/oss/python/langgraph/pregel) explains plan/execution/update super-steps, next-step visibility of updates, channel accumulation, and cycles. The legacy `langchain-ai.github.io/langgraph/concepts/low_level/` URL returned only a redirect page during retrieval; these current primary docs supplied the substance. Reviewer veto, measured progress, and dead-letter policy are authored safeguards, not automatic LangGraph behavior.

Unlike prompt chaining's linear stages, this graph deliberately revisits a worker through guarded cyclic edges. Unlike reflection or ReAct, it specifies role-owned state and routing rather than one agent's critique or action sequence. Unlike Graph of Thoughts, graph vertices are execution nodes rather than candidate solution artifacts. The workflow can be implemented with LangGraph or another executor; a prompt alone cannot enforce runtime isolation, independent review, or durable checkpoints.

## Variables

- `[nodes]`: role inventory, tools, inputs/outputs, permissions, acceptance checks, and escalation owner.
- `[state schema]`: typed fields with ownership, accumulation/reset rules, versioning, and gap metric.
- `[max cycles]`: hard worker/reviewer round cap; defaults to three, separate from runtime step limits.

## Tested On

Not model-tested. Original framework-grounded orchestration prompt; no multi-agent run or reliability benchmark is claimed.
