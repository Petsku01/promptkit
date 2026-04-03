# Expert Persona / Role Prompting

**Category:** reasoning
**Source:** Best practices

## When to Use

Elevating the quality, tone, and technical depth of the response.

## The Prompt

```
Act as a [ROLE] with [YEARS] years of experience in [DOMAIN]. You are known for your rigorous attention to [FOCUS_AREAS].

[Your task or question]
```

## Example

```
Act as a Principal Staff Software Engineer with 20 years of experience in distributed systems and high-frequency trading. You are known for your rigorous attention to performance, security, and edge cases. 

Review the following system architecture and provide feedback:
[Insert architecture]
```

## How It Works

By activating the latent space associated with "Principal Engineer" or "Expert," the model shifts its probability distribution toward higher-quality, more technical, and nuanced terminology.

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `[ROLE]` | The expert role | `Security Consultant` |
| `[YEARS]` | Years of experience | `15` |
| `[DOMAIN]` | Area of expertise | `penetration testing` |

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| GPT-4 | Yes | Excellent |
| Claude | Yes | Excellent |
| Llama 3 | Yes | Good |
