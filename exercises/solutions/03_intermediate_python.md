# Module 03 Solutions

## Beginner

```python
active_rows = [row for row in rows if row["status"] == "active"]

def parse_float(value: str, default: float = 0.0) -> float:
    try:
        return float(value)
    except ValueError:
        return default
```

## Intermediate
Create a separate file when a helper is reused across scripts or concepts.

## Applied
Use `sorted(records, key=lambda row: (row["created_at"], row["customer_id"]), reverse=True)` with care about desired sort order.

## Scenario
Both approaches are valid. Prefer functions first for small workflows and a class when shared state improves clarity.
