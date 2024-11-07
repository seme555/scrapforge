import re
import scrapy
from pydantic import BaseModel, HttpUrl, Field, field_validator
from typing import Optional


class ProductValidator(BaseModel):
    name: str = Field(min_length=1)
    url: HttpUrl
    sku: str = Field(min_length=1)
    price: Optional[float] = None
    currency: str = "USD"
    in_stock: bool
    category: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = None
    rating: Optional[float] = None
    review_count: Optional[int] = None
    retailer_name: str
    retailer_domain: str

    @field_validator("price")
    @classmethod
    def price_must_be_positive(cls, v):
        if v is not None and v < 0:
            raise ValueError("Price cannot be negative")
        return v

    @field_validator("rating")
    @classmethod
