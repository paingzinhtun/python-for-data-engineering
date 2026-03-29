# Module 08: ETL and ELT with Python

## Learning Objectives

- Understand ETL vs ELT
- Separate extract, transform, and load stages
- Design config-driven and repeatable jobs
- Learn idempotency, metadata, and data layer thinking

## Concept Explanation

ETL transforms before load. ELT loads earlier and transforms later. In practice, the right choice depends on tooling, data volume, governance, and downstream needs.

## Why It Matters in Data Engineering

Pipelines are more than scripts. Good pipelines separate concerns, capture metadata, and make reruns safe. This module connects Python code to system design thinking.

## Hands-On Examples

- extract raw files into a `raw/` layer
- validate and normalize records into a `processed/` layer
- load clean rows into SQLite
- write a run summary with row counts and timestamps

## Key Ideas

- raw, processed, curated layers
- config-driven paths and settings
- idempotent outputs
- row counts and audit metadata

## Common Mistakes

- Mixing all pipeline stages in one function
- Overwriting outputs without thinking about reruns
- Failing to preserve raw data
- Not recording how many records were rejected

## Summary

This is where Python becomes pipeline engineering.

## Next Module Connection

Module 09 shows how to make those pipelines more production-ready with logging, testing, and configuration.
