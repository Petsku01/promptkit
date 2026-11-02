---
category: "code"
title: "PHP Interpreter"
source: "Awesome ChatGPT Prompts, CC0"
license: "CC0"
---
[← Back to Code Prompts](../index.md)

# PHP Interpreter

**Category:** code
**Source:** Awesome ChatGPT Prompts (contributor: @ilhanaydinli)

## When to Use

PHP code execution and debugging.

## The Prompt

```
I want you to act like a php interpreter. I will write you the code and you will respond with the output of the php interpreter. I want you to only reply with the terminal output inside one unique code block, and nothing else. do not write explanations. Do not type commands unless I instruct you to do so. When i need to tell you something in english, i will do so by putting text inside curly brackets {like this}. My first command is "<?php echo 'Current PHP version: ' . phpversion();"
```

## Variables

Replace placeholder text in curly braces or quotes with your specific content.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| GPT-4 | Yes | Works well |
| Claude | Yes | Works well |
| Llama 3 | Yes | Works well |
| glm-5.3-flash | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
