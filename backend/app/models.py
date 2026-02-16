from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Boolean, Date, DateTime, Numeric
from zoneinfo import ZoneInfo
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base
import enum

# Enum tipus transacció
class TransactionType(str, enum.Enum):
    income = "income"
    expense = "expense"
    freeze = "freeze"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=False)
    timezone = Column(String, default="UTC")  # nou camp
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(ZoneInfo("UTC")))
    closed_at = Column(DateTime(timezone=True), nullable=True)

    transactions = relationship("Transaction", back_populates="user")
    categories = relationship("Category", back_populates="user")

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(Enum(TransactionType), nullable=False)
    is_default = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="categories")
    transactions = relationship("Transaction", back_populates="category")

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    type = Column(Enum(TransactionType), nullable=False)
    amount = Column(Numeric(10,2), nullable=False)
    date = Column(Date, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="transactions")
    category = relationship("Category", back_populates="transactions")
