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
    """Dispatch an async Celery task to run ALL spiders for maximum data volume."""
    task = trigger_full_scrape.delay()
    return {"message": "Full pipeline scrape queued.", "task_id": str(task.id)}


@app.get("/api/v1/products", tags=["products"])
def get_products(
    skip: int = 0,
    limit: int = 100,
    category: str | None = None,
    db: Session = Depends(get_db)
):
    """
    List all tracked products with enriched metadata.
    Filter by category (e.g. laptops, tablets, phones).
    """
    query = db.query(Product)
    if category:
        query = query.filter(Product.category == category)
    products = query.order_by(Product.id).offset(skip).limit(limit).all()

    return [
        {
            "id": p.id,
            "name": p.name,
            "sku": p.sku,
            "category": p.category,
            "brand": p.brand,
            "description": p.description,
            "image_url": p.image_url,
