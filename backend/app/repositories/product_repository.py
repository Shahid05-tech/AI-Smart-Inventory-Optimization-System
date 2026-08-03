from sqlalchemy.orm import Session

from app.models.product import Product


class ProductRepository:

    @staticmethod
    def create(db: Session, product: Product) -> Product:
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    @staticmethod
    def get_all(
        db: Session,
        category: str | None = None,
        supplier_id: int | None = None,
        limit: int = 20,
        offset: int = 0,
    ):
        query = db.query(Product)

        if category:
            query = query.filter(Product.category == category)

        if supplier_id:
            query = query.filter(Product.supplier_id == supplier_id)

        return query.offset(offset).limit(limit).all()