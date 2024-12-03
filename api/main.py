from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import desc

from core.database import get_db
from core.models import Product, PriceHistory, Retailer
from worker.tasks import trigger_ecommerce_scrape, trigger_books_scrape, trigger_full_scrape


app = FastAPI(
