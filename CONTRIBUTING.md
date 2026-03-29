# Contributing Guide

Thank you for helping improve this repository.

## What Contributions Are Welcome

- Fix typos, broken examples, or unclear explanations
- Improve exercises or solution clarity
- Add realistic sample datasets
- Improve tests for starter scripts
- Suggest better project prompts or interview questions
- Improve setup instructions across operating systems

## Repo Standards

- Prefer clarity over cleverness
- Keep examples beginner-friendly but realistic
- Connect Python concepts back to Data Engineering use cases
- Use descriptive names and small functions
- Document assumptions in project and pipeline examples
- Add tests when introducing non-trivial Python logic

## Local Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest
```

## Content Style Guide

- Use simple, direct language
- Explain both the `what` and the `why`
- Include practical examples
- Avoid overusing pandas when basic Python is the teaching goal
- Keep markdown skimmable with short sections and lists
- Mark starter templates clearly so learners know what they must complete

## Pull Request Checklist

- The change is scoped and understandable
- Lesson content remains consistent with the learning path
- Examples run or are obviously syntactically correct
- New code includes tests where appropriate
- File names and headings follow the existing structure
- Links between modules or docs still work

## Issues

When opening an issue, please include:

- the file path
- the problem you found
- expected behavior or suggested improvement
- screenshots or output only if helpful

## Good First Contribution Ideas

- Add one more exercise to an existing module
- Improve glossary definitions
- Add data quality edge cases to a project
- Expand the setup guide for macOS or Linux
- Add a mini test case for a transformation utility
