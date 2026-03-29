def normalize_country(value: str) -> str:
    """Standardize a country code or replace blank values."""
    cleaned = value.strip().upper()
    return cleaned if cleaned else "UNKNOWN"


def normalize_sales_record(record: dict) -> dict:
    """Normalize one sales record into a consistent schema."""
    return {
        "order_id": record["order_id"].strip(),
        "customer_id": record["customer_id"].strip(),
        "order_date": record["order_date"].strip(),
        "country": normalize_country(record["country"]),
        "amount": float(record["amount"]),
        "status": record["status"].strip().lower(),
    }


def keep_completed_records(records: list[dict]) -> list[dict]:
    """Keep only completed records with positive amounts."""
    cleaned_records = []
    for record in records:
        normalized = normalize_sales_record(record)
        if normalized["status"] == "completed" and normalized["amount"] > 0:
            cleaned_records.append(normalized)
    return cleaned_records
