# Architecture Decision Record Pattern

## Description

Document architectural decisions with context, options, and trade-offs.

## When to use

Significant architectural choices, technology selection, or design pattern adoption.

## When to avoid

Trivial decisions where overhead isn't justified.

## Template

```
# ADR-XXX: [Short Title]

## Context
[What is the issue we're deciding?]

## Decision
[What we decided]

## Consequences
[What becomes easier, harder, or changes]

## Alternatives Considered
| Option | Pros | Cons |
|--------|------|------|
| Option A | ... | ... |
| Option B | ... | ... |

## Status
Proposed | Accepted | Deprecated | Superseded

## Date
[Date]
```

## Example

```
# ADR-001: Authentication Strategy

## Context
We need to choose between session-based and JWT authentication.

## Decision
We will use JWT with refresh tokens.

## Consequences
- Statelessness allows horizontal scaling
- Token refresh adds complexity
- Revocation requires token blacklist

## Alternatives Considered
| Option | Pros | Cons |
|--------|------|------|
| Session-based | Simpler | Requires sticky sessions |
| JWT | Stateless | Token refresh complexity |
| OAuth2 | Industry standard | Overkill for our needs |

## Status
Accepted

## Date
2025-03-15
```

## Tags

adr, architecture, decisions, documentation
