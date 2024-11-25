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

    def start_requests(self):
        for path, category in CATEGORIES:
            yield scrapy.Request(
                url=f"{BASE_URL}/{path}",
                callback=self.parse,
                errback=self.errback,
                meta={
                    "playwright": True,
                    "playwright_include_page": True,
                    "category": category,
                }
            )

    async def parse(self, response):
        """Parse a product listing page and follow pagination."""
        page = response.meta.get("playwright_page")
        category = response.meta.get("category", "unknown")

        if page:
            try:
