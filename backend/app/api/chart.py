from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func, extract

from app.database.dependencies import get_db
from app.models.sale import Sale

router = APIRouter(
    prefix="/charts",
    tags=["Charts"]
)


@router.get("/sales-trend")
def sales_trend(
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
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]

    return [
        {
            "month": months[int(row.month) - 1],
            "revenue": float(row.revenue)
        }
        for row in data
    ]