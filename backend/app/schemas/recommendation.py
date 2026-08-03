from pydantic import BaseModel


class RecommendationRequest(BaseModel):
    store_id: int
    product_id: int


class RecommendationResponse(BaseModel):
    predicted_demand: float
    safety_stock: float
    recommended_stock: int
    inventory_health: int
    reorder_required: bool