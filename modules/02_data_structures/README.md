# Module 02: Core Python Data Structures

## Learning Objectives

- Use strings, lists, tuples, sets, and dictionaries confidently
- Apply slicing and iteration patterns
- Use built-in functions for practical data manipulation
- Model raw records using the right structure

## Concept Explanation

Data often arrives as rows, key-value records, or nested JSON objects. Python data structures help you represent that data before it ever reaches a database or DataFrame.

## Why It Matters in Data Engineering

- Lists help store batches of records
- Dictionaries represent rows or API objects
- Sets help detect unique IDs and duplicates
- Strings are central for parsing, cleaning, and standardization

## Hands-On Examples

```python
record = {
    "order_id": "A100",
    "customer_id": "C001",
    "amount": "125.50",
}

clean_amount = float(record["amount"])
```

```python
seen_ids = set()
duplicate_ids = []

for order_id in ["A100", "A101", "A100"]:
    if order_id in seen_ids:
        duplicate_ids.append(order_id)
    seen_ids.add(order_id)
```

## Practical Data Manipulation Ideas

- trim whitespace from strings
- split file names to extract dates
- gather unique country codes with a set
- use dictionaries for field-by-field transformation

## Common Mistakes

- Using the wrong structure for the task
- Forgetting that tuples are immutable
- Assuming dictionary keys always exist
- Treating all values as strings and delaying type cleanup too long

## Summary

Strong Data Engineering code usually starts with strong handling of native Python structures.

## Next Module Connection

Module 03 shows how to write more reusable Python with imports, exceptions, comprehensions, and basic OOP.
