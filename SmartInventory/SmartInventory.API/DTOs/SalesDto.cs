namespace SmartInventory.API.DTOs;

public class SalesCsvDto
{
    public DateTime SaleDate { get; set; }

    public string ProductName { get; set; } = string.Empty;

    public string StoreName { get; set; } = string.Empty;

    public int QuantitySold { get; set; }

    public decimal Revenue { get; set; }
}