from pathlib import Path

from python_for_data_engineering.ingestion.readers import read_csv_records
from python_for_data_engineering.loading.sqlite_loader import (
    initialize_database,
    load_sales_records,
)
from python_for_data_engineering.quality.validation import validate_sales_record
from python_for_data_engineering.transformation.clean_sales import keep_completed_records
from python_for_data_engineering.utils.files import is_valid_csv_file


def run_sales_etl(input_path: Path, db_path: Path) -> dict:
    """Run a small end-to-end ETL flow for the sample sales dataset."""
    if not is_valid_csv_file(input_path):
        raise FileNotFoundError(f"Invalid input file: {input_path}")

    raw_records = read_csv_records(input_path)
    valid_records = []
    invalid_records = []

    for record in raw_records:
        is_valid, reasons = validate_sales_record(record)
        if is_valid:
            valid_records.append(record)
        else:
            invalid_records.append({"record": record, "reasons": reasons})

    cleaned_records = keep_completed_records(valid_records)
    initialize_database(db_path)
    loaded_count = load_sales_records(db_path, cleaned_records)

    return {
        "raw_count": len(raw_records),
        "valid_count": len(valid_records),
        "invalid_count": len(invalid_records),
        "loaded_count": loaded_count,
    }
