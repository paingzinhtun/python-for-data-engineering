# Module 09 Solutions

## Beginner

```python
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Starting pipeline")
api_key = os.getenv("API_KEY", "")
logger.info("Finished pipeline")
```

## Intermediate
Tests should focus on pure functions first because they are fast and reliable.

## Applied
Move repeated constants into config, business logic into transformation code, and I/O into ingestion or loading modules.

## Scenario
Retry transient network failures, log context like source and page number, and fail fast on schema mismatch or permanent auth errors.
