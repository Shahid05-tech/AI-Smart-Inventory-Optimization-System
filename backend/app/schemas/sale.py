from datetime import date
from decimal import Decimal

from pydantic import BaseModel, Field


class SaleBase(BaseModel):

    sale_date: date

    store_id: int

    product_id: int

    quantity_sold: int = Field(..., gt=0)

    revenue: Decimal

    discount_percentage: Decimal = 0


class SaleCreate(SaleBase):
    pass


class SaleResponse(SaleBase):

    sale_id: int

    model_config = {
        "from_attributes": True
    }