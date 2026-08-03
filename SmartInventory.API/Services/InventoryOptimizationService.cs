using SmartInventory.API.DTOs;
using SmartInventory.API.Interfaces;

namespace SmartInventory.API.Services;

public class InventoryOptimizationService : IInventoryOptimizationService
{
    private readonly IDataCleaningService _cleaningService;
    private readonly IFeatureEngineeringService _featureService;

    public InventoryOptimizationService(
        IDataCleaningService cleaningService,
        IFeatureEngineeringService featureService)
    {
        _cleaningService = cleaningService;
        _featureService = featureService;
    }

    public List<InventoryRecommendationDto> GenerateRecommendations(
        List<SalesCsvDto> sales)
    {
        var cleaned = _cleaningService.Clean(sales);

        var features = _featureService.GenerateFeatures(cleaned.CleanData);

        var result = new List<InventoryRecommendationDto>();

        foreach (var item in features)
        {
            string demand;
            string recommendation;
            string priority;
            int restock;

            if (item.AverageDailySales >= 10)
            {
                demand = "High";
                recommendation = "Restock Immediately";
                priority = "Critical";
                restock = 50;
            }
            else if (item.AverageDailySales >= 5)
            {
                demand = "Medium";
                recommendation = "Monitor Inventory";
                priority = "Medium";
                restock = 25;
            }
            else
            {
                demand = "Low";
                recommendation = "Reduce Inventory";
                priority = "Low";
                restock = 10;
            }

            result.Add(new InventoryRecommendationDto
            {
                ProductName = item.ProductName,
                TotalQuantitySold = item.TotalQuantitySold,
                AverageDailySales = item.AverageDailySales,
                DemandLevel = demand,
                Recommendation = recommendation,
                SuggestedRestockQuantity = restock,
                Priority = priority
            });
        }

        return result;
    }
}