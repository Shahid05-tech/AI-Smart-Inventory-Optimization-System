from pydantic import BaseModel


class InventoryResponse(BaseModel):
    inventory_id: int
    store: str
    product: str

    current_stock: int
    minimum_stock: int
    maximum_stock: int

    inventory_health: float

    status: str

    class Config:
        from_attributes = True