using SmartInventory.API.DTOs;

namespace SmartInventory.API.Interfaces;

public interface IPythonPredictionService
{
    Task<PredictionResponseDto?> PredictAsync(PredictionRequestDto request);
}