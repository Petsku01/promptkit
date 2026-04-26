[← Back to Model-Optimized Prompts](../index.md)

# Codex 5.3: Agentic Coding

## Task with Reasoning Effort
```
Task: [describe what you want to build/fix]

Context:
- Repository: [repo context]
- Files involved: [list files]
- Constraints: [any constraints]

Use medium reasoning effort for this task.
```

## Long-running Autonomous Task
```
Task: [complex multi-file task]

This is a complex task that may take a while. Work autonomously and:
1. Plan your approach first
2. Execute step by step
3. Verify each step works
4. Report progress

Use high reasoning effort.
```

## Code Review and Refactor
```
Review and refactor this codebase:

Focus areas:
- [area 1]
- [area 2]

Apply patches incrementally. Explain each change.
```

## Debugging Session
```
I'm seeing this issue:

Error: [paste error]
Context: [what you were doing]

Help me debug this systematically. Use the available tools to:
1. Explore the codebase
2. Identify the root cause
3. Propose and apply a fix
4. Verify the fix works
```

---
**Codex 5.3 Tips (from OpenAI docs):**
- Use "medium" reasoning effort for interactive coding (balances speed/intelligence)
- Use "high" or "xhigh" for hardest tasks requiring hours of autonomous work
- First-class compaction support enables multi-hour reasoning
- Much better at PowerShell and Windows environments than previous versions
- Fewer thinking tokens needed - more efficient than earlier Codex
- Works well with apply_patch tool for incremental changes
