# Module 07: APIs and External Data

## Learning Objectives

- Make HTTP requests with `requests`
- Parse JSON responses
- Handle pagination and rate limits
- Validate external data before loading it

## Concept Explanation

Many pipelines start by pulling data from services rather than files. API data is useful but often inconsistent, paginated, and subject to retries or authentication rules.

## Why It Matters in Data Engineering

External systems change. Endpoints can fail, schemas can drift, and incomplete responses can break downstream assumptions. API extraction code must be defensive and observable.

## Hands-On Examples

```python
import requests

response = requests.get("https://example.com/api/orders", timeout=30)
response.raise_for_status()
payload = response.json()
```

## Design Questions

- how many pages need to be fetched
- what happens if the API returns partial data
- where will you store raw responses
- how will you retry or log failures

## Common Mistakes

- Ignoring timeouts
- Assuming all keys exist in the JSON
- Forgetting pagination
- Not separating API extraction from transformation

## Summary

APIs teach important engineering habits around reliability and uncertainty.

## Next Module Connection

Module 08 combines source extraction and loading into ETL / ELT workflow design.
