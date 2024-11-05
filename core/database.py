import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv(override=False)  # Don't override existing container env vars

POSTGRES_USER = os.getenv("POSTGRES_USER", "scraper_user")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "scraper_pass")
POSTGRES_DB = os.getenv("POSTGRES_DB", "scraper_db")
