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
