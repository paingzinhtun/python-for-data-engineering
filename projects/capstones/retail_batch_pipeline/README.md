# Capstone: Retail Batch Pipeline

## Project Overview

Build a retail batch pipeline that ingests daily sales and returns files, validates records, transforms them into analytics-friendly structures, and loads them into SQLite staging and reporting tables.

## Business Context

A retail company receives daily flat-file exports from store systems. Finance needs a clean daily summary and operations needs rejected record visibility.

## Architecture Explanation

- ingest source files into a raw layer
- validate file presence and schema
- transform rows into standardized tables
- load staging tables
- compute reporting outputs
- write audit metadata and row counts

## Folder Structure

- `data/raw/`
- `data/processed/`
- `src/`
- `tests/`
- `docs/`

## Starter Tasks

1. Add support for sales and returns files.
2. Track rejected records with reasons.
3. Build a daily summary table.
4. Add tests for transformations and loads.

## Expected Outputs

- cleaned tables
- rejection report
- daily KPI summary
- run metadata

## Stretch Goals

- incremental logic by business date
- partitioned processed outputs
- CLI entry point

## Best-Practice Solution Outline

Use separate modules for extraction, validation, transformation, and loading. Make reruns safe with primary keys and deterministic output paths.
