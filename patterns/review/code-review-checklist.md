# Code Review Checklist Pattern

## Description

Systematic code review covering functionality, security, performance, style, error handling, tests, documentation, and architecture.

## When to use

Every pull request, especially for critical or complex changes.

## When to avoid

Trivial one-line changes where checklist overhead exceeds value.

## Template

```
Review this code against all 8 areas:

## 1. Functionality & Logic
- [ ] Code fulfills requirements
- [ ] Edge cases handled (null, empty, boundaries)
- [ ] No off-by-one errors
- [ ] Calculations verified
- [ ] Error paths tested

## 2. Security
- [ ] User inputs validated
- [ ] Outputs escaped/encoded
- [ ] No hardcoded secrets
- [ ] Proper auth checks
- [ ] Sensitive data encrypted

## 3. Performance
- [ ] No N+1 queries
- [ ] Algorithms appropriate
- [ ] Memory usage reasonable
- [ ] Caching used correctly
- [ ] Resource cleanup verified

## 4. Style & Consistency
- [ ] Follows team style guide
- [ ] Naming is clear
- [ ] No magic values
- [ ] Code structure logical
- [ ] Linter passes

## 5. Error Handling
- [ ] Exceptions caught specifically
- [ ] Resources cleaned up
- [ ] Error messages useful
- [ ] Graceful degradation
- [ ] Logging appropriate

## 6. Tests
- [ ] Tests exist for new code
- [ ] Happy path covered
- [ ] Edge cases tested
- [ ] Tests are meaningful
- [ ] CI passes

## 7. Documentation
- [ ] Complex logic explained
- [ ] API docs updated
- [ ] README updated if needed
- [ ] Comments explain "why"
- [ ] No stale comments

## 8. Architecture
- [ ] Follows existing patterns
- [ ] Single responsibility
- [ ] No tight coupling
- [ ] Dependencies correct
- [ ] Abstractions appropriate

## Summary
- **Status**: [APPROVE / REQUEST_CHANGES / COMMENT]
- **Blockers**: [Any critical issues]
- **Nitpicks**: [Minor suggestions]
- **Praise**: [What was done well]
```

## Example

```
Reviewing PR #42: User Authentication Refactor

## 1. Functionality & Logic ✅
- Password validation works correctly
- Edge case: empty password handled
- Token expiration logic verified

## 2. Security ⚠️
- [x] Inputs validated
- [x] No hardcoded secrets
- [ ] JWT secret should be rotated (suggested)
- [x] Auth checks in place

## 3. Performance ✅
- Query optimized with index
- No N+1 issues found

## 4. Style & Consistency ✅
- Follows Python PEP 8
- Variable names clear

## 5. Error Handling ✅
- Specific exceptions caught
- Error messages user-friendly

## 6. Tests ✅
- 95% coverage on new code
- Edge cases tested

## 7. Documentation ✅
- API docs updated
- Comments explain token flow

## 8. Architecture ✅
- Clean separation of concerns
- Service layer properly used

## Summary
- **Status**: APPROVE with minor suggestion
- **Blockers**: None
- **Nitpicks**: Consider JWT rotation
- **Praise**: Clean refactoring, good test coverage
```

## Tips

- Automate what you can (linters, security scans)
- Focus human review on logic and architecture
- Be constructive, not critical
- Approve quickly when criteria met

## Tags

code-review, checklist, quality, systematic, thorough
