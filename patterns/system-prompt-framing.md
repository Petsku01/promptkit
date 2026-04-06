# System Prompt Framing Pattern

## Description

Use the system message to set persistent rules, constraints, and behavior for the entire conversation.

## When to use

Building chatbots, assistants, or any multi-turn application where behavior must stay consistent.

## When to avoid

One-off tasks where a simple instruction is enough — system prompts add complexity.

## Template

```
[System message]
You are [role]. You follow these rules:
1. [Rule 1 — e.g., always respond in JSON]
2. [Rule 2 — e.g., never make up information]
3. [Rule 3 — e.g., ask clarifying questions before answering]
4. [Tone/style constraint]

[User message]
[The actual user query]
```

## Example

```
[System message]
You are a customer support agent for a SaaS analytics platform. You follow these rules:
1. Always be empathetic and professional.
2. Never promise features that don't exist — say "I'll pass this to our product team."
3. If the user describes a bug, ask for their browser, OS, and steps to reproduce.
4. Keep responses under 150 words.

[User message]
The dashboard has been loading for 5 minutes and I have a client presentation in 30 minutes. Help!
```

## Best practices

- Keep system prompts at the beginning of the conversation
- Use XML tags to delineate sections
- Include identity, instructions, examples, and context

## Tags

intermediate, system, chatbot, multi-turn
