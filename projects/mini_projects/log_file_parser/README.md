# Mini Project: Log File Parser

## Objective

Parse an application log file, count event types, and identify warning and error patterns.

## Tasks

1. Read `datasets/raw/app_events.log`.
2. Parse timestamp, level, and message fields.
3. Count how many `INFO`, `WARN`, and `ERROR` events exist.
4. Create a summary output file.

## Suggested Enhancements

- group issues by pipeline run
- flag repeated warnings
- write a CSV summary
