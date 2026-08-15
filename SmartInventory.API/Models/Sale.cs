namespace SmartInventory.API.Models;

public class Sale
{
    public int SaleId { get; set; }

    public int ProductId { get; set; }

    public int StoreId { get; set; }

    public int QuantitySold { get; set; }

    public decimal Revenue { get; set; }

    public DateTime SaleDate { get; set; }

    public Product? Product { get; set; }

    public Store? Store { get; set; }
}