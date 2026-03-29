# Module 06 Solutions

## Beginner

```python
import sqlite3

connection = sqlite3.connect("orders.db")
cursor = connection.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS orders (order_id TEXT PRIMARY KEY, amount REAL)"
)
cursor.execute(
    "INSERT INTO orders (order_id, amount) VALUES (?, ?)",
    ("A100", 125.50),
)
connection.commit()
```

## Intermediate
Use `executemany` for batch inserts and a parameterized `SELECT`.

## Applied
Wrap the insert logic in `try/except`, commit on success, and rollback on failure.

## Scenario
Use a primary key, unique constraint, or a staging-and-merge pattern depending on the target system.
