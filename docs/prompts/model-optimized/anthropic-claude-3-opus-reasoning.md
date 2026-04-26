[← Back to Model-Optimized Prompts](../index.md)

# Claude Opus: Complex Reasoning

## Multi-Step Problem Solving
```xml
<task>
Solve this complex problem with full reasoning transparency.
</task>

<problem>
[describe problem]
</problem>

<methodology>
1. **Problem Decomposition**: Break into sub-problems
2. **Assumption Audit**: List and examine all assumptions
3. **Approach Selection**: Consider multiple methods, justify choice
4. **Step-by-Step Execution**: Show all work
5. **Verification**: Check answer through different method
6. **Edge Cases**: Consider where solution might fail
7. **Confidence Assessment**: Rate certainty of conclusion
</methodology>
```

## Philosophical Analysis
```xml
<task>
Examine this question with philosophical rigor.
</task>

<question>
[pose question]
</question>

<framework>
1. **Clarify Terms**: Define key concepts precisely
2. **Historical Context**: How has this been addressed before
3. **Major Positions**: Steel-man competing viewpoints
4. **Arguments**: Strongest cases for each position
5. **Objections**: Key criticisms and responses
6. **Synthesis**: Your reasoned position
7. **Remaining Uncertainties**: What cannot be resolved
</framework>
```

## Causal Analysis
```xml
<task>
Trace the causal chain of this phenomenon.
</task>

<phenomenon>
[describe what you want to understand]
</phenomenon>

<analysis>
1. **Proximate Causes**: Immediate triggers
2. **Distal Causes**: Deeper root causes
3. **Contributing Factors**: Necessary but not sufficient conditions
4. **Feedback Loops**: Self-reinforcing dynamics
5. **Counterfactuals**: What would change the outcome
6. **Causal Diagram**: Map the relationships
7. **Intervention Points**: Where could change happen
</analysis>
```
