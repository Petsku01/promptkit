# Code Prompts

Prompts for code review, development, and programming tasks.

## Available Prompts

| Prompt | Use Case |
|--------|----------|
| [senior-engineer](https://github.com/Petsku01/promptkit/blob/master/prompts/code/senior-engineer.md) | Senior dev perspective |
| [brutal-reviewer](https://github.com/Petsku01/promptkit/blob/master/prompts/code/brutal-reviewer.md) | Harsh, thorough code review |
| [code-reviewer](https://github.com/Petsku01/promptkit/blob/master/prompts/code/code-reviewer.md) | Standard code review |
| [code-reviewer-extended](https://github.com/Petsku01/promptkit/blob/master/prompts/code/code-reviewer-extended.md) | Comprehensive review with structure |
| [tdd-generator](https://github.com/Petsku01/promptkit/blob/master/prompts/code/tdd-generator.md) | Test-driven development |
| [fullstack-software-developer](https://github.com/Petsku01/promptkit/blob/master/prompts/code/fullstack-software-developer.md) | Full-stack development |
| [senior-frontend-developer](https://github.com/Petsku01/promptkit/blob/master/prompts/code/senior-frontend-developer.md) | Frontend specialist |

## Example Usage

```python
from llm_promptkit import PromptBuilder

# Load a code prompt as system message
with open("prompts/code/senior-engineer.md") as f:
    system_prompt = f.read()

prompt = (PromptBuilder()
    .system(system_prompt)
    .task("Review this pull request")
    .context(pr_diff)
    .build())
```
