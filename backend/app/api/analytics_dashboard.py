from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database.dependencies import get_db
from app.models.sale import Sale
from app.models.product import Product
from app.models.inventory import Inventory

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard Analytics"]
)


@router.get("/category-distribution")
def category_distribution(
    db: Session = Depends(get_db)
):

    data = (
        db.query(
            Product.category,
            func.sum(Sale.revenue)
        )
        .join(
            Product,
            Product.product_id == Sale.product_id
        )
        .group_by(Product.category)
        .all()
    )

    return [
        {
            "name": row[0],
            "value": float(row[1])
        }
        for row in data
    ]


@router.get("/inventory-health")
def inventory_health(
    db: Session = Depends(get_db)
):

    healthy = db.query(Inventory).filter(
        Inventory.current_stock >= Inventory.minimum_stock
    ).count()

    low = db.query(Inventory).filter(
        Inventory.current_stock < Inventory.minimum_stock
    ).count()

    return [
        {
            "name": "Healthy",
            "count": healthy
        },
        {
            "name": "Low Stock",
            "count": low
        }
    ]