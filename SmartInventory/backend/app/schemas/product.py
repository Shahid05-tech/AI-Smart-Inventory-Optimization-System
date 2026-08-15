from decimal import Decimal
from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    product_name: str = Field(..., min_length=2, max_length=150)
    category: str = Field(..., min_length=2, max_length=50)
    price: Decimal = Field(..., gt=0)
    shelf_life_days: int = Field(..., ge=0)
    supplier_id: int


class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    product_id: int
    is_active: bool

    model_config = {
        "from_attributes": True
    }