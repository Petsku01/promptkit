[← Back to Model-Optimized Few-Shot](../index.md)

# Few-Shot: Generointi

## Product Description

```
Write a compelling product description.

Product: Wireless Earbuds
Features: 24h battery, noise canceling, waterproof
Description: Experience audio freedom with our premium wireless earbuds. With 24-hour battery life, industry-leading noise cancellation, and full waterproof protection, these earbuds keep up with your lifestyle. Whether you're at the gym or in the office, enjoy crystal-clear sound without limits.

Product: Smart Watch
Features: heart rate monitor, GPS, 7-day battery
Description: Your health companion on your wrist. Track your heart rate in real-time, navigate with built-in GPS, and enjoy a full week of use on a single charge. This smartwatch combines style with substance, helping you stay connected and healthy.

Product: [PRODUCT]
Features: [FEATURES]
Description:
```

## Email Subject Lines

```
Generate engaging email subject lines.

Topic: New product launch announcement
Subjects:
-  It's Finally Here: Introducing [Product Name]
- You're the first to know: Our biggest launch yet
- The wait is over. Meet your new favorite [product].

Topic: Abandoned cart reminder
Subjects:
- Did you forget something? Your cart misses you
- Still thinking it over? Here's 10% off
- Your items are waiting (and selling fast!)

Topic: Monthly newsletter
Subjects:
- This Month's Top Picks (Curated Just for You)
- 5 Things You Need to Know This [Month]
- Your monthly dose of [topic] inspiration

Topic: [YOUR TOPIC]
Subjects:
```

## Code Documentation

```
Generate docstring documentation.

Function: def calculate_tax(income, rate, deductions=[]):
Docstring:
"""
Calculate tax owed based on income, rate, and deductions.

Args:
    income (float): Total annual income in dollars
    rate (float): Tax rate as decimal (e.g., 0.25 for 25%)
    deductions (list): Optional list of deduction amounts

Returns:
    float: Calculated tax amount after deductions

Example:
    >>> calculate_tax(100000, 0.25, [5000, 2000])
    23250.0
"""

Function: def merge_sorted_lists(list1, list2):
Docstring:
"""
Merge two sorted lists into a single sorted list.

Args:
    list1 (list): First sorted list
    list2 (list): Second sorted list

Returns:
    list: Merged and sorted list containing all elements

Time Complexity: O(n + m) where n, m are list lengths

Example:
    >>> merge_sorted_lists([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
"""

Function: [YOUR FUNCTION]
Docstring:
```

## Test Cases

```
Generate test cases for this function.

Function: def is_palindrome(s: str) -> bool
Tests:
- is_palindrome("racecar") == True  # basic palindrome
- is_palindrome("hello") == False   # not a palindrome
- is_palindrome("A man a plan a canal Panama") == True  # with spaces
- is_palindrome("") == True         # empty string
- is_palindrome("a") == True        # single char
- is_palindrome("RaceCar") == True  # case insensitive

Function: def factorial(n: int) -> int
Tests:
- factorial(0) == 1                 # base case
- factorial(1) == 1                 # base case
- factorial(5) == 120               # normal case
- factorial(10) == 3628800          # larger number
- factorial(-1) raises ValueError   # negative input

Function: [YOUR FUNCTION]
Tests:
```

## Commit Messages

```
Generate conventional commit messages.

Changes: Fixed login button not working on mobile
Commit: fix(auth): resolve mobile login button click handler

Changes: Added dark mode support to settings page
Commit: feat(settings): add dark mode toggle and theme persistence

Changes: Improved database query performance by 50%
Commit: perf(db): optimize user query with proper indexing

Changes: Updated README with installation instructions
Commit: docs: add installation guide and prerequisites

Changes: Renamed UserService to UserManager for clarity
Commit: refactor(services): rename UserService to UserManager

Changes: [YOUR CHANGES]
Commit:
```
