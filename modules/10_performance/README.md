# Module 10: Performance and Scale Mindset

## Learning Objectives

- Understand time and memory basics
- Use generators and iterators
- Process data in chunks
- Learn when Python alone is enough and when to move to distributed tools

## Concept Explanation

Not every data problem needs Spark, and not every pure Python script scales. Good engineers understand where the current approach is sufficient and where it becomes risky.

## Why It Matters in Data Engineering

Performance decisions affect runtime, cost, and reliability. Loading a small daily CSV locally is very different from processing millions of records across many partitions.

## Hands-On Examples

```python
def read_lines(path):
    with open(path, "r", encoding="utf-8") as file_handle:
        for line in file_handle:
            yield line.rstrip("\n")
```

## Decision Framework

- pure Python is often enough for small to medium control-flow-heavy tasks
- pandas is useful for tabular transformation but not always memory-friendly
- Spark becomes relevant when data volume, parallelism, or platform standards demand it

## Common Mistakes

- Reading everything into memory by default
- Optimizing too early
- Assuming pandas is always the answer
- Ignoring data size growth over time

## Summary

Performance is not just speed. It is fit-for-purpose design.

## Next Module Connection

Module 11 focuses on project structure so growing code stays maintainable.
