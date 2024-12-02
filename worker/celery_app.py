import os
from celery import Celery

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

app = Celery(
    'scrapforge',
    broker=REDIS_URL,
    backend=REDIS_URL,
    include=['worker.tasks']
)

# Optional scheduling (Celery Beat)
app.conf.beat_schedule = {
    'scrape-ecommerce-daily': {
        'task': 'worker.tasks.trigger_ecommerce_scrape',
        'schedule': 86400.0, # Every 24 hours
    },
}

