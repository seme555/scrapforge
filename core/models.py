from sqlalchemy import (
    Column, Integer, String, Float, Boolean,
    DateTime, ForeignKey, Index, BigInteger, Text
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base


class Retailer(Base):
    """Stores information about the store being scraped."""
    __tablename__ = "retailers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False, index=True)
    domain = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    products = relationship("Product", back_populates="retailer", cascade="all, delete")

