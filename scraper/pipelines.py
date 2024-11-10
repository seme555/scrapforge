import logging
import sys
import os
from scrapy.exceptions import DropItem

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from core.database import SessionLocal
from core.models import Retailer, Product, PriceHistory
from scraper.items import ProductValidator
