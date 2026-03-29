REQUIRED_SALES_FIELDS = [
    "order_id",
    "customer_id",
    "order_date",
    "country",
    "amount",
    "status",
]


def missing_required_fields(record: dict, required_fields: list[str]) -> list[str]:
    """Return missing or blank required fields."""
    missing_fields = []
    for field_name in required_fields:
        if field_name not in record or str(record[field_name]).strip() == "":
            missing_fields.append(field_name)
    return missing_fields


def validate_sales_record(record: dict) -> tuple[bool, list[str]]:
    """Validate a sales record and return status with reasons."""
    reasons = missing_required_fields(record, REQUIRED_SALES_FIELDS)
    if not reasons:
        try:
            if float(record["amount"]) <= 0:
                reasons.append("amount_must_be_positive")
        except ValueError:
            reasons.append("amount_must_be_numeric")
    return len(reasons) == 0, reasons
