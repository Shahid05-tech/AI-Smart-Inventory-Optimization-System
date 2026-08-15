using SmartInventory.API.DTOs;

namespace SmartInventory.API.Interfaces;

public interface IDashboardService
{
    Task<DashboardDto> GetSummaryAsync();
}