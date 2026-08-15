import { api } from "../api/api";

export interface TopProduct {
    product: string;
    quantity: number;
}

export async function getTopProducts() {
    const response = await api.get<TopProduct[]>(
        "/analytics/top-products"
    );

    return response.data;
}