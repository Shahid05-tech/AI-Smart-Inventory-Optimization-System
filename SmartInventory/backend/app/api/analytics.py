from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func, extract

from app.database.dependencies import get_db

from app.models.sale import Sale
from app.models.product import Product
from app.models.store import Store

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get("/monthly-revenue")
def monthly_revenue(
    db: Session = Depends(get_db)
):

    data = (

        db.query(

            extract("month", Sale.sale_date).label("month"),

            func.sum(Sale.revenue).label("revenue")

        )

        .group_by("month")

        .order_by("month")

        .all()

    )

    months = [

        "Jan","Feb","Mar","Apr","May","Jun",

        "Jul","Aug","Sep","Oct","Nov","Dec"

    ]

    return [

        {

            "month": months[int(row.month)-1],

            "revenue": float(row.revenue)

        }

        for row in data

    ]


@router.get("/category-revenue")
def category_revenue(
    db: Session = Depends(get_db)
):

    data = (

        db.query(

            Product.category,

            func.sum(Sale.revenue)

        )

        .join(

            Product,

            Sale.product_id == Product.product_id

        )

        .group_by(Product.category)

        .all()

    )

    return [

        {

            "category": row[0],

            "revenue": float(row[1])

        }

        for row in data

    ]


@router.get("/top-products")
def top_products(
    db: Session = Depends(get_db)
):

    data = (

        db.query(

            Product.product_name,

            func.sum(Sale.quantity_sold)

        )

        .join(

            Product,

            Sale.product_id == Product.product_id

        )

        .group_by(Product.product_name)

        .order_by(

            func.sum(Sale.quantity_sold).desc()

        )

        .limit(10)

        .all()

    )

    return [

        {

            "product": row[0],

            "quantity": int(row[1])

        }

        for row in data

    ]


@router.get("/top-stores")
def top_stores(
    db: Session = Depends(get_db)
):

    data = (

        db.query(

            Store.store_name,

            func.sum(Sale.revenue)

        )

        .join(

            Store,

            Sale.store_id == Store.store_id

        )

        .group_by(Store.store_name)

        .order_by(

            func.sum(Sale.revenue).desc()

        )

        .limit(10)

        .all()

    )

    return [

        {

            "store": row[0],

            "revenue": float(row[1])

        }

        for row in data

    ]


@router.get("/discount-summary")
def discount_summary(
    db: Session = Depends(get_db)
):

    avg_discount = db.query(

        func.avg(

            Sale.discount_percentage

        )

    ).scalar()

    return {

        "average_discount": round(

            float(avg_discount),

            2

        )

    }