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
                await page.wait_for_selector(".thumbnail", timeout=12000)
            except Exception:
                self.logger.warning(f"Timeout waiting for products on {response.url}")
            finally:
                await page.close()

        products = response.css(".thumbnail")
        self.logger.info(
            f"[{category.upper()}] {response.url} â€” {len(products)} products found"
        )

        for product in products:
            item = self._extract_product(product, response, category)
            if item:
                yield item

        # Follow pagination
        next_page = response.css("a[rel='next']::attr(href)").get()
        if next_page:
            yield scrapy.Request(
                url=response.urljoin(next_page),
                callback=self.parse,
                errback=self.errback,
                meta={
                    "playwright": True,
                    "playwright_include_page": True,
                    "category": category,
                }
            )

    def _extract_product(self, product, response, category: str):
        """
        Extract all fields from a single product card.
        Returns a populated ProductItem or None if critical fields are missing.
        """
        # --- Required fields ---
        name = (
            product.css("a.title::attr(title)").get()
            or product.css("a.title::text").get()
            or ""
        ).strip()

        link = product.css("a.title::attr(href)").get()

        if not name or not link:
            self.logger.debug("Skipping product card â€” missing name or link")
            return None

        url = response.urljoin(link)
        sku = url.rstrip("/").split("/")[-1]
