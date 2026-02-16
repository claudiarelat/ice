from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database, models

router = APIRouter()

@router.get("/categories")
def get_categories(db: Session = Depends(database.get_db)):
    categories = db.query(models.Category).all()
    return [{"id": c.id, "name": c.name, "type": c.type.value} for c in categories]
