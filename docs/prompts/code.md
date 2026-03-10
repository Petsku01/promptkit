# Code Prompts

Prompts for code review, development, and programming tasks.

## Available Prompts

| Prompt | Use Case |
|--------|----------|
| [brutal-reviewer](https://github.com/Petsku01/promptkit/blob/master/prompts/code/brutal-reviewer.md) | Harsh, thorough code review |
| [code-reviewer](https://github.com/Petsku01/promptkit/blob/master/prompts/code/code-reviewer.md) | Standard code review |
| [code-reviewer-extended](https://github.com/Petsku01/promptkit/blob/master/prompts/code/code-reviewer-extended.md) | Comprehensive review with structure |
| [senior-engineer](https://github.com/Petsku01/promptkit/blob/master/prompts/code/senior-engineer.md) | Senior dev perspective |
| [fullstack-software-developer](https://github.com/Petsku01/promptkit/blob/master/prompts/code/fullstack-software-developer.md) | Full-stack development |
| [senior-frontend-developer](https://github.com/Petsku01/promptkit/blob/master/prompts/code/senior-frontend-developer.md) | Frontend specialist |
| [python-interpreter](https://github.com/Petsku01/promptkit/blob/master/prompts/code/python-interpreter.md) | Python REPL simulation |
| [javascript-console](https://github.com/Petsku01/promptkit/blob/master/prompts/code/javascript-console.md) | JS console simulation |
| [sql-terminal](https://github.com/Petsku01/promptkit/blob/master/prompts/code/sql-terminal.md) | SQL terminal simulation |
| [linux-terminal](https://github.com/Petsku01/promptkit/blob/master/prompts/code/linux-terminal.md) | Linux shell simulation |
| [debugger-interactive](https://github.com/Petsku01/promptkit/blob/master/prompts/code/debugger-interactive.md) | Interactive debugging |
| [tdd-generator](https://github.com/Petsku01/promptkit/blob/master/prompts/code/tdd-generator.md) | Test-driven development |
| [machine-learning-engineer](https://github.com/Petsku01/promptkit/blob/master/prompts/code/machine-learning-engineer.md) | ML/AI development |
| [ethereum-developer](https://github.com/Petsku01/promptkit/blob/master/prompts/code/ethereum-developer.md) | Smart contract development |
| [it-architect](https://github.com/Petsku01/promptkit/blob/master/prompts/code/it-architect.md) | System architecture |
| [ux-ui-developer](https://github.com/Petsku01/promptkit/blob/master/prompts/code/ux-ui-developer.md) | UX/UI development |
| [software-quality-assurance-tester](https://github.com/Petsku01/promptkit/blob/master/prompts/code/software-quality-assurance-tester.md) | QA testing |
| [developer-relations-consultant](https://github.com/Petsku01/promptkit/blob/master/prompts/code/developer-relations-consultant.md) | DevRel consulting |

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
