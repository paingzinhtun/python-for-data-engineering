from pathlib import Path


def ensure_directory(path: Path) -> None:
    """Create a directory if it does not already exist."""
    path.mkdir(parents=True, exist_ok=True)


def is_valid_csv_file(path: Path) -> bool:
    """Validate that a file exists, is a CSV, and is not empty."""
    return path.exists() and path.suffix.lower() == ".csv" and path.stat().st_size > 0
