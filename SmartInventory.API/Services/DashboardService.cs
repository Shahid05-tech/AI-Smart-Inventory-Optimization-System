using Microsoft.EntityFrameworkCore;
using SmartInventory.API.Data;
using SmartInventory.API.DTOs;
using SmartInventory.API.Interfaces;

namespace SmartInventory.API.Services;

public class DashboardService : IDashboardService
{
    private readonly ApplicationDbContext _context;

    public DashboardService(ApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<DashboardDto> GetSummaryAsync()
    {
        var products = await _context.Products.CountAsync();

        var suppliers = await _context.Suppliers.CountAsync();

        var stores = await _context.Stores.CountAsync();

        double inventoryHealth = 0;

        if (await _context.Inventories.AnyAsync())
        {
            inventoryHealth =
                await _context.Inventories
                .AverageAsync(i =>
                    (double)i.CurrentStock /
                    i.MaximumStock * 100);
        }

        return new DashboardDto
        {
            TotalProducts = products,
            TotalSuppliers = suppliers,
            TotalStores = stores,
            InventoryHealth = Math.Round(inventoryHealth, 2)
        };
    }
}