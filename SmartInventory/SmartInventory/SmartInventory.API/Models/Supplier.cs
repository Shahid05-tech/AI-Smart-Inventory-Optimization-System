namespace SmartInventory.API.Models;

public class Supplier
{
    public int SupplierId { get; set; }

    public string SupplierName { get; set; } = string.Empty;

    public string Email { get; set; } = string.Empty;

    public string Phone { get; set; } = string.Empty;

    public ICollection<Product> Products { get; set; }
        = new List<Product>();
}