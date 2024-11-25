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
