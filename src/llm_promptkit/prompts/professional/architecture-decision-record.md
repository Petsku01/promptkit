---
category: "professional"
title: "Architecture Decision Record"
source: "github/awesome-copilot"
license: "MIT"
---
# Architecture Decision Record

**Category:** professional
**Source:** Adapted from https://github.com/github/awesome-copilot/blob/5269f7ea2d6c3a9bfda5ed878b6726cf509121fd/agents/adr-generator.agent.md (MIT)

Copyright GitHub, Inc. Full permission and warranty notice: [NOTICE.md](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md#agentic-workflow-adaptations--github-mit).

## When to Use

Turn a supplied architectural decision, context and considered options into a proposed ADR. This is a documentation workflow, not an automatic repository investigation or a substitute for stakeholder approval.

## The Prompt

```text
Draft an Architecture Decision Record using only supplied decision information
and identified supporting sources.
Decision inputs: [title, problem, constraints, chosen solution and rationale]
Options and people: [actually considered alternatives, rejection reasons and known stakeholders]
Evidence: [decision notes, measurements, official docs and related ADRs]
Project conventions: [project root, ADR directory, numbering and status rules]
Delivery mode: [response-only or authorized new file]

1. Establish the decision, constraints, rationale, actual alternatives and known
   stakeholders from these inputs. Link facts and trade-offs to supplied evidence.
   Distinguish measured outcomes, stakeholder statements and predicted effects.
   Do not invent rejected options, people, metrics, dates or consensus to fill a
   template quota. Mark unknowns explicitly; if the decision itself is missing,
   request it rather than pretending one was made. In non-interactive mode return
   a clearly incomplete draft with blockers, not a fictitious accepted decision.
2. Follow the project's ADR convention. Resolve all filesystem paths relative to
   the project root, never the operating-system root. If access is available,
   inspect the specified ADR directory for numbering and collisions; otherwise
   mark the number provisional. Default directory: docs/adr. Default filename:
   adr-NNNN-title-slug.md, with a four-digit next sequential number. Do not create
   directories or overwrite existing ADRs without authorization.
3. Produce Markdown with metadata: title, Proposed status unless an evidenced
   status is supplied, supplied date/authors, tags and known supersession links.
   Omit unknown optional metadata or label it unknown. Creating an ADR does not
   mean the architecture has been approved or implemented.
4. Include these sections:
   - Status: decision state and approval still needed, if known.
   - Context: problem, forces, constraints, scope and why a decision is necessary.
   - Decision: chosen approach and rationale tied to the supplied constraints.
   - Consequences: positive and negative trade-offs, evidence, uncertainties and
     conditions under which predicted benefits/risks apply.
   - Alternatives Considered: only actual supplied options and documented reasons;
     if none are documented, say so. A suggested future option must be labeled
     a suggestion, never retroactively described as rejected.
   - Implementation Notes: known rollout/migration considerations and proposed
     validation, explicitly separate from completed work.
   - References: verified supplied sources and related ADR links.
   - Open Questions: missing evidence, unresolved assumptions and needed decisions.
5. Use stable POS-001, NEG-001, ALT-001, IMP-001 and REF-001 labels when useful,
   without forcing arbitrary numbers of bullets. Keep language precise; retain
   adverse consequences and disagreements rather than smoothing them away.
6. Check internal consistency: does the rationale address the constraints, do
   references support the claims, and are predictions labeled? Do not claim a
   repository scan, performance validation or stakeholder consultation occurred
   unless it actually did. Keep paths project-root-relative and links correct
   relative to the proposed ADR file. Write only in the authorized delivery mode.

Return the proposed ADR, intended project-relative filename, numbering evidence
or provisional status, and unresolved inputs. Never silently mark it Accepted.
```

## How It Works

Structured context, decision, consequences and alternatives preserve the rationale behind an architectural choice. Explicit unknowns and evidence labels avoid manufacturing a history of consultation or evaluation.

## Variables

- `[title, problem, constraints, chosen solution and rationale]`: actual decision context.
- `[actually considered alternatives, rejection reasons and known stakeholders]`: documented participants and options, not a quota.
- `[decision notes, measurements, official docs and related ADRs]`: support for factual claims and trade-offs.
- `[project root, ADR directory, numbering and status rules]`: project-relative output convention.
- `[response-only or authorized new file]`: delivery permission; default is response-only.

## Tested On

Not model-tested. Curated adaptation; no live model-quality evaluation is claimed.
