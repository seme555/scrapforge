import logging
import sys
import os
from scrapy.exceptions import DropItem

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from core.database import SessionLocal
from core.models import Retailer, Product, PriceHistory
from scraper.items import ProductValidator
from pydantic import ValidationError

logger = logging.getLogger(__name__)


class ValidationPipeline:
    """
    Stage 1: Validate incoming items against the Pydantic schema.
    Drops malformed items with full error logging for observability.
    """

    def process_item(self, item, spider):
        try:
            ProductValidator(**dict(item))
            return item
        except ValidationError as e:
            errors = e.errors()
            spider.logger.warning(
                f"[VALIDATION FAIL] SKU={item.get('sku')} URL={item.get('url')} "
                f"Errors={errors}"
