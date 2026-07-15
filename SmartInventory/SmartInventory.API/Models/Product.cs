namespace SmartInventory.API.Models;

public class Product
{
    public int ProductId { get; set; }

    public string ProductName { get; set; } = string.Empty;

    public string Category { get; set; } = string.Empty;

    public decimal UnitPrice { get; set; }

    public int SupplierId { get; set; }

    public Supplier? Supplier { get; set; }

    public ICollection<Inventory> Inventories { get; set; }
        = new List<Inventory>();

    public ICollection<Sale> Sales { get; set; }
        = new List<Sale>();
}