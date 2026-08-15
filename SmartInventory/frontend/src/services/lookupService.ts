import { api } from "../api/api";

export interface Store {
    store_id: number;
    store_name: string;
}

export interface Product {
    product_id: number;
    product_name: string;
}

export async function getStores(): Promise<Store[]> {

    const response = await api.get("/lookup/stores");

    return response.data;

}

export async function getProducts(): Promise<Product[]> {

    const response = await api.get("/lookup/products");

    return response.data;

}