from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.models.sale import Sale
from app.models.store import Store
from app.models.product import Product

from app.repositories.sale_repository import SaleRepository

from app.schemas.sale import SaleCreate


class SaleService:

    @staticmethod
    def create_sale(
        db: Session,
        sale: SaleCreate
    ):

        store = (
            db.query(Store)
            .filter(Store.store_id == sale.store_id)
            .first()
        )

        if store is None:

            raise HTTPException(
                status_code=404,
                detail="Store not found"
            )

        product = (
            db.query(Product)
            .filter(Product.product_id == sale.product_id)
            .first()
        )

        if product is None:

            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        new_sale = Sale(

            sale_date=sale.sale_date,

            store_id=sale.store_id,

            product_id=sale.product_id,

            quantity_sold=sale.quantity_sold,

            revenue=sale.revenue,

            discount_percentage=sale.discount_percentage

        )

        return SaleRepository.create(
            db,
            new_sale
        )

    @staticmethod
    def get_sales(
        db: Session,
        limit,
        offset
    ):

        return SaleRepository.get_all(
            db,
            limit,
            offset
        )