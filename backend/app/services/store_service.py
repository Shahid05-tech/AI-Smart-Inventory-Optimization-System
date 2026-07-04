from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.store import Store
from app.repositories.store_repository import StoreRepository
from app.schemas.store import StoreCreate


class StoreService:

    @staticmethod
    def create_store(db: Session, store: StoreCreate):

        existing = StoreRepository.get_by_name(
            db,
            store.store_name
        )

        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Store already exists"
            )

        new_store = Store(
            store_name=store.store_name,
            city=store.city,
            state=store.state,
            store_type=store.store_type,
            opening_date=store.opening_date,
        )

        return StoreRepository.create(
            db,
            new_store
        )

    @staticmethod
    def get_stores(
        db: Session,
        city: str | None,
        limit: int,
        offset: int,
    ):
        return StoreRepository.get_all(
            db,
            city,
            limit,
            offset,
        )