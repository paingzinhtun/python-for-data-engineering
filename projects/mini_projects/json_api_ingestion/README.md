# Mini Project: JSON API Ingestion Pipeline

## Objective

Read API-style JSON data, flatten nested fields, validate required keys, and write a clean CSV or database-ready output.

## Business Context

A partner system exposes orders in a JSON API response. The analytics team needs a flat daily extract.

## Tasks

1. Read `datasets/sample_inputs/api_orders_sample.json`.
2. Flatten nested customer fields.
3. Standardize field names.
4. Save clean records to a new file.
5. Add one quality check for required IDs.
