namespace SmartInventory.API.DTOs;

public class FeatureEngineeringDto
{
    public string ProductName { get; set; } = string.Empty;

    public int TotalQuantitySold { get; set; }

    public decimal TotalRevenue { get; set; }

    public double AverageDailySales { get; set; }

    public decimal AverageRevenue { get; set; }
}