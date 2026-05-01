[← Back to Model-Optimized Use-Cases](../index.md)

# Use Case: Customer Support

## Support Ticket Classifier

```
Classify this support ticket:

Ticket: [ticket text]

Categories:
- billing: Payment, invoices, refunds
- technical: Bugs, errors, how-to
- account: Login, settings, profile
- shipping: Delivery, tracking, returns
- general: Other inquiries

Output:
{
  "category": "[category]",
  "priority": "[low/medium/high/urgent]",
  "sentiment": "[positive/neutral/negative/angry]",
  "suggested_team": "[team name]"
}
```

## Auto-Response Generator

```
Generate a customer support response:

Customer message: [message]
Account status: [active/pending/cancelled]
Previous interactions: [summary or "none"]

Guidelines:
- Be empathetic and professional
- Address the specific issue
- Provide clear next steps
- Include relevant links/resources
- Sign off with agent name placeholder

Response:
```

## Escalation Detector

```
Should this conversation be escalated to a human?

Conversation:
[conversation history]

Check for:
□ Customer explicitly requested human
□ Multiple failed resolution attempts
□ Legal/compliance mentions
□ Threats (legal action, social media)
□ High-value customer signals
□ Complex issue beyond FAQ

Decision: [continue AI / escalate]
Reason: [explanation]
Suggested handoff message: [if escalating]
```

## FAQ Matcher

```
Find the best FAQ match:

Customer question: [question]

Available FAQs:
1. [FAQ title 1]: [summary]
2. [FAQ title 2]: [summary]
3. [FAQ title 3]: [summary]
...

Match:
- Best FAQ: [number or "no match"]
- Confidence: [high/medium/low/none]
- Adapted answer: [FAQ content customized to question]
```

## Sentiment-Aware Response

```
Respond to this customer considering their emotional state:

Message: [customer message]
Detected sentiment: [sentiment]

Response strategy:
- If angry: Acknowledge frustration first, then solve
- If confused: Be extra clear and simple
- If happy: Match enthusiasm, suggest upgrades
- If neutral: Be efficient and helpful

Generate appropriate response:
```

## Issue Summary

```
Summarize this support conversation:

[conversation transcript]

Summary format:
- Issue: [one sentence description]
- Customer goal: [what they wanted]
- Resolution: [how it was resolved / current status]
- Action items: [any pending tasks]
- Tags: [relevant categories]
```

## Response Tone Adjuster

```
Rewrite this response to be more [tone]:

Original: [response]
Desired tone: [empathetic/professional/casual/urgent]

Rewritten:
```
