# Education Prompts

Prompts for teaching, explaining, and tutoring.

## Browsing Prompts

```bash
promptkit search "education"
promptkit search "teacher"
```

## Available Prompts

| Prompt | Description |
|--------|-------------|
| math-teacher | Math tutoring |
| ai-writing-tutor | Writing improvement |
| debate-coach | Debate training |
| instructor-in-a-school | General instruction |
| life-coach | Life coaching |
| mathematical-history-teacher | Math history |
| philosopher | Philosophical discussion |
| public-speaking-coach | Speaking skills |
| spoken-english-teacher-and-improver | English practice |
| teacher-of-react-js | React.js instruction |
| motivational-coach | Motivation and goals |

## Example Usage

```python
from llm_promptkit import PromptBuilder

builder = PromptBuilder()
builder.persona("Experienced math teacher")
builder.pattern("chain-of-thought")
builder.task("Explain why negative times negative equals positive")
prompt = builder.build()
```