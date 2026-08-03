using SmartInventory.API.DTOs;
using SmartInventory.API.Interfaces;

namespace SmartInventory.API.Services;

public class FeatureEngineeringService : IFeatureEngineeringService
{
    public List<FeatureEngineeringDto> GenerateFeatures(List<SalesCsvDto> sales)
    {
        return sales
            .GroupBy(x => x.ProductName)
            .Select(g => new FeatureEngineeringDto
            {
                ProductName = g.Key,

                TotalQuantitySold = g.Sum(x => x.QuantitySold),

                TotalRevenue = g.Sum(x => x.Revenue),

                AverageDailySales = g.Average(x => x.QuantitySold),

                AverageRevenue = g.Average(x => x.Revenue)
            })
            .ToList();
    }
}