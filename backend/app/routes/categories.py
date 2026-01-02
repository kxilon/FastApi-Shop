from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from backend.app.database import get_db
from backend.app.schemas.category import CategoryResponse
from backend.app.services.category_service import CategoryService

router = APIRouter(
    prefix="/api/categories",
    tags=['categories']
)

@router.get("", response_model=List[CategoryResponse], status_code=status.HTTP_200_OK)
def get_categories(db: Session = Depends(get_db)):
    return CategoryService(db).get_all_categories()

@router.get("/{category_id}", response_model=CategoryResponse, status_code= status.HTTP_200_OK)
def get_category(category_id: int, db: Session = Depends(get_db)):
    return CategoryService(db).get_category_by_id(category_id)


    

