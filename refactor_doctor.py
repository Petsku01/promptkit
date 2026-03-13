import re

with open("/home/ette/.openclaw/workspace/promptkit/src/llm_promptkit/cli.py", "r") as f:
    content = f.read()

# 1. Add import re and Constants
imports = """from typing import List, Optional, Tuple

import re

# Doctor Command Constants
VAGUE_PHRASES = ["make it good", "do it well", "as best as you can", "stuff", "things"]
ROLE_PHRASES = ["you are a", "role:", "persona:", "act as", "system:"]
VERBOSE_PHRASES = ["please could you", "i would like you to", "if you don't mind", "can you please"]
FORMAT_PHRASES = ["format", "json", "markdown", "output:", "structure", "return as"]
EXAMPLE_PHRASES = ["example:", "e.g.", "for instance", "few-shot", "here is an example"]
"""

content = content.replace("from typing import List, Optional, Tuple", imports)


old_doctor = """def doctor_command(args):
    \"\"\"Analyze a prompt for common issues.\"\"\"
    from pathlib import Path
    
    # Get text to analyze
    if Path(args.target).exists():
        text = Path(args.target).read_text().lower()
        console.print(f"[bold]Analyzing file:[/bold] {args.target}\\n")
    else:
        text = args.target.lower()
        console.print("[bold]Analyzing text prompt...[/bold]\\n")
        
    issues = []
    
    # 1. Vague/ambiguous
    vague_phrases = ["make it good", "do it well", "as best as you can", "stuff", "things"]
    for phrase in vague_phrases:
        if phrase in text:
            issues.append(("[yellow]Warning[/yellow]", "Vague or ambiguous instructions detected.", f"Found '{phrase}'. Be more specific."))
            
    # 2. Missing context/role
    role_phrases = ["you are a", "role:", "persona:", "act as", "system:"]
    if not any(phrase in text for phrase in role_phrases):
        issues.append(("[red]Suggestion[/red]", "Missing context or role definition.", "Add a persona or role to ground the LLM's responses (e.g., 'You are an expert...')."))
        
    # 3. Token inefficiency
    verbose_phrases = ["please could you", "i would like you to", "if you don't mind", "can you please"]
    for phrase in verbose_phrases:
        if phrase in text:
            issues.append(("[blue]Info[/blue]", "Token inefficiency detected.", f"Found verbose phrasing '{phrase}'. Use direct commands to save tokens."))
            
    # 4. Missing output format
    format_phrases = ["format", "json", "markdown", "output:", "structure", "return as"]
    if not any(phrase in text for phrase in format_phrases):
        issues.append(("[yellow]Warning[/yellow]", "Missing output format specification.", "Specify how you want the output formatted (e.g., 'Output as JSON', 'Use markdown headers')."))
        
    # 5. Lack of examples
    example_phrases = ["example:", "e.g.", "for instance", "few-shot", "here is an example"]
    if not any(phrase in text for phrase in example_phrases):
        issues.append(("[blue]Info[/blue]", "Lack of examples (few-shot opportunities).", "Providing examples can significantly improve output quality and consistency."))"""

new_doctor = """def doctor_command(args):
    \"\"\"Analyze a prompt for common issues.\"\"\"
    from pathlib import Path
    
    # Get text to analyze
    if Path(args.target).exists():
        text = Path(args.target).read_text().lower()
        console.print(f"[bold]Analyzing file:[/bold] {args.target}\\n")
    else:
        text = args.target.lower()
        console.print("[bold]Analyzing text prompt...[/bold]\\n")
        
    issues = []
    
    if len(text.strip()) < 20:
        issues.append(("[yellow]Warning[/yellow]", "Prompt is very short.", "Prompts under 20 characters often lack sufficient detail."))
    
    # 1. Vague/ambiguous
    for phrase in VAGUE_PHRASES:
        if re.search(rf"\\b{re.escape(phrase)}\\b", text, re.IGNORECASE):
            issues.append(("[yellow]Warning[/yellow]", "Vague or ambiguous instructions detected.", f"Found '{phrase}'. Be more specific."))
            
    # 2. Missing context/role
    if not any(re.search(rf"\\b{re.escape(phrase)}\\b", text, re.IGNORECASE) for phrase in ROLE_PHRASES):
        issues.append(("[red]Suggestion[/red]", "Missing context or role definition.", "Add a persona or role to ground the LLM's responses (e.g., 'You are an expert...')."))
        
    # 3. Token inefficiency
    for phrase in VERBOSE_PHRASES:
        if re.search(rf"\\b{re.escape(phrase)}\\b", text, re.IGNORECASE):
            issues.append(("[blue]Info[/blue]", "Token inefficiency detected.", f"Found verbose phrasing '{phrase}'. Use direct commands to save tokens."))
            
    # 4. Missing output format
    if not any(re.search(rf"\\b{re.escape(phrase)}\\b", text, re.IGNORECASE) for phrase in FORMAT_PHRASES):
        issues.append(("[yellow]Warning[/yellow]", "Missing output format specification.", "Specify how you want the output formatted (e.g., 'Output as JSON', 'Use markdown headers')."))
        
    # 5. Lack of examples
    if not any(re.search(rf"\\b{re.escape(phrase)}\\b", text, re.IGNORECASE) for phrase in EXAMPLE_PHRASES):
        issues.append(("[blue]Info[/blue]", "Lack of examples (few-shot opportunities).", "Providing examples can significantly improve output quality and consistency."))"""

content = content.replace(old_doctor, new_doctor)

# Fix list_patterns in main
old_main_cond = """    elif args.command == "doctor":
        doctor_command(args)
        list_patterns()"""
new_main_cond = """    elif args.command == "doctor":
        doctor_command(args)"""

content = content.replace(old_main_cond, new_main_cond)

with open("/home/ette/.openclaw/workspace/promptkit/src/llm_promptkit/cli.py", "w") as f:
    f.write(content)
