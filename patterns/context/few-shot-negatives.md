# Few-Shot Negatives Pattern

## Description
This pattern provides examples of both what the model SHOULD do and what it SHOULD NOT do, helping it better define the boundaries of acceptable output.

## Usage
Include pairs of positive and negative examples in the prompt.

```text
Example 1 (Good): The system correctly identified the issue and logged a warning.
Example 2 (Bad - Too informal): The system saw a problem and yelled about it.
Example 3 (Good): Process completed with 0 errors.
Example 4 (Bad - Contains emojis): Process completed!
```
