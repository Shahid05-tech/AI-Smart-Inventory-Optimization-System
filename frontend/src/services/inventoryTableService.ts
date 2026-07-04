import { api } from "../api/api";

export interface InventoryItem {

    inventory_id: number;

    store: string;

    product: string;

    current_stock: number;

    minimum_stock: number;

    maximum_stock: number;

    inventory_health: number;

    status: string;

}

export async function getInventory(): Promise<InventoryItem[]> {

    const response = await api.get<InventoryItem[]>("/inventory");

    return response.data;

}