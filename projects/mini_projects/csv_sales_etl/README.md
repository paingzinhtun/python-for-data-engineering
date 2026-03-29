# Mini Project: CSV Sales ETL Pipeline

## Objective

Build a small batch pipeline that reads raw sales CSV data, validates rows, transforms fields, and loads clean data into SQLite.

## Architecture Summary

- source: local CSV file
- extract: read raw rows
- validate: required fields and positive amount
- transform: normalize casing and types
- load: SQLite table
- output: summary counts and loaded records

## Data Flow

`raw CSV -> validation -> cleaned rows -> SQLite -> load summary`

## Setup Instructions

- use `datasets/raw/sales_data.csv`
- use the starter code in `src/python_for_data_engineering/`
- run tests before and after your changes

## Tasks

1. Add logging to the ETL pipeline.
2. Save rejected rows to a JSON file.
3. Add a test for duplicate order handling.

## Suggested Enhancements

- add a batch ID
- write a processed CSV output
- support command-line arguments

## Expected Learning Outcomes

- file ingestion
- data validation
- transformation functions
- SQLite loading
- simple integration testing
