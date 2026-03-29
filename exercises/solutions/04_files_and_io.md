# Module 04 Solutions

## Beginner

```python
from pathlib import Path

path = Path("datasets/sample_inputs/readme.txt")
with path.open("r", encoding="utf-8") as file_handle:
    for line in file_handle:
        print(line.strip())
```

## Intermediate
Use `csv.DictReader` and `Path.glob("*.csv")`.

## Applied
Validate `path.exists()`, `path.suffix == ".csv"`, and `path.stat().st_size > 0`.

## Scenario
Scan the folder, validate each file, route good files to processing, and record bad-file reasons in a log or report.
