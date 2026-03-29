# Module 02 Solutions

## Beginner

```python
customer = {
    "customer_id": "C001",
    "country": "mm",
    "signup_date": "2026-03-01",
}

order_ids = ["A100", "A101", "A102"]
print(order_ids[1])
```

## Intermediate

```python
seen = set()
duplicates = set()

for order_id in ["A100", "A101", "A100"]:
    if order_id in seen:
        duplicates.add(order_id)
    seen.add(order_id)
```

## Applied
Loop through records, add `record["country"].strip().upper()` to a set, then sort it.

## Scenario
Use nested key access carefully and create a new flat dictionary with the required fields.
