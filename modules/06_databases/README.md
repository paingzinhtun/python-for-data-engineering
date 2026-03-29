# Module 06: Python and Databases

## Learning Objectives

- Understand database basics for Data Engineers
- Connect to SQLite using Python
- Run queries, inserts, and transactions
- Use parameterized queries and batch inserts safely

## Concept Explanation

Databases are often the first target system in a learning pipeline. SQLite is simple enough for local practice but still teaches the habits that matter in larger systems.

## Why It Matters in Data Engineering

Loading data into tables is a core part of many pipelines. Even if your future environment uses PostgreSQL, Snowflake, or BigQuery, you still need to understand tables, transactions, inserts, and query patterns.

## Hands-On Examples

```python
cursor.execute(
    "INSERT INTO orders (order_id, customer_id, amount) VALUES (?, ?, ?)",
    ("A100", "C001", 125.50),
)
```

## Common Database Mistakes

- Building SQL with string concatenation
- Forgetting transactions
- Loading dirty data before validation
- Not thinking about duplicates or reruns

## Summary

Database loading teaches discipline: schema, transactions, types, and safe queries.

## Next Module Connection

Module 07 introduces APIs as another major source of external data.
