import csv
import json
from pathlib import Path


def read_csv_records(path: Path) -> list[dict]:
    """Read a CSV file into a list of row dictionaries."""
    with path.open("r", encoding="utf-8", newline="") as file_handle:
        reader = csv.DictReader(file_handle)
        return list(reader)


def read_json_records(path: Path) -> list[dict]:
    """Read a JSON array file into Python records."""
    with path.open("r", encoding="utf-8") as file_handle:
        return json.load(file_handle)
