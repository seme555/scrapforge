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
def read_root():
    return {"status": "Online", "service": "ScrapForge API", "version": "2.0.0"}


@app.post("/scrape/trigger", tags=["scraping"])
def trigger_scrape():
    """Dispatch an async Celery task to scrape the e-commerce (webscraper.io) spider."""
    task = trigger_ecommerce_scrape.delay()
    return {"message": "E-commerce scraping task queued.", "task_id": str(task.id)}


@app.post("/scrape/trigger/books", tags=["scraping"])
def trigger_books():
    """Dispatch an async Celery task to scrape books.toscrape.com (1,000 books)."""
    task = trigger_books_scrape.delay()
    return {"message": "Books scraping task queued.", "task_id": str(task.id)}


@app.post("/scrape/trigger/all", tags=["scraping"])
def trigger_all():
