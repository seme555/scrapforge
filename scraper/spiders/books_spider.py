import re
import scrapy
from scraper.items import ProductItem

# Word-to-number map for CSS star rating class names
STAR_RATING = {
    "One": 1.0, "Two": 2.0, "Three": 3.0, "Four": 4.0, "Five": 5.0
}


class BooksSpider(scrapy.Spider):
    """
    High-volume spider targeting books.toscrape.com.

    A site purpose-built for scraping practice with 1,000 books
    across 50 genres. Uses standard HTTP (no Playwright needed)
    for maximum throughput. Extracts:
      - title, price, currency, in_stock status
      - star rating, category / genre
      - cover image URL
      - per-genre breadcrumb category
    """
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/catalogue/page-1.html"]

    custom_settings = {
        # No Playwright needed â€” this site is static HTML
        "DOWNLOAD_HANDLERS": {},
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
        "CONCURRENT_REQUESTS": 16,
        "DOWNLOAD_DELAY": 0.25,
    }

    def parse(self, response):
        """Parse a paginated book listing page."""
        books = response.css("article.product_pod")
        self.logger.info(
            f"[BOOKS] {response.url} â€” {len(books)} books found"
        )

        for book in books:
            item = self._extract_book(book, response)
            if item:
                yield item

        # Follow pagination (50 pages Ã— 20 books = 1,000 total)
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def _extract_book(self, book, response):
        """Extract all available fields from a book card."""
        # Title
        name = book.css("h3 a::attr(title)").get()
        if not name:
            return None

        # Relative URL to book detail page
        link = book.css("h3 a::attr(href)").get()
