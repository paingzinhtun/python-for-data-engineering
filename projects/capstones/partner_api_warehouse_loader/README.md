# Capstone: Partner API to Warehouse Loader

## Project Overview

Simulate a partner integration where paginated API data is extracted, validated, flattened, stored in raw JSON snapshots, and then loaded into warehouse-style staging tables.

## Business Context

A business partner exposes order data via an API, but the payload changes occasionally and rate limits apply.

## Tasks

1. Design an extraction layer with pagination support.
2. Store raw response snapshots.
3. Flatten and validate the payload.
4. Load clean records into SQLite staging tables.
5. Add logging and retry behavior.

## Stretch Goals

- add watermark logic
- add late-arrival handling
- record page-level metadata
