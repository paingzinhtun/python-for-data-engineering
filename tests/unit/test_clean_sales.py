from python_for_data_engineering.transformation.clean_sales import (
    keep_completed_records,
    normalize_country,
)


def test_normalize_country_blank_value_returns_unknown() -> None:
    assert normalize_country("   ") == "UNKNOWN"


def test_keep_completed_records_filters_cancelled_and_zero_amount() -> None:
    raw_records = [
        {
            "order_id": "A100",
            "customer_id": "C001",
            "order_date": "2026-03-25",
            "country": "mm",
            "amount": "125.50",
            "status": "completed",
        },
        {
            "order_id": "A102",
            "customer_id": "C003",
            "order_date": "2026-03-26",
            "country": "th",
            "amount": "0.00",
            "status": "cancelled",
        },
    ]

    result = keep_completed_records(raw_records)

    assert len(result) == 1
    assert result[0]["order_id"] == "A100"
