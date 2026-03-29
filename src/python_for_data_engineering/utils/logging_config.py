import logging


def configure_logging(level: int = logging.INFO) -> None:
    """Configure a simple console logger for teaching projects."""
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )
