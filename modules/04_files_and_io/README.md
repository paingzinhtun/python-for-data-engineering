# Module 04: Working with Files

## Learning Objectives

- Read and write text, CSV, and JSON files
- Use `pathlib` for safe path handling
- Traverse directories and validate files
- Understand encoding and compression basics

## Concept Explanation

Many data pipelines begin with files. Vendor drops, exports, logs, batch extracts, and snapshots often arrive as files before they reach more advanced systems.

## Why It Matters in Data Engineering

If you cannot reliably find, open, validate, and parse files, the rest of the pipeline does not matter. File handling is often the first operational edge a new Data Engineer encounters.

## Hands-On Examples

```python
from pathlib import Path
import csv

file_path = Path("datasets/raw/sales_data.csv")

with file_path.open("r", encoding="utf-8") as file_handle:
    reader = csv.DictReader(file_handle)
    rows = list(reader)
```

## Practical Ingestion Patterns

- skip empty files
- validate expected file extensions
- separate bad files from valid ones
- preserve the raw input before transformation

## Common Mistakes

- Hard-coding absolute paths
- Ignoring encoding
- Reading giant files into memory when streaming would be better
- Overwriting raw inputs instead of writing processed outputs separately

## Summary

File handling is one of the most transferable Python skills in Data Engineering.

## Next Module Connection

Module 05 builds on file ingestion by cleaning, validating, and transforming records.
