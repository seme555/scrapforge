import re
import scrapy
from pydantic import BaseModel, HttpUrl, Field, field_validator
from typing import Optional


class ProductValidator(BaseModel):
    name: str = Field(min_length=1)
    url: HttpUrl
    sku: str = Field(min_length=1)
