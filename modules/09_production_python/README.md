# Module 09: Production-Oriented Python Skills

## Learning Objectives

- Add logging and configuration
- Use environment variables and CLI arguments
- Write tests with `pytest`
- Design better exceptions and simple retry patterns

## Concept Explanation

A script that works once is not the same as a maintainable pipeline. Production-oriented Python makes behavior observable, configurable, testable, and easier to debug.

## Why It Matters in Data Engineering

Pipelines run repeatedly. Other people will read your code, operate it, extend it, and troubleshoot it. Production skills reduce fragility and confusion.

## Hands-On Examples

```python
import logging

logger = logging.getLogger(__name__)
logger.info("Starting sales pipeline")
```

## Professional Habits

- log row counts and important state changes
- keep secrets out of source code
- test transformation rules
- refactor repeated logic into utilities

## Common Mistakes

- Using `print` everywhere instead of logging
- Hard-coding file paths or credentials
- Writing tests only after code becomes painful
- Catching exceptions without enough context

## Summary

Production Python is about code that other people can trust.

## Next Module Connection

Module 10 adds the scale and performance mindset needed for larger workloads.
