---
category: "debug"
title: "Four-Phase Root-Cause Debugging with Evidence and Reassessment Gates"
source: "obra/superpowers"
license: "MIT"
---
[← Back to Debug Prompts](../index.md)

# Four-Phase Root-Cause Debugging with Evidence and Reassessment Gates

**Category:** debug
**Source:** Adapted from https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/systematic-debugging/SKILL.md (MIT)

Copyright (c) 2025 Jesse Vincent. Full permission and warranty notice: [NOTICE.md](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md#agentic-workflow-adaptations--superpowers-mit).

## When to Use

Investigate a failure that crosses component boundaries or has resisted repeated fixes. The distinctive gate is evidence before a durable fix, with explicit reassessment instead of an escalating stack of speculative patches.

## The Prompt

```text
Investigate this failure through four phases. Do not propose a durable fix until
an observed causal chain and a discriminating experiment support it.
Incident: [symptom, expected behavior and reproduction context]
Scope: [repository, environments and authorized diagnostic actions]
Budget: [time, requests, log volume and instrumentation lifetime]
Urgency: [impact and authorized reversible mitigation limits]

Phase 1 — Root-cause investigation.
Read the complete error and relevant stack trace; record exact codes, locations,
versions and timing without publishing secrets. Reproduce with precise inputs
and environment. Classify consistent, intermittent and unreproduced failures;
non-reproduction means evidence is missing, not that the issue is fixed. Inspect
recent code, dependency, configuration and deployment changes as candidates,
not automatic causes. Establish a baseline and retain a redacted reproduction.

For a multi-component path, draw the boundaries: caller to service, service to
queue, worker to database, or CI to build to signing. At each relevant boundary
capture bounded input/output shape, status, correlation identifier and timing.
Check whether required configuration is present and propagated without dumping
its secret value. Prefer existing telemetry; obtain permission before adding
probes. Set sampling, retention, request and runtime ceilings. Do not log full
environments, credentials, tokens, personal payloads or unrestricted database
rows. Stop diagnostics if load or sensitive-data exposure exceeds the budget.
Find the first boundary where observed state departs from the contract.

Trace backward from that bad value or failed operation. Identify its immediate
caller and supplied arguments, then where those arguments were produced. Repeat
through wrappers, asynchronous handoffs and configuration assembly until you
reach the earliest observed invalid transition. Record each link and the evidence
supporting it. Do not patch the final exception handler merely because that is
where the symptom surfaced. If a link cannot be observed, label the gap and design
one bounded probe instead of inventing a causal story.

Phase 2 — Pattern analysis.
Find a comparable working path and read its relevant implementation and setup.
List concrete differences in inputs, ordering, versions, configuration, state,
permissions and lifecycle. Check dependencies and assumptions before copying a
pattern. Narrow which differences can explain the first failing boundary; do not
bundle all differences into a speculative rewrite. A library or infrastructure
failure remains possible, but requires evidence just like an application defect.

Phase 3 — Hypothesis and minimal experiment.
Write one falsifiable statement: “X causes Y because observed evidence Z; if true,
changing only A should produce B, while the baseline produces C.” Choose the
smallest reversible experiment that distinguishes it from plausible alternatives.
Record predicted and actual results. Change one variable, repeat only within the
budget, and restore experimental changes before trying a different hypothesis.
A failed experiment updates the evidence ledger; do not stack another fix on top.
If uncertain, name the uncertainty and return to the missing Phase 1 observation.

Phase 4 — Implementation and verification.
Capture a regression test that fails for the observed reason on the baseline;
use a deterministic minimal harness if the repository lacks a test framework.
Implement one scoped correction at the supported causal boundary. Run the
regression, relevant integration checks and applicable broader suite, preserving
existing edge-case assertions. Confirm the original reproduction is resolved,
not merely that a different error or silent fallback replaced it. Record actual
commands and outputs. A passing test is evidence within its coverage, not proof
that every possible environment is repaired.

Stop and decision rules:
- Proposing several fixes before tracing, changing several variables, skipping
  baseline evidence or saying “one more quick attempt” means stop and return to
  investigation. Do not let a convenient theory become a substitute for data.
- After three or more failed fix attempts, stop further fixes and REASSESS the
  reproduction, assumptions, test oracle, coupling and architecture with the
  maintainer. This threshold is not proof the architecture is wrong. Obtain an
  agreed revised approach before a fourth fix; a broad refactor is not automatic.
- During an incident, a separately authorized scoped reversible mitigation may
  precede causal certainty. Record its hypothesis, blast radius, rollback trigger,
  owner and expiry. Track user-impact recovery and root-cause uncertainty
  separately; mitigation success does not close the investigation.
- External or timing-dependent causes may remain unresolved. Report observations,
  rejected hypotheses and the next discriminating measurement. Bounded retry,
  timeout or monitoring changes require their own safety and behavior contract.

Remove temporary instrumentation and restore temporary configuration/state you
introduced; retain only approved diagnostics with explicit ownership. Finish with
phase reached, redacted causal chain, experiment ledger, attempt count, mitigation
status, tests actually run, cleanup result and remaining unknowns. Report blocked
or partial outcomes honestly rather than declaring a guessed root cause fixed.
```

## How It Works

Boundary instrumentation localizes the first bad transition, backward tracing identifies its producer, and one-variable experiments distinguish causation from correlation. The attempt threshold changes the decision process without diagnosing architecture by numerology.

## Variables

- `[symptom, expected behavior and reproduction context]`: observable failure and baseline.
- `[repository, environments and authorized diagnostic actions]`: investigation permissions.
- `[time, requests, log volume and instrumentation lifetime]`: diagnostic ceilings and cleanup deadline.
- `[impact and authorized reversible mitigation limits]`: independent incident-response boundary.

## Tested On

Not model-tested. Curated adaptation; no live model-quality evaluation is claimed.
