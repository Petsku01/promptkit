[← Back to Model-Optimized Anthropic](../index.md)

# Claude Opus 4.7: Analysis

## High-Resolution Visual Analysis
```
Analyze this image in detail:

[Attach image up to 3.75 megapixels]

Analysis tasks:
1. Describe all visible elements with spatial references
2. Identify any text, code, or data in the image
3. For UI screenshots: layout, components, accessibility issues
4. For diagrams: nodes, connections, data flow direction
5. For documents: structure, key data points, anomalies

Extract any actionable information.
Note any elements that are ambiguous or unclear.
```

## Comprehensive System Audit
```
Audit this system across all dimensions:

System: [name and description]
Documentation: [paste or reference]

Audit areas:
1. **Architecture**: Coupling, cohesion, bounded contexts
2. **Performance**: Latency, throughput, resource usage
3. **Reliability**: SPOFs, recovery time, data integrity
4. **Security**: Attack surface, auth model, data classification
5. **Observability**: Logging, metrics, tracing, alerting
6. **Operability**: Deployment, rollback, runbooks
7. **Compliance**: Data handling, access controls, audit trail

For each area:
- Current state: [✓/✗/partial]
- Risk level: critical / high / medium / low
- Key finding
- Recommended action

Executive summary: 3-5 bullet points for leadership.
```

## Codebase Health Assessment
```
Assess the health of this codebase:

Stats: [LOC, file count, age, languages]
Structure: [paste file tree or describe]

Evaluate:
1. Code quality: duplication, complexity, naming
2. Test health: coverage, flakiness, quality of assertions
3. Dependency health: outdated, vulnerable, abandoned
4. Architecture: modularity, abstraction quality
5. Documentation: README, API docs, comments
6. CI/CD: build time, test reliability, deploy confidence

Output:
- Health score: X/100
- Top 3 risks (what could kill the project)
- Top 3 opportunities (what would add most value)
- Prioritized improvement backlog
```

## Competitive Product Analysis
```
Analyze these competing products:

Products:
- [Product A]: [brief description]
- [Product B]: [brief description]
- [Product C]: [brief description]

Compare across dimensions:
| Dimension | A | B | C |
|-----------|---|---|---|
| Core features | | | |
| UX quality | | | |
| Performance | | | |
| Pricing model | | | |
| Integration | | | |
| Support | | | |

Strategic analysis:
- Category leader and why
- Underserved segments
- Key differentiators per product
- Market gaps and opportunities
```

---
**Claude Opus 4.7 Analysis Tips:**
- Unmatched vision capabilities — can analyze images up to 3.75 megapixels
- Excellent at extracting details from dense screenshots and diagrams
- Takes instructions literally — provide exact output format you want
- Self-verifies analysis before responding
- Produces higher-quality professional output: docs, slides, interfaces
- Use structured rubrics and scoring for reproducible analysis
- Ask it to flag assumptions and uncertainties explicitly