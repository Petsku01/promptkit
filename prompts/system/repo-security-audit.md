# Repository Security & Architecture Audit

**Use case:** Comprehensive code repository security and architecture review

**Source:** prompts.chat — Repository Security & Architecture Audit Framework

---

## Quick Version (~120 tokens)

```
Audit repository [REPO_NAME] for security and architecture.

Check against:
- OWASP Top 10 (2021)
- SOLID Principles
- DORA Metrics
- Google SRE Production Readiness

Output: Critical findings with severity and fixes.
```

---

## Extended Version (~500 tokens)

```
# Repository Security & Architecture Audit Framework

Research-backed repository audit covering OWASP Top 10, SOLID principles, DORA metrics, and Google SRE production readiness criteria.

## Audit Anchors

- OWASP Top 10 (2021)
- SOLID Principles (Robert C. Martin)
- DORA Metrics (Forsgren, Humble, Kim)
- Google SRE Book (production readiness)

## Variables

- repository_name: [Name of repository]
- stack: [Auto-detect from package.json, requirements.txt, go.mod, etc.]

## Audit Sections

### A. Security (OWASP Top 10)
Check for:
- Injection vulnerabilities (SQL, NoSQL, Command)
- Broken authentication
- Sensitive data exposure
- XML external entities (XXE)
- Broken access control
- Security misconfiguration
- Cross-site scripting (XSS)
- Insecure deserialization
- Using components with known vulnerabilities
- Insufficient logging and monitoring

### B. Architecture (SOLID)
Evaluate:
- Single Responsibility Principle
- Open/Closed Principle
- Liskov Substitution Principle
- Interface Segregation Principle
- Dependency Inversion Principle

### C. Delivery Performance (DORA)
Measure:
- Deployment Frequency
- Lead Time for Changes
- Mean Time to Recovery (MTTR)
- Change Failure Rate

### D. Production Readiness (Google SRE)
Assess:
- Monitoring and observability
- Capacity planning
- Change management
- Incident response
- Documentation completeness

## Output Format

### Executive Summary
- Overall security posture
- Architecture maturity
- Production readiness score

### Critical Findings
For each finding:
- Severity: Critical / High / Medium / Low
- Category: Security / Architecture / Reliability / Maintainability
- OWASP/DORA/SOLID mapping
- Specific location in codebase
- Recommended fix with code example

### Quick Wins
- 10 highest-impact improvements with minimal effort

### Prioritized Roadmap
- Immediate (critical security)
- Short-term (architecture debt)
- Medium-term (reliability)
- Long-term (optimization)

## Rules

- Only report verifiable issues
- Map each finding to specific framework/principle
- Provide actionable fixes, not just flags
- Prioritize by actual risk, not theoretical
```

---

## Metadata

- **Source:** prompts.chat
- **Tags:** security, audit, owasp, solid, dora, sre
- **Models:** All
- **Version:** 1.0 (adapted)
