BOT_NAME = 'scrapforge'

SPIDER_MODULES = ['scraper.spiders']
NEWSPIDER_MODULE = 'scraper.spiders'

# Obey robots.txt - Enterprise setups often ignore this but we will be good netizens for testing
ROBOTSTXT_OBEY = False

# Configure concurrent requests
CONCURRENT_REQUESTS = 16
