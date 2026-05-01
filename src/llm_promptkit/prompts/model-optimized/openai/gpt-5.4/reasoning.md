# GPT-5.4: Reasoning

## Deep Investigation
```
Investigate this problem thoroughly:

Context: [domain/situation]
Problem: [what needs to be understood]

Approach:
1. Identify all relevant variables and their relationships
2. Consider alternative explanations
3. Check for confounding factors
4. Test each hypothesis against available evidence
5. Identify what evidence would distinguish between remaining hypotheses

Conclude with:
- Most likely explanation (with confidence level)
- Key uncertainties that remain
- What to investigate next
```

## Multi-Step Decision Analysis
```
Help me make a complex decision:

Decision: [what needs to be decided]
Stakeholders: [who is affected]
Constraints: [budget, time, technical, etc.]
Options:
- Option A: [description]
- Option B: [description]
- Option C: [description]

For each option, analyze:
1. Short-term impact (1-3 months)
2. Long-term impact (1-3 years)
3. Reversibility (how hard to undo?)
4. Risk profile (what could go wrong?)
5. Hidden costs or side effects

Recommendation with reasoning.
```

## Technical Root Cause Analysis
```
Perform a formal RCA for this incident:

Incident: [describe]
Timeline: [what happened when]
Impact: [users affected, duration, data loss, etc.]

Analysis framework:
1. **What happened?** (chronological events)
2. **Why did it happen?** (5 Whys or fault tree)
3. **Why wasn't it prevented?** (defenses that failed)
4. **How do we fix it?** (immediate remediation)
5. **How do we prevent recurrence?** (systemic changes)

Classify contributing factors as: human error, process gap, technical failure, or design flaw.
```

## Research Synthesis
```
Synthesize findings from multiple sources on: [topic]

Sources:
- [Source 1]: [key finding]
- [Source 2]: [key finding]
- [Source 3]: [key finding]

Tasks:
1. Identify areas of agreement across sources
2. Identify contradictions and possible explanations
3. Evaluate source reliability and methodology
4. Note gaps in current evidence
5. Propose a reconciled understanding
6. Suggest what further research is needed

Be explicit about confidence levels and remaining uncertainties.
```

## Strategic Planning
```
Develop a strategic plan for: [objective]

Current state:
- [constraint 1]
- [constraint 2]

Desired state:
- [goal 1]
- [goal 2]

Timeline: [timeframe]

Provide:
1. Key milestones with dependencies
2. Resource requirements per phase
3. Critical path analysis
4. Risk register (likelihood × impact)
5. Decision points (where to reassess)
6. Success metrics for each phase

Flag any assumptions that need validation.
```

---
**GPT-5.4 Reasoning Tips:**
- Use extended thinking mode for complex multi-step reasoning
- Explicitly ask for confidence levels and uncertainty acknowledgment
- Can maintain reasoning chains across very long contexts
- Excellent at identifying hidden assumptions and biases
- Benefits from structured analysis frameworks (5 Whys, SWOT, etc.)