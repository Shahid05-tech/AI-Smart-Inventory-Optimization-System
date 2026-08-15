using System.Net.Http.Json;
using SmartInventory.API.DTOs;
using SmartInventory.API.Interfaces;

namespace SmartInventory.API.Services;

public class PythonPredictionService : IPythonPredictionService
{
    private readonly HttpClient _httpClient;

    public PythonPredictionService(HttpClient httpClient)
    {
        _httpClient = httpClient;
    }

    public async Task<PredictionResponseDto?> PredictAsync(
        PredictionRequestDto request)
    {
        var response = await _httpClient.PostAsJsonAsync(
            "predict",
            request);

        if (!response.IsSuccessStatusCode)
        {
            return null;
        }

        return await response.Content
            .ReadFromJsonAsync<PredictionResponseDto>();
    }
}