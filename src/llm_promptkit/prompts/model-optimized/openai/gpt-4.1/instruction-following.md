# GPT-4.1: Instruction Following

## Complex Multi-Step Task
```
Complete this task. Follow ALL instructions precisely.

Task: [describe task]

Steps:
1. [step 1 with exact requirements]
2. [step 2 with exact requirements]
3. [step 3 with exact requirements]
4. [step 4 with exact requirements]

Output format: [describe exact format]
Constraints:
- [constraint 1]
- [constraint 2]
- [constraint 3]

Do not skip any step. Do not add content beyond what is requested.
```

## Format-Specific Output
```
Generate [content type] with this exact structure:

[Show the exact template/structure with placeholders]

Rules:
- [formatting rule 1]
- [formatting rule 2]
- [negative constraint: do NOT do X]

Example of correct output:
[show a short example]
```

## Checklist Execution
```
Execute each item in this checklist. Mark each as done.

- [ ] [task 1]: [requirements]
- [ ] [task 2]: [requirements]
- [ ] [task 3]: [requirements]
- [ ] [task 4]: [requirements]

After completing all items, provide a summary confirming each was done.
If any item cannot be completed, explain why — do not skip silently.
```

## Role + Constraint Prompt
```
You are [role description with expertise].

Your task: [what to do]

You MUST:
- [positive constraint 1]
- [positive constraint 2]

You MUST NOT:
- [negative constraint 1]
- [negative constraint 2]

Output: [exact format specification]
```

---
**GPT-4.1 Instruction Following Tips:**
- GPT-4.1's standout improvement over GPT-4o — excels at precise instruction adherence
- Use explicit "MUST" and "MUST NOT" constraints for best results
- Number steps and ask it to complete each in order
- Specify negative constraints ("do not add X") — it respects these well
- Use `developer` role for system-level behavioral rules
- Give an example of desired output format for complex formatting requirements