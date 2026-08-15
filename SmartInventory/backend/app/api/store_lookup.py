from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.store import Store
from app.models.product import Product

router = APIRouter(
    prefix="/lookup",
    tags=["Lookup"]
)


@router.get("/stores")
def get_stores(
    db: Session = Depends(get_db)
):
    stores = (
        db.query(Store)
        .order_by(Store.store_id)
        .all()
    )

    return [
        {
            "store_id": s.store_id,
            "store_name": s.store_name
        }
        for s in stores
    ]

@router.get("/products")
def get_products(
    db: Session = Depends(get_db)
):
    products = (
        db.query(Product)
        .order_by(Product.product_name)
        .all()
    )

    return [
        {
            "product_id": p.product_id,
            "product_name": p.product_name
        }
        for p in products
    ]