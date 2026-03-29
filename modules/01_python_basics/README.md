# Module 01: Python Foundations

## Learning Objectives

- Use variables, basic types, and operators
- Write conditionals, loops, and functions
- Understand input, output, and simple debugging
- Build readable beginner-safe scripts

## Concept Explanation

Python basics are the building blocks of data scripts. Even large ETL jobs still depend on clear functions, loop logic, conditional checks, and correct use of types like strings, integers, floats, and booleans.

## Why It Matters in Data Engineering

Data pipelines are full of small decisions:

- should this record be kept or rejected
- should this file be processed or skipped
- should this field become an integer or stay null

Those decisions are written with conditionals, loops, and functions.

## Hands-On Examples

```python
def should_process_file(file_size_bytes: int, extension: str) -> bool:
    return file_size_bytes > 0 and extension.lower() == ".csv"
```

```python
total_rows = 0
for file_name in ["sales.csv", "returns.csv"]:
    print(f"Processing {file_name}")
    total_rows += 1
```

## Practice Focus

- declare variables for pipeline settings
- use `if` statements for validation logic
- use loops to process multiple files
- write small functions that do one thing well

## Common Mistakes

- Reusing vague variable names like `x` or `data`
- Mixing string and numeric types without conversion
- Writing large scripts without functions
- Forgetting to test edge cases like empty input

## Summary

Python basics are not beginner-only knowledge. They are production fundamentals.

## Next Module Connection

Module 02 teaches the data structures you will use constantly for rows, fields, lookups, and unique values.
