[← Back to Model-Optimized Safety](../index.md)

# Safety: Content Moderation

## Basic Content Check

```
Analyze this content for policy violations:

Content: [content to check]

Check for:
□ Hate speech
□ Violence/threats
□ Sexual content
□ Self-harm content
□ Harassment
□ Illegal activities
□ Misinformation

Result:
- Safe: [yes/no]
- Violations: [list if any]
- Severity: [low/medium/high]
- Action: [allow/flag/block]
```

## Multi-Category Classification

```
Classify this content into safety categories:

[content]

Categories (rate 0-1 probability):
- hate: [0.0-1.0]
- violence: [0.0-1.0]
- sexual: [0.0-1.0]
- harassment: [0.0-1.0]
- self_harm: [0.0-1.0]
- dangerous: [0.0-1.0]

Flagged (>0.5): [list categories]
Recommended action: [allow/review/block]
```

## Context-Aware Moderation

```
Moderate this content considering context:

Content: [content]
Context: [where/how it will be used]
Audience: [who will see it]

Analysis:
1. Content in isolation: [assessment]
2. Content in context: [assessment]
3. Audience considerations: [assessment]

Final decision: [allow/modify/block]
Reasoning: [explanation]
```

## Toxicity Detection

```
Analyze toxicity level:

Text: [text]

Dimensions:
- Insult: [none/mild/severe]
- Profanity: [none/mild/severe]
- Threat: [none/implied/explicit]
- Identity attack: [none/mild/severe]

Overall toxicity: [0-100%]
Suggested response: [engage/caution/disengage]
```

## Child Safety

```
Is this content appropriate for children?

Content: [content]
Target age: [age range]

Check:
□ Age-appropriate language
□ No mature themes
□ No dangerous instructions
□ No contact solicitation
□ Educational value (if applicable)

Verdict: [appropriate/not appropriate]
Concerns: [specific issues if any]
```

## Fact-Check Flag

```
Check for potential misinformation:

Claim: [claim or content]

Analysis:
1. Is this a factual claim? [yes/no/opinion]
2. Verifiability: [easily verified/hard to verify/unverifiable]
3. Red flags: [sensational language/no sources/contradicts known facts]
4. Confidence: [likely true/uncertain/likely false]

Recommendation: [pass/flag for review/label as disputed]
```
