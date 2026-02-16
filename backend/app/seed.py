from sqlalchemy.orm import Session
from . import models
from .database import engine, Base, SessionLocal

def seed_categories(db: Session):
    # Expense
    expense_categories = [
        "House", "Transport", "Toiletry", "Taxi", "Sports", "Pets", "Health",
        "Cosmetics", "Gifts", "Trips", "Studies", "Food", "Entertainment",
        "Eating Out", "Communications", "Clothes", "Car", "Bills", "Other"
    ]
    for name in expense_categories:
        db.add(models.Category(name=name, type=models.TransactionType.expense, is_default=True))

    # Income
    income_categories = ["Salary", "Sales", "Other"]
    for name in income_categories:
        db.add(models.Category(name=name, type=models.TransactionType.income, is_default=True))

    # Freeze
    db.add(models.Category(name="Frozen", type=models.TransactionType.freeze, is_default=True))

    db.commit()

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    seed_categories(db)
    db.close()
    print("Seed categories complete!")
