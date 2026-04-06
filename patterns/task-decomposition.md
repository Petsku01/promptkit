# Task Decomposition Pattern

## Description

Break a complex task into subtasks, solve each one, then combine. Reduces errors on hard problems.

## When to use

Multi-step workflows, research tasks, or anything where a single prompt would produce shallow results.

## When to avoid

Simple tasks that don't benefit from decomposition — it adds overhead.

## Template

```
I need to [complex goal]. Let's break this into steps:

Step 1: [First subtask]
Step 2: [Second subtask, building on Step 1]
Step 3: [Third subtask, building on Step 2]
Step 4: [Synthesis / final output]

Start with Step 1.
```

## Example

```
I need to write a competitive analysis of the top 5 project management tools. Let's break this into steps:

Step 1: List the top 5 tools by market share and briefly describe each.
Step 2: For each tool, identify 3 strengths and 3 weaknesses.
Step 3: Create a comparison matrix across pricing, features, integrations, and user ratings.
Step 4: Write a 200-word executive summary with a recommendation.

Start with Step 1.
```

## Variations

- **Map-reduce:** Break into pieces, process in parallel, combine results
- **Tree of Thought:** Explore multiple paths, pick best
- **Recursive:** Decompose until tasks are atomic

## Tags

advanced, planning, workflow, complex-tasks
