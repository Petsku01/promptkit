# Test Documentation Pattern

## Description

Document test coverage, test strategies, and testing approach.

## When to use

Formalizing testing standards, onboarding QA teams, or maintaining test suites.

## When to avoid

Small changes where test documentation overhead exceeds value.

## Template

```
Document the test strategy for this feature:

Coverage areas:
- Unit: [What to unit test]
- Integration: [Integration test scope]
- E2E: [End-to-end scenarios]
- Performance: [Load/stress testing]
- Security: [Security testing]

For each area:
- Test approach
- Success criteria
- Tools/frameworks
- Mock/stub strategy

Test cases:
1. [Case 1]: Input -> Expected result
2. [Case 2]: Input -> Expected result
3. [Case 3]: Input -> Expected result
```

## Example

```
Document the test strategy for authentication:

Coverage areas:
- Unit: Token generation, validation, edge cases
- Integration: Auth & DB interaction
- E2E: Full login flow
- Security: JWT best practices

For each area:
- Test approach: Pytest with fixtures
- Success criteria: 100% branch coverage
- Mock/stub strategy: DB calls mocked

Test cases:
1. Valid token generation returns JWT
2. Invalid credentials rejected with 401
3. Expired token rejected with 403
4. SQL injection prevention

## Tags

testing, qa, test-plan, coverage
