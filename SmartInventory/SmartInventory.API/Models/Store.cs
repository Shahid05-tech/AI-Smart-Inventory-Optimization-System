namespace SmartInventory.API.Models;

public class Store
{
    public int StoreId { get; set; }

    public string StoreName { get; set; } = string.Empty;

    public string City { get; set; } = string.Empty;

    public ICollection<Inventory> Inventories { get; set; }
        = new List<Inventory>();

    public ICollection<Sale> Sales { get; set; }
        = new List<Sale>();
}