from pydantic import BaseModel, EmailStr, condecimal
from datetime import date, datetime
from decimal import Decimal
from typing import Optional
from enum import Enum
from .models import TransactionType

# --- Usuari ---
class UserCreate(BaseModel):
    email: EmailStr
    full_name: str
    timezone: Optional[str] = "UTC"  # camp opcional amb default

class User(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    timezone: str
    created_at: datetime
    closed_at: Optional[datetime]

    class Config:
        orm_mode = True

# --- Transaccions ---
class TransactionType(str, Enum):
    income = "income"
    expense = "expense"
    freeze = "freeze"

class TransactionCreate(BaseModel):
    user_id: int # Per l'MVP, l'usuari ha de passar el seu ID explícitament
    category_id: int
    type: TransactionType
    amount: condecimal(gt=0, max_digits=10, decimal_places=2)
    date: date
    description: Optional[str] = None

class TransactionUpdate(BaseModel):
    category_id: Optional[int]
    type: Optional[TransactionType]
    amount: Optional[condecimal(gt=0, max_digits=10, decimal_places=2)]
    date: Optional[date]
    description: Optional[str] = None





