[← Back to Debug Prompts](../index.md)

# bug-risk-analysis

**Category:** debug
**Source:** prompts.chat (contributor: @wkaandemir)

## When to Use

Use this prompt when you need an AI to act as a bug-risk-analysis.

## The Prompt

```
# Bug Risk Analysis: Agent Personas

## Executive Summary
This assessment focuses on reliability and logic errors in agent persona definitions. Primary risks stem from the complexity in the `pm-agent` state machine and potential conflicting triggers between expert agents, leading to "multi-agent confusion" where multiple agents attempt to respond to the same query.

## Detailed Findings

### 1. State Machine Fragility (PM Agent)
- **File**: `dev/pm-agent.md`
- **Location**: "Session Start Protocol"
- **Risk**: **High**
- **Description**: The protocol assumes `list_memories()` and `read_memory()` operations will always succeed. If the MCP server is cold or returns empty, the agent has no fallback behavior defined in the prompt. It may loop or hallucinate a "new" start when it shouldn't.
- **Potential Bug**: Agent cannot initialize context and overwrites previous work with a blank slate.

### 2. Ambiguous Agent Triggers
- **File**: `dev/backend-architect.md` vs `dev/security-engineer.md`
- **Location**: `Triggers` section
- **Risk**: Medium
- **Description**: Both agents trigger on "Security... requirements" (Backend) and "Vulnerability..." (Security).
- **Potential Bug**: A user asking about "secure API design" could trigger *both* agents, causing a race condition or double response in a chat interface (if the system allows auto-execution).

### 3. "Docs/Temp" File Pollution
- **File**: `dev/pm-agent.md`
- **Location**: "Documentation Cleanup"
- **Risk**: Medium
- **Description**: The agent is responsible for deleting old hypothesis files (>7 days). This is a manual instruction given to an LLM. LLMs are notoriously bad at date calculation and "cleaning up" without explicit, rigorous tool chains.
- **Potential Bug**: Over time, `docs/temp/` will accumulate thousands of files because the agent ignores the cleanup task or cannot correctly identify "7-day-old" files.

### 4. Socratic Loop Deadlocks
- **File**: `dev/socratic-mentor.md`
- **Location**: "Response Generation Strategy"
- **Risk**: Low
- **Description**: The agent is instructed to *never* give direct answers ("only... explain after user discovers"). If the user gets stuck and frustrated, the agent may stubbornly keep asking questions, leading to a poor user experience (an infinite "Why?" loop).

## Recommended Fixes

1.  **Define Fallback States**: Update `pm-agent`: "If memory read fails, assume NEW SESSION and ask user for confirmation."
2.  **Disambiguate Triggers**: Edit `backend-architect` triggers to exclude "Security audits" and focus entirely on "Implementation."
3.  **Automate Cleanup**: Don't rely on the agent to delete files. Use a cron job or a dedicated "Janitor" script/tool for `docs/temp` cleanup.
4.  **Escape Hatch**: Add a "Frustration Detected" clause to `socratic-mentor`: "If user expresses frustration, switch to Direct Explanation mode."
```

## Variables

Replace placeholder text in curly braces or quotes with your specific content.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| GPT-4 | Yes | Works well |
| Claude | Yes | Works well |
| Llama 3 | Yes | Works well |
