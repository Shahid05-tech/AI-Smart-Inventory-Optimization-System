from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.models.inventory import Inventory
from app.models.store import Store
from app.models.product import Product

from app.schemas.inventory import InventoryResponse

router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"]
)


@router.get(
    "/",
    response_model=list[InventoryResponse]
)
def get_inventory(
    db: Session = Depends(get_db)
):

    rows = (

        db.query(
            Inventory,
            Store.store_name,
            Product.product_name
        )

        .join(
            Store,
            Inventory.store_id == Store.store_id
        )

        .join(
            Product,
            Inventory.product_id == Product.product_id
        )

        .all()

    )

    result = []

    for inventory, store_name, product_name in rows:

        health = round(

            inventory.current_stock
            /
            inventory.maximum_stock
            * 100,

            2

        )

        status = (

            "Healthy"

            if inventory.current_stock >= inventory.minimum_stock

            else "Low Stock"

        )

        result.append(

            InventoryResponse(

                inventory_id=inventory.inventory_id,

                store=store_name,

                product=product_name,

                current_stock=inventory.current_stock,

                minimum_stock=inventory.minimum_stock,

                maximum_stock=inventory.maximum_stock,

                inventory_health=health,

                status=status

            )

        )

    return result