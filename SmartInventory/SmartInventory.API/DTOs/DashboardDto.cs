namespace SmartInventory.API.DTOs;

public class DashboardDto
{
    public int TotalProducts { get; set; }

    public int TotalSuppliers { get; set; }

    public int TotalStores { get; set; }

    public double InventoryHealth { get; set; }
}