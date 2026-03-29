# Python for Data Engineering: Beginner to Advanced

Learn Python the way a Data Engineer actually uses it: to ingest files, call APIs, validate records, transform data, load databases, automate repeatable jobs, and build maintainable pipelines.

This repository is a complete learning, practice, and portfolio course. It is designed for beginners who want a practical path into Data Engineering without skipping Python fundamentals.

## Who This Repository Is For

- Beginners who are new to Python
- Aspiring Data Engineers who want practical projects
- Analysts or BI professionals moving toward engineering work
- Self-learners who want a structured repo, not scattered notes
- Educators and mentors who want a shareable teaching resource

## What You Will Learn

- Python foundations through real data examples
- File handling for CSV, JSON, text, and directories
- Data cleaning, validation, and transformation techniques
- Database access with SQLite and production-oriented SQL habits
- API extraction patterns including pagination and validation
- ETL and ELT thinking, pipeline stages, and idempotent design
- Logging, testing, configuration, and error handling
- Performance basics, generators, chunking, and scale tradeoffs
- Real-world Data Engineering patterns such as incremental loads, deduplication, audit columns, and reproducibility

## Learning Philosophy

This repo teaches both `how` and `why`.

We start simple:

- write readable Python
- understand core types and control flow
- manipulate records and files
- build reusable functions

Then we connect those skills to realistic Data Engineering work:

- ingest raw files and APIs
- validate schemas and bad records
- load data into a database
- structure code like a maintainable pipeline
- reason about scale, reliability, and operational tradeoffs

The goal is not to turn every lesson into a toy notebook. The goal is to build habits that transfer into actual Data Engineering projects.

## Repository Structure

```text
.
├── README.md
├── ROADMAP.md
├── CONTRIBUTING.md
├── docs/
├── modules/
├── exercises/
├── datasets/
├── src/
├── tests/
├── projects/
└── assets/
```

## Course Roadmap

1. Orientation and setup
2. Python basics
3. Data structures
4. Intermediate Python
5. Files and I/O
6. Data processing
7. Databases
8. APIs
9. ETL / ELT
10. Production Python
11. Performance mindset
12. Project structure
13. Real-world patterns
14. Mini projects
15. Capstones
16. Interview prep
17. Next steps

See [ROADMAP.md](ROADMAP.md) for the full sequence.

## How to Study This Repo

- Read one module at a time.
- Run the examples locally.
- Complete the exercises before opening the solutions.
- Keep notes on what each concept solves in a data workflow.
- Build at least one mini-project and one capstone in your own GitHub portfolio.
- Revisit modules 08 to 12 after you finish your first full project. They become much clearer once you have written pipeline code yourself.

## Recommended Weekly Progress

- Week 1: modules 00 to 03
- Week 2: modules 04 to 06
- Week 3: modules 07 to 09
- Week 4: modules 10 to 12
- Week 5: mini-projects
- Week 6: capstone and interview prep

## What Makes This Different

- Python is taught through a Data Engineering lens from day one.
- Exercises include realistic ingestion, transformation, and loading scenarios.
- Lessons explain business and operational context, not just syntax.
- Projects are designed to be shareable portfolio work.
- The repo emphasizes maintainability, debugging, and professional habits.

## Quick Start

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest
```

Then begin with:

- [docs/course-overview.md](docs/course-overview.md)
- [docs/setup-guide.md](docs/setup-guide.md)
- [modules/00_orientation/README.md](modules/00_orientation/README.md)

## Portfolio Guidance

If you want employers to take your work seriously:

- finish the mini-projects with clean README files
- add tests to one project
- document assumptions and data quality checks
- explain tradeoffs such as full refresh vs incremental loads
- show code structure, not just notebook output

The guide at [docs/portfolio-guide.md](docs/portfolio-guide.md) explains how to turn course work into stronger public projects.

## Contributing

This repo is open-source friendly. Improvements are welcome for:

- clearer explanations
- bug fixes
- better exercises
- more realistic sample datasets
- more tests and project enhancements

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This repository is released under the MIT License.

## What To Learn Next

After completing this repo, move into:

- advanced SQL
- data modeling
- orchestration with Airflow
- Spark and distributed processing
- Docker and containerized development
- cloud data platforms
- CI/CD for data pipelines
- observability and monitoring
- lakehouse fundamentals

Module 16 and the docs folder provide a guided roadmap.
