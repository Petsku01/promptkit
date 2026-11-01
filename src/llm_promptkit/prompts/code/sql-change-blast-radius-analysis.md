---
category: "code"
title: "SQL Change Blast-Radius Analysis"
source: "github/awesome-copilot"
license: "MIT"
---
# SQL Change Blast-Radius Analysis

**Category:** code
**Source:** Adapted from https://github.com/github/awesome-copilot/blob/5269f7ea2d6c3a9bfda5ed878b6726cf509121fd/skills/sql-object-impact-analysis/SKILL.md (MIT)

Copyright GitHub, Inc. Full permission and warranty notice: [NOTICE.md](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md#agentic-workflow-adaptations--github-mit).

## When to Use

Before renaming, dropping or changing a database object, trace SQL dependencies and application consumers without altering schema or data. This is dependency analysis, not query optimization or permission to migrate.

## The Prompt

```text
Produce a read-only pre-change dependency report.
Target: [database, schema, exact object identifier and type]
Proposed change: [rename, drop, type, signature or behavior change]
Sources: [repository path/revision, schema definitions and authorized metadata]
Scope and budget: [modules, databases and trace depth]

1. Resolve the exact target, dialect and identifier quoting/case rules. For a
   column include its parent table; for overloaded routines include the signature.
   If ambiguity changes the target, stop and request identification rather than
   search an assumed object. Record source identities, freshness and omissions.
2. Search SQL definitions, migration scripts and available read-only dependency
   metadata. Identify referencing procedures, views, functions, triggers, foreign
   keys, synonyms and scheduled jobs. Include read/write/filter usage and call
   chains. Do not execute stored procedures or application flows, run migrations,
   or change files/data. Use only authorized read-only metadata queries.
3. Search application SQL strings, ORM mappings, repositories/data-access methods,
   services, API handlers and client contracts. Trace affected paths to reporting,
   jobs, integrations and frontend consumers within budget. Cite each discovered
   hop instead of assuming an endpoint or class maps to a particular table.
4. Inspect dynamic SQL, constructed identifiers, configuration, reflection,
   generated code and cross-database references. Record unresolved constructions
   and external consumers as unknowns, not fabricated dependencies.
5. Label each finding Direct (explicit verified reference), Indirect (evidenced
   call/mapping chain), or Uncertain (plausible but unresolved). Show the chain and
   confidence; a literal text match alone may be a comment or unrelated namesake.
   Distinguish verified references from incidental search hits.
6. Assess impact of the specified change on projections, parameters, types,
   constraints, callers and returned contracts. Separate observed facts from
   predicted breakage. Highlight jobs, reporting and external integrations.

Return these sections:
- Target Object: exact identifier/type, proposed change, source revision/freshness.
- Direct SQL Dependents: object, usage, verified path:line or metadata evidence.
- Application Code Dependents: layer, file/symbol, call chain and evidence.
- Indirect / Dynamic References: confidence, unresolved hops and verification owner
  if supplied; do not invent people or systems.
- Risk Summary: change-specific impact, searched scope/method and unsearched areas.
- Suggested Verification Steps: smallest staging tests, contract checks or owner
  questions needed before any change; list them, do not execute them here.

Static search is never proof of completeness. Say "no references found within
these sources by these searches" rather than "unused" or "safe to drop". Explain
limits from dynamic SQL, generated artifacts, stale schemas and external callers.
If budget prevents a full trace, name the remaining areas and next bounded pass.
Never invent paths, line numbers, object names or successful verification.
```

## How It Works

SQL-first discovery followed by application tracing exposes cross-layer effects. Explicit evidence classes keep unresolved dynamic references visible without asserting an exhaustive blast radius.

## Variables

- `[database, schema, exact object identifier and type]`: unambiguous target, including table or signature where needed.
- `[rename, drop, type, signature or behavior change]`: change whose consequences matter.
- `[repository path/revision, schema definitions and authorized metadata]`: actual evidence sources.
- `[modules, databases and trace depth]`: scope, access and effort bounds.

## Tested On

Not model-tested. Curated adaptation; no live model-quality evaluation is claimed.
