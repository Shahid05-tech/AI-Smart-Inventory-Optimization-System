export interface RecommendationRequest {
    store_id: number;
    product_id: number;
}

export interface RecommendationResponse {
    predicted_demand: number;
    safety_stock: number;
    recommended_stock: number;
    inventory_health: number;
    reorder_required: boolean;
}