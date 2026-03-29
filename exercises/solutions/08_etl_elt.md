# Module 08 Solutions

## Beginner
ETL transforms before loading. ELT loads earlier and transforms later in the target platform.

## Intermediate
Each stage should have a clear responsibility and return predictable outputs.

## Applied
Use a config object for paths, a transform function for normalization, and a loader that records batch metadata.

## Scenario
Use deterministic output paths, replace-or-upsert logic, and run metadata so a rerun does not duplicate results.
