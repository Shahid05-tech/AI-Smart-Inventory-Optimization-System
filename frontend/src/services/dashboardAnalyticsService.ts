import { api } from "../api/api";

export interface CategoryDistribution {
    name: string;
    value: number;
}

export interface InventoryHealth {
    name: string;
    count: number;
}

export async function getCategoryDistribution() {
    const response = await api.get<CategoryDistribution[]>(
        "/dashboard/category-distribution"
    );

    return response.data;
}

export async function getInventoryHealth() {
    const response = await api.get<InventoryHealth[]>(
        "/dashboard/inventory-health"
    );

    return response.data;
}