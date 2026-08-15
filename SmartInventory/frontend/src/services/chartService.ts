import { api } from "../api/api";

export interface SalesTrend {
    month: string;
    revenue: number;
}

export async function getSalesTrend(): Promise<SalesTrend[]> {

    const response = await api.get<SalesTrend[]>(
        "/charts/sales-trend"
    );

    return response.data;

}