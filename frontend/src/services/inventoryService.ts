import { api } from "../api/api";
import type {
    RecommendationRequest,
    RecommendationResponse,
} from "../types/inventory";

export async function getRecommendation(
    data: RecommendationRequest
): Promise<RecommendationResponse> {

    const response = await api.post<RecommendationResponse>(
        "/recommendation/",
        data
    );

    return response.data;
}