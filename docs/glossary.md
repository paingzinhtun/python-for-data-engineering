# Glossary

## API
An application programming interface. In Data Engineering, APIs are often used as data sources.

## Batch Processing
Processing data in groups at scheduled intervals instead of one event at a time.

## CSV
Comma-separated values. A simple file format often used for exports and ingestion.

## Data Quality Check
A rule that tests whether data meets expectations, such as non-null IDs or positive quantities.

## Deduplication
Removing duplicate records based on keys or business logic.

## ELT
Extract, load, transform. Raw data is loaded first, then transformed later, often inside a warehouse.

## ETL
Extract, transform, load. Data is transformed before loading into the target system.

## Idempotency
A property where running a pipeline multiple times produces the same intended result without corrupting outputs.

## Incremental Load
A load strategy that processes only new or changed data since the previous run.

## JSON
JavaScript Object Notation. A common format for APIs and semi-structured data.

## Late-Arriving Data
Records that belong to an earlier business time window but arrive after the expected processing time.

## Logging
Recording structured or human-readable messages about what a program is doing.

## Metadata
Data about data, such as file names, load timestamps, source systems, and row counts.

## Parameterized Query
A SQL query that passes values safely as parameters instead of building SQL with string concatenation.

## Partition
A logical division of data, often by date or region, that improves manageability and performance.

## Pipeline
A sequence of steps that moves data from source to target, often including extraction, validation, transformation, and loading.

## Raw Layer
The storage area that keeps source data as close to original as practical.

## Schema
The expected structure of data, including field names and data types.

## SQLite
A lightweight relational database useful for teaching and local projects.

## Transformation
Changing data from one form into another, such as cleaning fields, renaming columns, or aggregating records.
