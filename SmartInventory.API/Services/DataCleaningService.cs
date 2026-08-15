using SmartInventory.API.DTOs;
using SmartInventory.API.Interfaces;

namespace SmartInventory.API.Services;

public class DataCleaningService : IDataCleaningService
{
    public CleaningResultDto Clean(List<SalesCsvDto> sales)
    {
        var cleaned = sales
            .Where(x =>
                !string.IsNullOrWhiteSpace(x.ProductName) &&
                x.QuantitySold > 0 &&
                x.Revenue > 0)
            .ToList();

        return new CleaningResultDto
        {
            OriginalRows = sales.Count,
            CleanRows = cleaned.Count,
            RemovedRows = sales.Count - cleaned.Count,
            CleanData = cleaned
        };
    }
}