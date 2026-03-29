# Module 05: Python for Data Processing

## Learning Objectives

- Parse, clean, filter, and aggregate records
- Handle missing values and type conversion
- Think in terms of schema and validation
- Build reusable transformation functions

## Concept Explanation

Data processing means turning messy inputs into reliable structured outputs. That often includes trimming strings, standardizing values, checking required fields, converting types, and creating derived columns.

## Why It Matters in Data Engineering

Raw data is rarely analysis-ready. Data Engineers build the logic that turns unreliable source records into trustworthy downstream tables.

## Hands-On Examples

```python
def normalize_order(record: dict) -> dict:
    return {
        "order_id": record["order_id"].strip(),
        "customer_id": record["customer_id"].strip(),
        "amount": float(record["amount"]),
        "country": record["country"].upper(),
    }
```

## Schema Thinking

Ask these questions:

- which fields are required
- which fields can be null
- which fields need type conversion
- which values are invalid but common in the source

## Common Mistakes

- Cleaning values inconsistently across scripts
- Mixing validation with loading logic
- Dropping bad records without tracking counts
- Failing to define required fields explicitly

## Summary

Transformation logic is where pipeline correctness is won or lost.

## Next Module Connection

Module 06 shows how to load clean outputs into a database safely.
