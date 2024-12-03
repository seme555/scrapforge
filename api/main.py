from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import desc

from core.database import get_db
from core.models import Product, PriceHistory, Retailer
from worker.tasks import trigger_ecommerce_scrape, trigger_books_scrape, trigger_full_scrape


app = FastAPI(
    title="ScrapForge API",
    description=(
        "Distributed Price Intelligence API. "
        "Triggers Scrapy/Playwright crawls via Celery and serves time-series price data from PostgreSQL."
    ),
    version="2.0.0"
)


@app.get("/")
