from python_for_data_engineering.quality.validation import validate_sales_record


def test_validate_sales_record_rejects_blank_country() -> None:
    record = {
        "order_id": "A104",
        "customer_id": "C005",
        "order_date": "2026-03-27",
        "country": " ",
        "amount": "45.25",
        "status": "completed",
    }

    is_valid, reasons = validate_sales_record(record)

    assert not is_valid
    assert "country" in reasons
