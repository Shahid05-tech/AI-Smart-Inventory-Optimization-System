using SmartInventory.API.DTOs;
using SmartInventory.API.Interfaces;

namespace SmartInventory.API.Services;

public class InventoryOptimizationService : IInventoryOptimizationService
{
    private readonly IDataCleaningService _cleaningService;
    private readonly IFeatureEngineeringService _featureService;
    private readonly IPythonPredictionService _predictionService;

    public InventoryOptimizationService(
        IDataCleaningService cleaningService,
        IFeatureEngineeringService featureService,
        IPythonPredictionService predictionService)
    {
        _cleaningService = cleaningService;
        _featureService = featureService;
        _predictionService = predictionService;
    }

    public async Task<List<InventoryRecommendationDto>> GenerateRecommendationsAsync(
        List<SalesCsvDto> sales)
    {
        var cleaningResult = _cleaningService.Clean(sales);

        var cleanedSales = cleaningResult.CleanData;

        var features = _featureService.GenerateFeatures(cleanedSales);

        var recommendations = new List<InventoryRecommendationDto>();

        foreach (var item in features)
        {
            var representativeSale = cleanedSales
                .Where(x => x.ProductName == item.ProductName)
                .OrderByDescending(x => x.SaleDate)
                .FirstOrDefault();

            if (representativeSale == null)
                continue;

            var predictionRequest = new PredictionRequestDto
            {
                ProductName = representativeSale.ProductName,
                StoreName = representativeSale.StoreName,
                QuantitySold = representativeSale.QuantitySold,
                Revenue = representativeSale.Revenue,
                StockAvailable = 50,
                LeadTimeDays = 3,
                Promotion = 0,
                Month = representativeSale.SaleDate.Month,
                DayOfWeek = (int)representativeSale.SaleDate.DayOfWeek
            };

            var prediction = await _predictionService
                .PredictAsync(predictionRequest);

            var demand = prediction?.PredictedDemand ?? "Unknown";

            string recommendation;
            string priority;
            int restock;

            switch (demand)
            {
                case "High":
                    recommendation = "Restock Immediately";
                    priority = "Critical";
                    restock = 50;
                    break;

                case "Medium":
                    recommendation = "Monitor Inventory";
                    priority = "Medium";
                    restock = 25;
                    break;

                case "Low":
                    recommendation = "Reduce Inventory";
                    priority = "Low";
                    restock = 10;
                    break;

                default:
                    recommendation = "Review Inventory";
                    priority = "Low";
                    restock = 10;
                    break;
            }

            recommendations.Add(new InventoryRecommendationDto
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

        return recommendations;
    }
}