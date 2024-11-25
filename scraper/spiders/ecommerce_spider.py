import scrapy
from scraper.items import ProductItem


# All product categories available on the test site
CATEGORIES = [
    ("computers/laptops", "laptops"),
    ("computers/tablets", "tablets"),
    ("phones/touch", "touch-phones"),
    ("phones", "phones"),
]

BASE_URL = "https://webscraper.io/test-sites/e-commerce/allinone"


class EcommerceSpider(scrapy.Spider):
    """
    Production-grade Scrapy spider with Playwright rendering.

    Scrapes ALL product categories across ALL paginated pages from
    the webscraper.io e-commerce test site, extracting:
      - name, SKU, URL, category
      - price, currency, in-stock status
      - description, image URL
      - star rating and review count
      - retailer metadata
    """
    name = "ecommerce"
    allowed_domains = ["webscraper.io"]

