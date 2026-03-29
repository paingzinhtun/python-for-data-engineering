# Module 12 Solutions

## Beginner
Full refresh reloads everything. Incremental processing handles only new or changed data.

## Intermediate
Audit columns capture information such as load time, source file, and batch ID.

## Applied
Track the latest processed business date or update timestamp and reprocess a small backfill window when needed.

## Scenario
Use a business key plus update timestamp, allow a late-arrival window, and load into a staging area before applying dedup and upsert rules.
