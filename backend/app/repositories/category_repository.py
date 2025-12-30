from typing import List
from sqlalchemy.orm import Session
from backend.app.models import Category


class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Category]:
        return self.db.query(Category).all()