import re
import scrapy
from scraper.items import ProductItem

# Word-to-number map for CSS star rating class names
STAR_RATING = {
    "One": 1.0, "Two": 2.0, "Three": 3.0, "Four": 4.0, "Five": 5.0
}


