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
