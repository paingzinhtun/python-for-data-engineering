# Module 11: Python Project Structure for Data Engineering

## Learning Objectives

- Organize code using a clear `src` layout
- Separate config, docs, tests, datasets, and projects
- Keep notebooks separate from reusable pipeline code
- Build a structure that scales beyond one script

## Concept Explanation

A messy folder structure slows teams down. As projects grow, code organization starts affecting onboarding, testing, debugging, and deployment.

## Why It Matters in Data Engineering

Pipelines usually expand over time. A clean structure helps you add new sources, transformations, tests, and environments without constant rewrites.

## Recommended Layout

- `src/` for reusable code
- `tests/` for automated checks
- `datasets/` for sample or mock data
- `projects/` for guided implementations
- `docs/` for setup, architecture, and learning material

## Common Mistakes

- Mixing notebooks and production code
- Keeping large scripts at repo root
- Storing config values directly in many files
- No separation between raw and processed data

## Summary

Good structure is a force multiplier for learning and maintainability.

## Next Module Connection

Module 12 covers patterns you will see repeatedly in real-world pipelines.
