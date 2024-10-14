# ScrapForge

> A production-grade, distributed web scraping pipeline for real-time e-commerce price tracking. Built with Scrapy, Playwright, Celery, FastAPI, PostgreSQL, and Redis â€” fully containerised with Docker.

---

## ðŸ“¸ Screenshots

### API Documentation (Swagger UI)
![Swagger UI](docs/screenshots/1_swagger_ui.png)

### Live Products Endpoint â€” Enriched Data
![Products API](docs/screenshots/4_enriched_products.png)

### Categories Summary Endpoint
![Categories API](docs/screenshots/2_categories_api.png)

### pgAdmin â€” Database View (1,124 Products)
![pgAdmin](docs/screenshots/5_pgadmin.png)

> Shows `scraper_db` with all 4 tables (`alembic_version`, `price_history`, `products`, `retailers`) and the `products` table results â€” 1,124 total rows, query completed in 0.225s.

**Tables in `scraper_db`:**
| Table | Description |
|---|---|
| `retailers` | Source website metadata |
| `products` | 1,124+ unique products with enriched fields |
| `price_history` | Time-series price snapshots (grows every scrape) |

---

## ðŸ—ï¸ Architecture

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚                        Docker Compose                       â”‚
â”‚                                                            â”‚
â”‚  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”   POST /scrape   â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”   â”‚
â”‚  â”‚          â”‚ â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â–¶â”‚  Celery Worker        â”‚   â”‚
â”‚  â”‚ FastAPI  â”‚                  â”‚  (Redis Broker)       â”‚   â”‚
â”‚  â”‚ :8000    â”‚â—€â”€â”€ JSON â”€â”€â”€â”€â”€â”€â”€â”€ â”‚                       â”‚   â”‚
â”‚  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜                  â”‚  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”  â”‚   â”‚
â”‚       â”‚                        â”‚  â”‚ Scrapy + Play-  â”‚  â”‚   â”‚
â”‚       â”‚                        â”‚  â”‚ wright Spiders  â”‚  â”‚   â”‚
â”‚       â–¼                        â”‚  â””â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”˜  â”‚   â”‚
â”‚  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”                  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜   â”‚
â”‚  â”‚PostgreSQLâ”‚â—€â”€â”€â”€â”€ SQLAlchemy  â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜               â”‚
â”‚  â”‚  :5432   â”‚      ORM + Alembic                           â”‚
â”‚  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜                                              â”‚
â”‚                                                            â”‚
â”‚  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”                                              â”‚
â”‚  â”‚  Redis   â”‚  â† Task Queue / Result Backend               â”‚
â”‚  â”‚  :6379   â”‚                                              â”‚
â”‚  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜                                              â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

---

## âš™ï¸ Tech Stack

| Layer | Technology |
|---|---|
| **Scraping** | [Scrapy 2.11](https://scrapy.org/) |
| **JS Rendering** | [Playwright](https://playwright.dev/) via `scrapy-playwright` |
| **Task Queue** | [Celery 5](https://docs.celeryq.dev/) + [Redis 7](https://redis.io/) |
| **API** | [FastAPI](https://fastapi.tiangolo.com/) + [Uvicorn](https://www.uvicorn.org/) |
| **Database** | [PostgreSQL 15](https://www.postgresql.org/) |
| **ORM** | [SQLAlchemy 2](https://www.sqlalchemy.org/) |
| **Migrations** | [Alembic](https://alembic.sqlalchemy.org/) |
| **Validation** | [Pydantic v2](https://docs.pydantic.dev/) |
| **Infrastructure** | [Docker](https://www.docker.com/) + [Docker Compose](https://docs.docker.com/compose/) |

---

## ðŸ—‚ï¸ Project Structure

```
scrapforge/
â”œâ”€â”€ docker-compose.yml          # All 4 services: Postgres, Redis, API, Worker
â”œâ”€â”€ Dockerfile                  # Python app image (Playwright-ready)
â”œâ”€â”€ requirements.txt            # Pinned dependencies
â”œâ”€â”€ .env                        # Local environment variables
â”‚
â”œâ”€â”€ alembic/                    # Database migration scripts
â”‚   â”œâ”€â”€ env.py
â”‚   â””â”€â”€ versions/               # Auto-generated migration files
â”‚
â”œâ”€â”€ core/
â”‚   â”œâ”€â”€ database.py             # SQLAlchemy engine & session factory
â”‚   â””â”€â”€ models.py               # ORM models: Retailer, Product, PriceHistory
â”‚
â”œâ”€â”€ scraper/
â”‚   â”œâ”€â”€ settings.py             # Scrapy + Playwright config
â”‚   â”œâ”€â”€ items.py                # Scrapy Items + Pydantic validation schema
â”‚   â”œâ”€â”€ middlewares.py          # User-Agent rotation (anti-bot)
â”‚   â”œâ”€â”€ pipelines.py            # Validation pipeline + PostgreSQL write pipeline
â”‚   â””â”€â”€ spiders/
â”‚       â”œâ”€â”€ ecommerce_spider.py # Playwright spider â†’ webscraper.io (electronics)
â”‚       â””â”€â”€ books_spider.py     # Fast HTTP spider â†’ books.toscrape.com (1,000 books)
â”‚
â”œâ”€â”€ worker/
â”‚   â”œâ”€â”€ celery_app.py           # Celery app config, Redis broker, Beat schedule
â”‚   â””â”€â”€ tasks.py                # 3 Celery tasks: ecommerce, books, full pipeline
â”‚
â”œâ”€â”€ api/
â”‚   â””â”€â”€ main.py                 # FastAPI router with all endpoints
â”‚
â””â”€â”€ docs/
    â””â”€â”€ screenshots/            # Pipeline documentation screenshots
```

---

## ðŸš€ Quick Start

### Prerequisites

Make sure you have the following installed:
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (includes Docker Compose)
