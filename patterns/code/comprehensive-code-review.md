# Comprehensive Code Review Pattern

## Description

Multi-model code review with parallel execution from different AI perspectives, synthesis of feedback, and iterative fixing.

## When to use

Critical code changes where thorough review is needed before merging — especially complex refactors, security-sensitive changes, or architectural decisions.

## When to avoid

Simple one-line changes where review overhead exceeds value.

## Template

```
You are a senior software engineer doing a comprehensive code review.

Review the current branch changes against [TARGET_BRANCH]. Use available tools to view git diff and examine the code.

Provide feedback on:

1. **Bugs/Issues**
   - Logic errors and incorrect assumptions
   - Edge cases not handled
   - Potential crashes or exceptions
   - Race conditions
   - State management issues

2. **Security**
   - Injection vulnerabilities (SQL, XSS, command injection)
   - Authentication/authorization flaws
   - Sensitive data exposure
   - Input validation gaps
   - Dependency vulnerabilities

3. **Performance**
   - Inefficient algorithms or data structures
   - N+1 query problems
   - Memory leaks
   - Unnecessary computations
   - Blocking operations

4. **Code Quality**
   - Readability and naming conventions
   - Function complexity (cyclomatic complexity)
   - Code duplication
   - SOLID principles
   - Documentation adequacy

5. **Best Practices**
   - Idiomatic language/framework patterns
   - Error handling (exceptions, error codes, logging)
   - Test coverage
   - Type safety
   - API design

## Output Format

For each issue found, provide:
- **Severity**: CRITICAL | WARNING | SUGGESTION
- **File**: Line numbers
- **Issue**: Clear description
- **Impact**: Why it matters
- **Fix**: Specific suggestion with code example

Be specific - reference line numbers and file names.
Prioritize: critical issues first, nitpicks last.

If no significant issues found, say "LGTM" and explain what makes it good.
```

## Example

```
You are a senior software engineer doing a comprehensive code review.

Review the current branch changes against main. Use available tools to view git diff and examine the code.

Provide feedback on:

1. **Bugs/Issues**
   - Logic errors and incorrect assumptions
   - Edge cases not handled
   - Potential crashes or exceptions

2. **Security**
   - Injection vulnerabilities
   - Authentication/authorization flaws
   - Sensitive data exposure

3. **Performance**
   - Inefficient algorithms
   - N+1 query problems
   - Memory leaks

4. **Code Quality**
   - Readability and naming
   - Function complexity
   - Code duplication

5. **Best Practices**
   - Idiomatic patterns
   - Error handling
   - Test coverage

## Output Format

For each issue found, provide:
- **Severity**: CRITICAL | WARNING | SUGGESTION
- **File**: Line numbers
- **Issue**: Clear description
- **Impact**: Why it matters
- **Fix**: Specific suggestion with code example

Be specific - reference line numbers and file names.
Prioritize: critical issues first, nitpicks last.
```

## Multi-Model Workflow (Optional)

For maximum thoroughness, run this prompt through multiple models (Claude, GPT, Gemini) and synthesize:

1. **Consensus Issues** — flagged by 2+ reviewers
2. **Unique Insights** — valid issues from single reviewer
3. **Discarded** — evaluated and found invalid

Iterate: Fix valid issues, re-run review, stop when only repetitive nitpicks remain.

## Tips

- Don't skip "small" issues — if valid, fix it
- Trust consensus on subjective matters
- Reviews taking 10-30 minutes is normal for complex changes

## Tags

code-review, security, performance, quality, comprehensive
