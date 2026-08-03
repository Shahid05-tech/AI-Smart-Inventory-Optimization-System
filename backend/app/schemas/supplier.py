from pydantic import BaseModel


class SupplierBase(BaseModel):
    supplier_name: str
    city: str
    country: str
    lead_time_days: int


class SupplierCreate(SupplierBase):
    pass


class SupplierResponse(SupplierBase):
    supplier_id: int

    model_config = {
        "from_attributes": True
    }