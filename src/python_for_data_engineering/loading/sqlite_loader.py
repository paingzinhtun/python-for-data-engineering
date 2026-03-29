import sqlite3
from pathlib import Path


def initialize_database(db_path: Path) -> None:
    """Create the example sales table."""
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS sales_orders (
            order_id TEXT PRIMARY KEY,
            customer_id TEXT NOT NULL,
            order_date TEXT NOT NULL,
            country TEXT NOT NULL,
            amount REAL NOT NULL,
            status TEXT NOT NULL
        )
        """
    )
    connection.commit()
    connection.close()


def load_sales_records(db_path: Path, records: list[dict]) -> int:
    """Insert or replace normalized sales records."""
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.executemany(
        """
        INSERT OR REPLACE INTO sales_orders
        (order_id, customer_id, order_date, country, amount, status)
        VALUES (:order_id, :customer_id, :order_date, :country, :amount, :status)
        """,
        records,
    )
    connection.commit()
    inserted_rows = cursor.rowcount
    connection.close()
    return inserted_rows
