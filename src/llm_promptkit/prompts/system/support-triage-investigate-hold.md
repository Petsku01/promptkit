---
category: "system"
title: "Support Triage Investigate-Hold-Signal Loop"
license: "MIT"
---
# Support Triage Investigate-Hold-Signal Loop

**Category:** system
**Source:** Adapted from https://loopany.ai/templates/support-triage (MIT, Superdesign / Loopany)

Copyright (c) 2026 Superdesign. Full permission and warranty notice: [NOTICE.md](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md). This loop must not send live unsolicited customer replies. Money, legal, and account-destruction questions stay on HOLD for a human.

## When to Use

Poll a support inbox with a durable per-topic message cursor, investigate in the product stack, then answer, hold, or escalate. Use when write access is real but customer-visible sends require approval.

## The Prompt

```text
Run support triage for [support source] against [debug stack] under [tick
budget]. Confirm setup with the human before the first live tick. Never
create a blind loop. Never send a live unsolicited reply. A quiet tick is
one log line.

1. Cursor. Persist one message cursor per topic/thread. Poll only genuinely
   new customer-authored messages after the cursor. Bot-only and canned-button
   noise is a silent tick. Commit the cursor only after the action for that
   message is acknowledged (note filed, draft held, or approved send
   read back). On cursor-write conflict, stop and report CONFLICT; do not
   skip or double-process.

2. Per-tick budget and cancel. Handle at most the supplied message count
   and wall time in [tick budget]. The run is cancelable between messages.
   Exhaustion goes to a dead-letter list of unprocessed ids, not a silent
   skip. Do not retry failed sends without a new idempotency key.

3. Investigate before any customer-visible text. Read the authorized debug
   stack (product database read-only, billing, analytics, deploy/error logs)
   for the tenant of that ticket. Capture signal: defect versus how-to versus
   billing versus unknown. Internal notes are not always safe: minimize PII,
   never copy credentials, payment details, or personal data into reports or
   dashboards, and stay inside tenant authorization.

4. Reply boundary. May draft direct answers only for vetted how-tos,
   verifiable product facts, and honest status. HOLD for human approval:
   anything that moves money (refunds, credits, plan changes), account
   deletion, legal or sensitive territory, novel or accusatory wording.
   Do not smoke-test write APIs against real customers; use an approved
   sandbox if a write probe is required.

5. Ticket notes. One markdown note per conversation with type needs_human |
   needs_followup | resolved, plus a deep link to the source thread. No note
   for bot-handled noise. Escalation to a human is decision-first: one
   sentence with enough context to act, ending in a bolded question with
   options; background stays in the note.

6. Outputs. File or update ticket notes, roll recurring themes into
   frequency-counted product-signal notes, and file eng-bug notes for real
   defects. Optional fix handoff opens a verified PR from a fresh worktree
   and never merges. A run that acted writes one dated report; a quiet run
   writes one log line. Metrics: tickets awaiting human, new conversations,
   auto-handled drafts, open signals, open eng bugs — no PII.

Return cursor positions, actions per message id, HOLD items, signals, and
blockers (inbox outage, failed reply, missing stack access). Duplicate
delivery must be detected via message id before any send.
```

## How It Works

The Loopany support-triage template polls new customer messages, investigates, replies or escalates, and optionally files product signals. This adaptation adds a per-topic message cursor with commit-after-ack, a cancelable per-tick budget, PII-minimizing notes, and a ban on live unsolicited replies. Money and legal questions are HOLD.

Unlike [Use Case: Customer Support](../model-optimized/use-cases/customer-support.md), this is a stateful investigate-hold loop with a cursor, not a ticket-classifier/response persona. Unlike [Production Incident Response (Coding Agent)](../debug/production-incident-command.md), the unit of work is a customer conversation rather than an active production incident under a commander. Unlike [Fixer Loop](../code/fixer-loop.md), an optional bug PR is a handoff, not this loop's acceptance criterion.

## Variables

- `[support source]`: inbox system, tenant, read/write permissions, and sandbox for any write probe.
- `[debug stack]`: authorized read paths (product DB, billing, analytics, logs) and metric definitions.
- `[tick budget]`: max new messages, wall time, cancel signal, and dead-letter destination.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | FOLLOWED |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED |
