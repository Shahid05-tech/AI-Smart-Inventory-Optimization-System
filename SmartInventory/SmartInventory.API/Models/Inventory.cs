namespace SmartInventory.API.Models;

public class Inventory
{
    public int InventoryId { get; set; }

    public int ProductId { get; set; }

    public int StoreId { get; set; }

    public int CurrentStock { get; set; }

    public int MinimumStock { get; set; }

    public int MaximumStock { get; set; }

    public Product? Product { get; set; }

    public Store? Store { get; set; }
}