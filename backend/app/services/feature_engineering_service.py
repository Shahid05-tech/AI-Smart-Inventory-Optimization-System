from datetime import datetime

import pandas as pd
from sqlalchemy.orm import Session

from app.models.sale import Sale


class FeatureEngineeringService:

    @staticmethod
    def build_features(
        db: Session,
        store_id: int,
        product_id: int
    ):

        sales = (
            db.query(Sale)
            .filter(
                Sale.store_id == store_id,
                Sale.product_id == product_id
            )
            .order_by(Sale.sale_date)
            .all()
        )

        if len(sales) < 30:
            raise ValueError(
                "Not enough historical sales data."
            )

        df = pd.DataFrame([
            {
                "sale_date": s.sale_date,
                "quantity_sold": s.quantity_sold,
                "discount_percentage": float(s.discount_percentage),
            }
            for s in sales
        ])

        df["sale_date"] = pd.to_datetime(df["sale_date"])

        latest = df.iloc[-1]

        return {
            "store_id": store_id,
            "product_id": product_id,
            "day_of_week": latest["sale_date"].dayofweek,
            "month": latest["sale_date"].month,
            "quarter": latest["sale_date"].quarter,
            "weekend_flag": int(latest["sale_date"].dayofweek >= 5),
            "holiday_flag": 0,   # we'll connect the holiday table later
            "lag_1": df["quantity_sold"].iloc[-1],
            "lag_7": df["quantity_sold"].iloc[-7],
            "lag_30": df["quantity_sold"].iloc[-30],
            "rolling_7": df["quantity_sold"].tail(7).mean(),
            "rolling_30": df["quantity_sold"].tail(30).mean(),
            "discount_percentage": latest["discount_percentage"],
        }