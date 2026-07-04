from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.product import Product
from app.models.supplier import Supplier
from app.repositories.product_repository import ProductRepository
from app.schemas.product import ProductCreate


class ProductService:

    @staticmethod
    def create_product(db: Session, product: ProductCreate):

        supplier = db.query(Supplier).filter(
            Supplier.supplier_id == product.supplier_id
        ).first()

        if supplier is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Supplier not found"
            )

        new_product = Product(
            product_name=product.product_name,
            category=product.category,
            price=product.price,
            shelf_life_days=product.shelf_life_days,
            supplier_id=product.supplier_id
        )

        return ProductRepository.create(db, new_product)

    @staticmethod
    def get_products(
        db: Session,
        category: str | None,
        supplier_id: int | None,
        limit: int,
        offset: int,
    ):
        return ProductRepository.get_all(
            db,
            category,
            supplier_id,
            limit,
            offset,
        )