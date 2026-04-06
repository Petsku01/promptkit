# Fact-Check Pattern

## Description

Request the model to verify facts and distinguish between known information and speculation.

## When to use

When accuracy is critical and you need to prevent confident-sounding but incorrect information.

## When to avoid

Creative writing or brainstorming where factual accuracy is less important.

## Template

```
[Question or task requiring factual accuracy]

Important instructions:
1. Distinguish between **verified facts** and **inference/speculation**
2. If uncertain, say "I'm not sure" or "This requires verification"
3. Cite sources when possible
4. Flag any information that may be outdated
5. Avoid presenting opinions as facts

Format your response as:
**Verified**: [Confirmed facts]
**Likely**: [Reasonable inferences with caveats]
**Uncertain**: [Areas needing verification]
```

## Example

```
What are the current GDPR requirements for data retention?

Important instructions:
1. Distinguish between **verified facts** and **inference/speculation**
2. If uncertain, say "I'm not sure" or "This requires verification"
3. Cite sources when possible
4. Flag any information that may be outdated
5. Avoid presenting opinions as facts

Format your response as:
**Verified**: [Confirmed facts]
**Likely**: [Reasonable inferences with caveats]
**Uncertain**: [Areas needing verification]
```

## Tags

defensive, fact-check, accuracy, verification, safety
