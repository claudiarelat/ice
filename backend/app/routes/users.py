from fastapi import APIRouter, Depends, HTTPException
from fastapi import Query
from sqlalchemy.orm import Session
from .. import database, models, schemas
from datetime import datetime
from zoneinfo import ZoneInfo

router = APIRouter()

@router.post("/users")
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    db_user = models.User(
        email=user.email,
        full_name=user.full_name,
        timezone=user.timezone,
        created_at=datetime.now(ZoneInfo("UTC"))
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {
        "message": "User created",
        "user": {
            "id": db_user.id,
            "email": db_user.email,
            "full_name": db_user.full_name,
            "timezone": db_user.timezone,
            "created_at": str(db_user.created_at)
        }
    }

@router.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "id": user.id,
        "email": user.email,
        "full_name": user.full_name,
        "created_at": str(user.created_at),
        "closed_at": str(user.closed_at) if user.closed_at else None
    }

@router.get("/users/{user_id}/summary")
def user_summary(
    user_id: int,
    month: int = Query(None, ge=1, le=12),
    year: int = Query(None, ge=2000),
    db: Session = Depends(database.get_db)
):
    # Comprovar que l'usuari existeix
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Zona horària de l'usuari
    user_tz = ZoneInfo(user.timezone)
    now_local = datetime.now(user_tz)

    if not month:
        month = now_local.month
    if not year:
        year = now_local.year

    # Filtrar transaccions d'aquest mes
    transactions = db.query(models.Transaction).join(models.Category).filter(
        models.Transaction.user_id == user_id,
        func.extract('month', models.Transaction.date) == month,
        func.extract('year', models.Transaction.date) == year
    ).all()

    summary = {
        "month": month,
        "year": year,
        "income": 0,
        "expense": 0,
        "frozen": 0,
        "balance": 0,
        "total_saved": 0,  # nous diners congelats
        "totals_by_category": {},
        "percent_by_category": {}
    }

    for t in transactions:
        amount = float(t.amount)
        cat_name = t.category.name

        if t.type.value == "income":
            summary["income"] += amount
        elif t.type.value == "expense":
            summary["expense"] += amount
            # totals per category només per expenses
            if cat_name not in summary["totals_by_category"]:
                summary["totals_by_category"][cat_name] = 0
            summary["totals_by_category"][cat_name] += amount
        elif t.type.value == "freeze":
            summary["frozen"] += amount
            summary["total_saved"] += amount  # diners moguts a frozen

    # calcular balance
    summary["balance"] = summary["income"] - summary["expense"] - summary["frozen"]

    # calcular percentatges per categoria només sobre despeses
    total_expense = summary["expense"]
    for cat, val in summary["totals_by_category"].items():
        summary["percent_by_category"][cat] = round((val / total_expense) * 100, 2) if total_expense > 0 else 0

    return summary
