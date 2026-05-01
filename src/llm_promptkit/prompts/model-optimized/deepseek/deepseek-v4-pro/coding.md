# DeepSeek V4 Pro: Coding

## Agentic Code Implementation (Cost-Optimized)
```
You are implementing a feature autonomously.

Task: [detailed description]
Codebase: [paste structure or describe]

Execution protocol:
1. Read relevant files to understand patterns
2. Plan minimal changes needed
3. Implement each change
4. Run tests after each logical step
5. Fix any failures before proceeding
6. Verify end-to-end

Constraints:
- Follow existing code style and patterns
- Keep changes minimal and focused
- All tests must pass
- Document non-obvious decisions in comments

Cost note: At ~1/7th the cost of Claude Opus, execute full agentic loops confidently.
Long-running autonomous sessions (8+ hours) are economically viable.
```

## Full-Stack Feature Development
```
Implement this full-stack feature:

Feature: [description]
Tech stack: [frontend / backend / database]
Existing patterns: [describe or reference]

Deliver:
1. Database migration (if needed)
2. Backend API endpoint(s)
3. Frontend UI component(s)
4. Integration tests
5. Brief documentation update

Work through each component sequentially.
Test as you go. Fix failures immediately.
```

## Code Review at Scale
```
Review this large changeset efficiently.

PR description: [paste]
Files changed: [count or list key files]

Review strategy:
1. Start with the architecture — does the change make sense?
2. Check public API changes — are they backward compatible?
3. Review security-critical code paths
4. Check error handling and edge cases
5. Verify test coverage for new code
6. Look for performance implications

Prioritize findings:
- 🔴 Must fix before merge
- 🟡 Should fix soon
- 🟢 Nice to have

Be thorough but efficient — focus on correctness over style.
```

## Long-Context Codebase Analysis
```
I need to understand this codebase. The full source fits in V4's 1M context.

Questions: [what I need to understand]

Approach:
1. Map the overall architecture
2. Trace the data flow for [specific feature]
3. Identify key abstractions and their relationships
4. Find potential issues or inconsistencies
5. Answer each question with code references

Note: V4 Pro's 1M context can hold an entire medium codebase.
Provide the full source if possible for best results.
```

---
**DeepSeek V4 Pro Coding Tips:**
- Excellent at LiveCodeBench (93.7) — one of the strongest coding models
- 1M token context — can hold entire codebases for analysis
- 1/7th the cost of Claude Opus — run long agentic loops cheaply
- Strong at autonomous multi-step coding workflows
- Use `deepseek-chat` for standard, `deepseek-reasoner` for thinking mode
- MIT licensed for self-hosting if needed