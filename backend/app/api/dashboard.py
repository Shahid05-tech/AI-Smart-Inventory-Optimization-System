from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database.dependencies import get_db

from app.models.product import Product
from app.models.store import Store
from app.models.supplier import Supplier
from app.models.inventory import Inventory
from app.models.sale import Sale

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/summary")
def dashboard_summary(
    db: Session = Depends(get_db)
):

    total_products = db.query(Product).count()

    total_stores = db.query(Store).count()

    total_suppliers = db.query(Supplier).count()

    avg_health = db.query(
        func.avg(
            Inventory.current_stock * 100.0 /
            Inventory.maximum_stock
        )
    ).scalar()

    if avg_health is None:
        avg_health = 0

    total_sales = (
        db.query(func.sum(Sale.revenue))
        .scalar()
    ) or 0

    low_stock = (
        db.query(Inventory)
        .filter(
            Inventory.current_stock <= Inventory.minimum_stock
        )
        .count()
    )

    return {
        "products": total_products,
        "stores": total_stores,
        "suppliers": total_suppliers,
        "inventory_health": round(avg_health, 2),
        "total_sales": round(float(total_sales), 2),
        "low_stock": low_stock,
    }