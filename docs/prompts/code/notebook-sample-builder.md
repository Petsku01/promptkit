---
category: "code"
title: "Executable Python Notebook Sample Builder"
source: "github/awesome-copilot"
license: "MIT"
---
[← Back to Code Prompts](../index.md)

# Executable Python Notebook Sample Builder

**Category:** code
**Source:** Adapted from https://github.com/github/awesome-copilot/blob/1a4c3a7fc2c636ad5111a8b1b86493d5600f038e/agents/python-notebook-sample-builder.agent.md (MIT)

Copyright GitHub, Inc. Full permission and warranty notice: [NOTICE.md](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md#agentic-workflow-adaptations--github-mit).

## When to Use

Create a new instructional Python notebook from locally exercised public SDK examples, then validate the notebook itself in a clean kernel without overwriting existing work or publishing sensitive outputs.

## The Prompt

```text
Create a new executable Python notebook teaching one bounded capability.
Learning objective: [reader, prerequisites and observable outcome]
Repository context: [existing notebooks, sample code and style references]
Public SDK scope: [packages, supported versions and official documentation]
Execution permissions: [network access, credentials, paid-call budget and cleanup]
Output boundary: [new notebook path and companion prerequisite/evidence files]

1. Inspect existing notebooks and samples before drafting. Discover their cell
   structure, explanatory depth, dependency management, output policy and naming.
   Identify the actual Python interpreter, notebook kernel and installed packages;
   do not assume an editor, cloud provider or devcontainer. Use a project-approved
   isolated environment where appropriate. Never install directly into a shared
   environment merely because an upstream sample assumed container isolation.
   Confirm the proposed output path is new and preserve all existing notebooks.
2. Research the public SDK through official version-compatible documentation,
   release notes and public samples. Check installed signatures and exercise
   the supported APIs instead of pasting an outdated snippet. Use no internal-only
   packages, private endpoints or undocumented organization-specific setup. Record
   documentation URLs, dependency versions, required Python/kernel version and any
   differences between the documentation example and the runnable implementation.
3. Establish execution permissions before real calls. Reading credentials from an
   approved environment is not authorization to spend money or create resources.
   Require explicit permission for paid API calls, with account/resource scope,
   request/token/resource ceiling and cleanup policy. Avoid repeated billable calls
   during debugging and final run-all by budgeting both. If network, credentials
   or paid execution is unavailable, test independently runnable local portions
   and report the live path blocked; never replace missing service results with
   plausible fake outputs presented as real. Label deliberate offline fixtures.
4. Prototype and run each code fragment in a terminal using the intended Python
   environment before putting it in a notebook. Exercise setup, imports, SDK calls,
   parsing, error handling and cleanup. Keep a minimal prototype until the complete
   demonstration works. Fix failures at their actual source and record real results.
   No snippet may be advertised as verified merely because it parses. If a blocked
   live fragment must be delivered for later execution, label that cell unverified
   and do not invent its output or claim the full notebook is complete.
5. Assemble a valid notebook with a short title/objective cell, prerequisites and
   environment guidance, focused setup/import cells, and logical instructional
   sections. Each section should briefly explain the next operation before its
   code. Keep one teaching concept per code cell, explicit variable dependencies
   and readable names. Use tables or labeled charts where they clarify actual
   results, not a mandatory visualization for every value. End with interpretation,
   limitations, cleanup instructions and links for further reading.
6. Make execution order reproducible. Pin compatible dependencies through the
   project's existing mechanism and explain any kernel restart needed after setup.
   Do not rely on terminal variables, stale notebook globals, hidden files or a
   previously authenticated interactive session. Load secrets without displaying
   them, use synthetic inputs where possible, and keep generated resources bounded.
   Validate cell metadata and notebook structure with available notebook tooling.
7. Restart the intended kernel and run every cell from top to bottom with an
   explicit timeout. Repeat after resolving errors; out-of-order execution is not
   acceptance. Capture environment, exact execution command, exit status and failed
   cell identifiers without secret values. Terminal prototype success alone does
   not establish kernel dependency availability or cell order. If the clean run
   would exceed the authorized budget, stop and report that validation incomplete.
8. Inspect saved outputs, exceptions, metadata, attachments and rich displays for
   credentials, personal records and sensitive URLs. Redact or clear unsafe outputs
   without altering code semantics, and state what was removed. Preserve an execution
   record separately from publication-safe notebook output. Confirm cleanup against
   the exact authorized resources, or report any resources left for the owner.

Deliver the new notebook, reproducible prerequisites and execution evidence. Report
prototype checks and clean-kernel run-all separately, list unverified cells and
remaining cleanup, and never overwrite an existing notebook to resolve a path clash.
```

## How It Works

Run-before-write catches SDK errors early; restart-and-run-all catches notebook-specific state and ordering failures. Environment discovery replaces upstream editor/cloud assumptions, while explicit paid-call and output-redaction gates make the sample safer to execute and share.

## Variables

- `[reader, prerequisites and observable outcome]`: teaching contract.
- `[existing notebooks, sample code and style references]`: style and reuse context.
- `[packages, supported versions and official documentation]`: public SDK evidence.
- `[network access, credentials, paid-call budget and cleanup]`: execution limits.
- `[new notebook path and companion prerequisite/evidence files]`: non-overwriting deliverables.

## Tested On

Not model-tested. Curated adaptation; no live model-quality evaluation is claimed.
