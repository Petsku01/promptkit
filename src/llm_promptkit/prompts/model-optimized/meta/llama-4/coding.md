# Llama 4: Coding

## Code Generation (Scout — Fast & Efficient)
```
Write [language] code for: [task]

Requirements:
- [req 1]
- [req 2]

Include type hints and basic error handling.
Keep it clean and straightforward.
```

## Code Generation (Maverick — High Quality)
```
Implement [feature description] in [language].

Codebase context:
[paste relevant files or describe patterns]

Requirements:
- [requirement 1]
- [requirement 2]

Constraints:
- Follow existing code patterns
- Include comprehensive error handling
- Add docstrings and inline comments for complex logic
- Write tests for happy path and edge cases

Output complete, production-ready code.
```

## Code Review
```
Review this code thoroughly.

[paste code]

Evaluate:
1. **Correctness** — does it do what's intended?
2. **Performance** — any unnecessary allocations or O() issues?
3. **Security** — injection, auth, or data exposure risks?
4. **Readability** — clear naming, proper structure?
5. **Edge cases** — what inputs break it?

Prioritize: [correctness / performance / readability]
```

## Debugging
```
This code is broken:

[paste code]

Error:
[paste error message / stack trace]

What I expected: [expected behavior]
What actually happens: [actual behavior]

Find the root cause and provide a minimal fix.
Explain why it broke.
```

## Multi-File Feature Implementation (Maverick)
```
Implement this feature across multiple files:

Feature: [description]
Tech stack: [language / framework]

Files to modify:
1. [file1] — [what changes]
2. [file2] — [what changes]
3. [file3] — [what changes]

Working approach:
1. Read existing code patterns
2. Plan minimal changes
3. Implement each change
4. Verify consistency across files

Constraints:
- Maintain backward compatibility
- Follow existing patterns and naming
- All existing tests must still pass
```

---

**Llama 4 Coding Tips:**
- Scout (17B active) is great for quick code generation and reviews — fast and cheap
- Maverick (400B total) excels at complex multi-file implementations
- Both variants support tool use for agentic coding workflows
- Explicit format requirements lead to better results
- Great for self-hosted coding assistants with full codebase context (up to 10M tokens)