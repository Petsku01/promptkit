# GPT-4.1: Coding

## Full Feature Implementation
```
Implement [feature description] in this codebase.

Language: [Python/TypeScript/etc]
Framework: [Django/Next.js/etc]
Test runner: [pytest/jest/etc]

Requirements:
- [requirement 1]
- [requirement 2]

Constraints:
- Follow existing code patterns
- Add type hints/annotations
- Include error handling for edge cases
- Write tests for new code
- Update relevant documentation

Provide the complete implementation with all files changed.
```

## Code Review
```
Review this code as a senior engineer:

1. **Bugs**: List any bugs or potential issues
2. **Security**: Check for vulnerabilities
3. **Performance**: Identify inefficiencies
4. **Readability**: Suggest improvements
5. **Testing**: What tests are needed?

Reference specific line numbers. Be explicit about severity.

Code:
```

## Debug Assistant
```
Help me debug this error:

Error message:
[paste error]

Code:
[paste code]

Provide:
1. **Error explanation**: What does this error mean?
2. **Root cause**: Why is this happening?
3. **Fix**: Exact code change needed
4. **Prevention**: How to avoid this in future
5. **Verification**: How to confirm it's fixed
```

## Multi-File Refactoring
```
Refactor this module structure:

Current structure:
[paste file tree or describe]

Problems:
- [problem 1]
- [problem 2]

Goals:
- [goal 1]
- [goal 2]

Constraints:
- No breaking API changes
- All existing tests must pass
- Minimize diff size

Produce a plan first, then implement each step.
```

## API Design
```
Design a [REST/GraphQL/gRPC] API for [feature/system].

Requirements:
- [requirement 1]
- [requirement 2]

Provide:
1. Endpoint specifications (method, path, params)
2. Request/response schemas (JSON with types)
3. Authentication approach
4. Rate limiting strategy
5. Error response format
6. SDK client interface (TypeScript or Python)
```

## Unit Tests
```
Write unit tests for this function:

[paste function]

Requirements:
- Framework: [pytest/jest/etc]
- Cover: happy path, edge cases, errors
- Use descriptive test names
- Include setup/teardown if needed
- Mock external dependencies

Provide complete, runnable test file.
```

---
**GPT-4.1 Coding Tips:**
- Excels at following detailed coding instructions precisely
- Better at maintaining consistency across multi-file changes than GPT-4o
- Specify formatting preferences explicitly (type hints, docstrings, etc.)
- Use `developer` role with explicit constraints for best results
- Supports Structured Outputs — use `response_format` with Pydantic schemas for guaranteed output types