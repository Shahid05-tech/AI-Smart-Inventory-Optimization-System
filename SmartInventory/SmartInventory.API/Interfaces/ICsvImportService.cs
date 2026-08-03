using SmartInventory.API.DTOs;

namespace SmartInventory.API.Interfaces;

public interface ICsvImportService
{
    Task<List<SalesCsvDto>> ImportSalesAsync(string filePath);
}