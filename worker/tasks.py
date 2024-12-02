import os
import subprocess
import sys
from worker.celery_app import app

os.environ.setdefault('SCRAPY_SETTINGS_MODULE', 'scraper.settings')


def _run_spider(spider_name: str) -> subprocess.CompletedProcess:
    """Run a single Scrapy spider by name via the CLI subprocess pattern."""
