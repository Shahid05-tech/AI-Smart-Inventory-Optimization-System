using SmartInventory.API.DTOs;

namespace SmartInventory.API.Interfaces;

public interface IInventoryOptimizationService
{
    List<InventoryRecommendationDto> GenerateRecommendations(List<SalesCsvDto> sales);
}