from sqlalchemy import (
    Column, Integer, String, Float, Boolean,
    DateTime, ForeignKey, Index, BigInteger, Text
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base


class Retailer(Base):
