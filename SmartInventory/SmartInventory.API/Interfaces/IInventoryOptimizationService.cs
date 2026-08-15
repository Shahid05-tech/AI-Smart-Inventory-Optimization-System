using SmartInventory.API.DTOs;

namespace SmartInventory.API.Interfaces;

public interface IInventoryOptimizationService
{
    Task<List<InventoryRecommendationDto>> GenerateRecommendationsAsync(
        List<SalesCsvDto> sales);
}