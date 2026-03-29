# Module 03: Intermediate Python

## Learning Objectives

- Use comprehensions, `args`, `kwargs`, `lambda`, and sorting tools
- Organize code into modules and imports
- Handle errors with `try` and `except`
- Understand when simple OOP helps data workflows

## Concept Explanation

Intermediate Python is where scripts become reusable. Instead of writing everything inline, you start grouping logic into modules, handling failures intentionally, and creating abstractions that improve readability.

## Why It Matters in Data Engineering

Pipelines fail for predictable reasons: missing files, bad types, bad JSON, database errors. Good intermediate Python lets you catch expected problems and keep code maintainable as the workflow grows.

## Hands-On Examples

```python
def parse_int(value: str, default: int = 0) -> int:
    try:
        return int(value)
    except ValueError:
        return default
```

```python
valid_rows = [row for row in rows if row.get("status") == "active"]
```

## When OOP Is Useful

Basic classes can help when you want to group related configuration or pipeline behavior, but many beginner pipelines are clearer with plain functions. Start with functions first and use classes only when they improve structure.

## Common Mistakes

- Using comprehensions when a normal loop would be easier to read
- Catching broad exceptions without logging context
- Creating classes too early for tiny scripts
- Letting imports become circular or messy

## Summary

Intermediate Python helps you move from practice snippets to small, structured tools.

## Next Module Connection

Module 04 applies these skills to files, paths, encodings, and ingestion workflows.
