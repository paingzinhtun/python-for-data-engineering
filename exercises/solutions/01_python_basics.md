# Module 01 Solutions

## Beginner

```python
source_file = "sales_2026_03_29.csv"
row_count = 1250
is_valid = True

def is_large_file(rows: int) -> bool:
    return rows > 1000
```

## Intermediate

```python
for file_name in ["sales.csv", "notes.txt", "returns.csv"]:
    if file_name.endswith(".csv"):
        print(file_name)

def classify_row(amount: float) -> str:
    return "keep" if amount > 0 else "reject"
```

## Applied
Use a loop, `startswith("sales_")`, and `endswith(".csv")` to count matching files.

## Scenario
Check for positive size, allowed extension, and a non-empty name before processing.
