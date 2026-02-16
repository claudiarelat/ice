from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database
from datetime import datetime

router = APIRouter()

@router.post("/transactions")
def create_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(database.get_db)):
    # Comprovar que l'usuari existeix
    user = db.query(models.User).filter(models.User.id == transaction.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Comprovar que la categoria existeix
    category = db.query(models.Category).filter(models.Category.id == transaction.category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    # Comprovar que type coincideix amb la categoria
    if category.type.value != transaction.type.value:
        raise HTTPException(status_code=400, detail="Transaction type does not match category type")

    db_transaction = models.Transaction(
        user_id=transaction.user_id,
        category_id=transaction.category_id,
        type=transaction.type,
        amount=transaction.amount,
        date=transaction.date,
        description=transaction.description
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return {"message": "Transaction created", "transaction": {
        "id": db_transaction.id,
        "user_id": db_transaction.user_id,
        "category_id": db_transaction.category_id,
        "type": db_transaction.type.value,
        "amount": float(db_transaction.amount),
        "date": str(db_transaction.date),
        "description": db_transaction.description
    }}

@router.get("/transactions")
def get_transactions(user_id: int, db: Session = Depends(database.get_db)):
    transactions = db.query(models.Transaction).filter(models.Transaction.user_id == user_id).all()
    return [
        {
            "id": t.id,
            "user_id": t.user_id,
            "category_id": t.category_id,
            "type": t.type.value,
            "amount": float(t.amount),
            "date": str(t.date),
            "created_at": str(t.created_at),
            "description": t.description
        }
        for t in transactions
    ]

@router.get("/transactions/{transaction_id}")
def get_transaction(transaction_id: int, db: Session = Depends(database.get_db)):
    t = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()
    if not t:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Transaction not found")
    return {
        "id": t.id,
        "user_id": t.user_id,
        "category_id": t.category_id,
        "type": t.type.value,
        "amount": float(t.amount),
        "date": str(t.date),
        "created_at": str(t.created_at),
        "description": t.description
    }

@router.delete("/transactions/{transaction_id}")
def delete_transaction(transaction_id: int, db: Session = Depends(database.get_db)):
    transaction = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    
    db.delete(transaction)
    db.commit()
    return {"message": f"Transaction {transaction_id} deleted successfully"}


@router.put("/transactions/{transaction_id}")
def update_transaction(
    transaction_id: int,
    updated_data: schemas.TransactionUpdate,
    db: Session = Depends(database.get_db)
):
    transaction = db.query(models.Transaction).filter(
        models.Transaction.id == transaction_id
    ).first()

    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")

    # Només actualitzar els camps que s'han enviat
    for field, value in updated_data.model_dump(exclude_unset=True).items():
        setattr(transaction, field, value)

    db.commit()
    db.refresh(transaction)

    return {
        "message": f"Transaction {transaction_id} updated successfully",
        "transaction": {
            "id": transaction.id,
            "user_id": transaction.user_id,
            "category_id": transaction.category_id,
            "type": transaction.type.value,
            "amount": float(transaction.amount),
            "date": str(transaction.date),
            "created_at": str(transaction.created_at),
            "description": transaction.description
        }
    }

