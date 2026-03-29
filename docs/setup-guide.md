# Setup Guide

## Tools You Need

- Python 3.10 or newer
- Git
- VS Code or another editor
- A terminal

Optional later:

- DB Browser for SQLite
- Postman or Bruno for inspecting APIs

## Verify Python

```bash
python --version
```

If that does not work, install Python from the official website and ensure it is added to your path.

## Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Recommended VS Code Extensions

- Python
- Pylance
- Markdown All in One

## Repo Usage Pattern

- read the module lesson
- run example code
- solve the exercises
- inspect the separate solutions
- complete the mini-project starter tasks
- add tests when you refactor

## Running Tests

```bash
pytest
```

## Common Beginner Problems

### The virtual environment is not active
If imports fail or the wrong Python version appears, confirm the environment is activated.

### File path errors
Use `pathlib.Path` and avoid hard-coded absolute paths when possible.

### Encoding issues
When reading text files, explicitly use `encoding="utf-8"` unless you know you need something else.

### Package not found
Re-run `pip install -r requirements.txt` inside the active virtual environment.
