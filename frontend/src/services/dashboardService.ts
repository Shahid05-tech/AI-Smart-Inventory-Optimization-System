import { api } from "../api/api";

export interface DashboardSummary {
    products: number;
    stores: number;
    suppliers: number;
    inventory_health: number;
    total_sales: number;
    low_stock: number;
}

export async function getDashboardSummary(): Promise<DashboardSummary> {
    const response = await api.get<DashboardSummary>(
        "/dashboard/summary"
    );

    return response.data;
}