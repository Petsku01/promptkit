# Template-Based Prompting Pattern

## Description

Create reusable prompt templates with placeholders for dynamic content.

## When to use

When you have repetitive tasks with similar structure but different inputs (email generation, report templates, form filling).

## When to avoid

One-off tasks where creating a template is overhead.

## Template

```
You are a [ROLE] specializing in [DOMAIN].

Your task is to [TASK_DESCRIPTION].

Use the following template for your response:

---
[TEMPLATE_STRUCTURE_WITH_PLACEHOLDERS]
---

Input data:
{{INPUT_DATA}}

Requirements:
- [Requirement 1]
- [Requirement 2]
```

## Example

```
You are a customer success manager specializing in SaaS onboarding.

Your task is to write personalized welcome emails for new users.

Use the following template for your response:

---
Subject: Welcome to {{COMPANY_NAME}}, {{USER_NAME}}! 🎉

Hi {{USER_NAME}},

Welcome to {{COMPANY_NAME}}! We're thrilled to have {{COMPANY_TYPE}} like yours on board.

Based on your signup, you're most interested in {{PRIMARY_USE_CASE}}. Here's how to get started:

1. {{FIRST_STEP}}
2. {{SECOND_STEP}}
3. {{THIRD_STEP}}

Need help? Reply to this email or book a call: {{CALENDAR_LINK}}

Best,
{{SENDER_NAME}}
---

Input data:
{{INPUT_DATA}}

Requirements:
- Keep tone warm and professional
- Include at least one specific value proposition
- Keep under 250 words
```

## Tags

template, reusable, placeholders, automation
