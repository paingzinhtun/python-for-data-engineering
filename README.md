# Python for Data Engineering: Beginner to Advanced

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](pyproject.toml)
[![Course Type](https://img.shields.io/badge/Course-Hands--On-orange.svg)](ROADMAP.md)
[![Focus](https://img.shields.io/badge/Focus-Data%20Engineering-purple.svg)](docs/course-overview.md)

Learn Python the way Data Engineers actually use it: to ingest files, call APIs, validate records, transform data, load databases, automate repeatable jobs, and build maintainable pipelines.

This repository is a complete learning, practice, and portfolio course for beginners and early intermediate learners who want to become Data Engineers through practical Python work, not disconnected syntax drills.

## Why This Repo Exists

Most Python learning resources are either:

- too generic to feel relevant to Data Engineering
- too advanced too early
- too academic
- too notebook-heavy
- too light on projects, testing, structure, and real workflow thinking

This course is built to close that gap.

It teaches Python fundamentals and then steadily connects them to real Data Engineering tasks like:

- reading CSV and JSON files
- validating and cleaning records
- loading SQLite tables
- consuming API data
- designing ETL and ELT workflows
- logging, testing, and structuring small pipelines

## Who This Is For

- beginners who are new to Python
- aspiring Data Engineers who want structured practice
- analysts moving toward engineering work
- self-learners who want a complete repo instead of scattered notes
- educators and mentors who want a shareable teaching resource

## What You Will Learn

- Python foundations through data-oriented examples
- strings, lists, dictionaries, sets, and record manipulation
- intermediate Python patterns for reusable pipeline code
- file handling for CSV, JSON, text, and directories
- data cleaning, validation, transformation, and aggregation
- SQLite loading and database-safe habits
- API extraction patterns like pagination and response validation
- ETL and ELT thinking, idempotency, and layer design
- logging, testing, configuration, and exception handling
- performance basics, generators, chunking, and scale tradeoffs
- real-world Data Engineering patterns like incremental loads, deduplication, audit columns, and reproducibility

## What Makes It Different

- Python is taught through a Data Engineering lens from day one.
- Every major topic answers both `how` and `why`.
- Exercises include practical workflow scenarios, not just syntax repetition.
- The repo includes lessons, exercises, solutions, starter code, tests, datasets, mini-projects, and capstones.
- The structure is designed for both self-study and public portfolio use.

## Repository At a Glance

- `17` structured modules from orientation to next-step roadmap
- module-wise exercises and separate solutions
- reusable starter package under `src/`
- sample datasets for files, API-style JSON, and logs
- mini-projects and capstones
- tests for starter pipeline code
- documentation for setup, study flow, glossary, and portfolio guidance

## Repository Structure

```text
python-for-data-engineering/
|- README.md
|- ROADMAP.md
|- CONTRIBUTING.md
|- docs/
|- modules/
|- exercises/
|- datasets/
|- src/
|- tests/
|- projects/
`- assets/
```

## Course Roadmap

### Stage 1: Foundations

1. Orientation and setup
2. Python basics
3. Core data structures

### Stage 2: Practical Python

4. Intermediate Python
5. Files and I/O
6. Data processing

### Stage 3: Data Engineering Inputs and Outputs

7. Databases
8. APIs
9. ETL / ELT

### Stage 4: Production Skills

10. Production Python
11. Performance mindset
12. Project structure

### Stage 5: Real-World Pipeline Thinking

13. Real-world patterns
14. Mini-projects
15. Capstones

### Stage 6: Career Readiness

16. Interview prep
17. Next steps

See the full curriculum in [ROADMAP.md](ROADMAP.md).

## Featured Topics

### Python Fundamentals for Data Work

- variables, data types, control flow, functions, and debugging
- strings, lists, dictionaries, sets, and iteration patterns

### Practical Data Handling

- CSV, JSON, file paths, encodings, and directory traversal
- cleaning records, missing values, type conversion, and schema thinking

### Core Data Engineering Skills

- database inserts, transactions, and parameterized queries
- API requests, pagination, rate-limit awareness, and validation
- ETL and ELT workflow design

### Production-Oriented Habits

- logging
- testing with `pytest`
- configuration and environment variables
- modular code structure
- performance tradeoffs and scale awareness

## Projects Included

### Mini Projects

- CSV sales ETL pipeline
- JSON API ingestion pipeline
- log file parser
- daily reporting script

### Capstones

- retail batch pipeline
- partner API to warehouse loader
- data quality and observability pipeline

These projects are designed to help you build shareable portfolio work, not just complete exercises.

## How To Study This Repo

1. Start with [docs/course-overview.md](docs/course-overview.md).
2. Follow the setup steps in [docs/setup-guide.md](docs/setup-guide.md).
3. Begin with [modules/00_orientation/README.md](modules/00_orientation/README.md).
4. Study one module at a time.
5. Complete the exercise before opening the solution.
6. Run the code and modify the examples yourself.
7. Build at least one mini-project and one capstone for your portfolio.

## Recommended Study Pace

- Week 1: modules 00 to 03
- Week 2: modules 04 to 06
- Week 3: modules 07 to 09
- Week 4: modules 10 to 12
- Week 5: mini-projects
- Week 6: capstone, revision, and interview prep

## Quick Start

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest
```

Then open:

- [docs/course-overview.md](docs/course-overview.md)
- [docs/learning-path.md](docs/learning-path.md)
- [docs/repo-navigation.md](docs/repo-navigation.md)

## Example Learning Outcomes

By the end of this repository, you should be able to:

- write readable Python for batch data workflows
- validate and clean raw records
- process file-based data safely
- extract and flatten API responses
- load transformed data into SQLite
- structure a small Python project like a real pipeline repo
- explain tradeoffs like full refresh vs incremental loads
- discuss when Python alone is enough and when tools like Spark or Airflow become necessary

## Portfolio Value

If you want this repo to help you professionally, do more than just read it.

- finish at least one mini-project end to end
- document assumptions and data quality checks
- add tests to one project
- explain tradeoffs such as idempotency and incremental loads
- show structure, not only notebook output

Use [docs/portfolio-guide.md](docs/portfolio-guide.md) to turn your course work into stronger public projects.

## Repo Navigation

- [docs/course-overview.md](docs/course-overview.md) for the high-level picture
- [docs/setup-guide.md](docs/setup-guide.md) for environment setup
- [docs/glossary.md](docs/glossary.md) for key Python and Data Engineering terms
- [modules](modules) for lessons
- [exercises/module_wise_exercises](exercises/module_wise_exercises) for practice
- [exercises/solutions](exercises/solutions) for solutions
- [projects/mini_projects](projects/mini_projects) for smaller builds
- [projects/capstones](projects/capstones) for larger case studies

## Contributing

This repository is open-source friendly. Contributions are welcome for:

- clearer explanations
- better exercises
- more realistic sample datasets
- stronger tests
- improved project prompts
- fixes for examples or documentation

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This repository is released under the MIT License. See [LICENSE](LICENSE).

## What To Learn Next

After completing this repo, continue with:

- advanced SQL
- data modeling
- orchestration with Airflow
- Spark and distributed processing
- Docker
- cloud data platforms
- CI/CD for data pipelines
- observability and monitoring
- lakehouse fundamentals

Module 16 and the docs folder provide a guided next-step roadmap.

## Star This Repo

If this repository helps you learn or teach Python for Data Engineering, consider starring it and sharing it with other learners.
