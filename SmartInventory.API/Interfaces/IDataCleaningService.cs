using SmartInventory.API.DTOs;

namespace SmartInventory.API.Interfaces;

public interface IDataCleaningService
{
    CleaningResultDto Clean(List<SalesCsvDto> sales);
}