from pathlib import Path

from python_for_data_engineering.pipelines.sales_etl import run_sales_etl


def test_run_sales_etl_loads_clean_records(tmp_path: Path) -> None:
    input_path = Path("datasets/raw/sales_data.csv")
    db_path = tmp_path / "sales.db"

    result = run_sales_etl(input_path=input_path, db_path=db_path)

    assert result["raw_count"] == 5
    assert result["invalid_count"] == 2
    assert result["loaded_count"] == 3
