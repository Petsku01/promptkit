# Professional Prompts

Prompts for business, consulting, and professional writing.

## Browsing Prompts

```bash
promptkit search "professional"
promptkit search "business"
```

## Available Prompts

| Prompt | Description |
|--------|-------------|
| career-coach | Career guidance |
| career-counselor | Career counseling |
| job-interviewer | Interview practice |
| legal-advisor | Legal guidance |
| product-manager | Product management |
| project-manager | Project management |
| recruiter | Hiring and recruitment |
| social-media-manager | Social media strategy |
| startup-idea-generator | Startup ideation |
| startup-tech-lawyer | Startup legal advice |
| web-design-consultant | Web design consulting |

## Example Usage

```python
from llm_promptkit import PromptBuilder

builder = PromptBuilder()
builder.persona("Product manager")
builder.pattern("decomposition")
builder.task("Break down this feature request into user stories")
prompt = builder.build()
```