# Code Prompts

Ready-to-use prompts for software development tasks.

## Browsing Prompts

```bash
# List all providers and models
promptkit prompts

# List code prompts
promptkit prompts --model code

# Search for a specific prompt
promptkit search "code review"
```

## Available Prompts

| Prompt | Description |
|--------|-------------|
| brutal-reviewer | Harsh, thorough code review |
| code-reviewer | Standard code review |
| code-reviewer-extended | Comprehensive review with structure |
| senior-engineer | Senior dev perspective |
| fullstack-software-developer | Full-stack development |
| senior-frontend-developer | Frontend specialist |
| python-interpreter | Python REPL simulation |
| javascript-console | JS console simulation |
| sql-terminal | SQL terminal simulation |
| linux-terminal | Linux shell simulation |
| debugger-interactive | Interactive debugging |
| tdd-generator | Test-driven development |
| machine-learning-engineer | ML/AI development |
| ethereum-developer | Smart contract development |
| it-architect | System architecture |
| ux-ui-developer | UX/UI development |
| software-quality-assurance-tester | QA testing |
| developer-relations-consultant | DevRel consulting |

## Example Usage

```python
from llm_promptkit import PromptBuilder

# Load a code prompt as system message
builder = PromptBuilder()
builder.pattern("senior-reviewer")
builder.task("Review this pull request")
builder.context(diff_text)
prompt = builder.build()
```