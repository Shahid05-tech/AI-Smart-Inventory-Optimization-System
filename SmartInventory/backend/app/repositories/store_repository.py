from sqlalchemy.orm import Session

from app.models.store import Store


class StoreRepository:

    @staticmethod
    def create(db: Session, store: Store):
        db.add(store)
        db.commit()
        db.refresh(store)
        return store

    @staticmethod
    def get_all(
        db: Session,
        city: str | None = None,
        limit: int = 20,
        offset: int = 0,
    ):
        query = db.query(Store)

        if city:
            query = query.filter(Store.city == city)

        return query.offset(offset).limit(limit).all()

    @staticmethod
    def get_by_name(db: Session, store_name: str):
        return (
            db.query(Store)
            .filter(Store.store_name == store_name)
            .first()
        )