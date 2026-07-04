from datetime import date

from pydantic import BaseModel, Field


class StoreBase(BaseModel):
    store_name: str = Field(..., min_length=2, max_length=150)
    city: str = Field(..., min_length=2, max_length=100)
    state: str = Field(..., min_length=2, max_length=100)
    store_type: str = Field(..., min_length=2, max_length=50)
    opening_date: date


class StoreCreate(StoreBase):
    pass


class StoreResponse(StoreBase):
    store_id: int
    is_active: bool

    model_config = {
        "from_attributes": True
    }