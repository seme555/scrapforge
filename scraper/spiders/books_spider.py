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
