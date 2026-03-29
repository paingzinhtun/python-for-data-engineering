# Best Practices

## Python Habits Every Data Engineer Should Build

- Write small, testable functions
- Prefer explicit names over short clever ones
- Validate assumptions early
- Separate extraction, transformation, and loading logic
- Log meaningful events, not everything
- Use parameterized SQL
- Keep raw data separate from processed outputs
- Treat bad records intentionally instead of silently ignoring them
- Make reruns safe when possible

## Code Quality Rules

- Avoid giant scripts that mix many responsibilities
- Use `pathlib` for paths
- Keep configuration out of hard-coded constants when it may change by environment
- Add docstrings to reusable functions
- Write tests for transformation rules and quality checks
- Prefer readable loops and functions over compact one-liners when teaching
