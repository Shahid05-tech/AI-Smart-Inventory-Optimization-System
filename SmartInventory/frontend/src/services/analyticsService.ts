import { api } from "../api/api";

export interface MonthlyRevenue {
    month: string;
    revenue: number;
}

export interface CategoryRevenue {
    category: string;
    revenue: number;
}

export interface TopProduct {
    product: string;
    quantity: number;
}

export interface TopStore {
    store: string;
    revenue: number;
}

export interface DiscountSummary {
    average_discount: number;
}

export async function getMonthlyRevenue() {
    const response = await api.get<MonthlyRevenue[]>(
        "/analytics/monthly-revenue"
    );

    return response.data;
}

export async function getCategoryRevenue() {
    const response = await api.get<CategoryRevenue[]>(
        "/analytics/category-revenue"
    );

    return response.data;
}

export async function getTopProducts() {
    const response = await api.get<TopProduct[]>(
        "/analytics/top-products"
    );

    return response.data;
}

export async function getTopStores() {
    const response = await api.get<TopStore[]>(
        "/analytics/top-stores"
    );

    return response.data;
}

export async function getDiscountSummary() {
    const response = await api.get<DiscountSummary>(
        "/analytics/discount-summary"
    );

    return response.data;
}