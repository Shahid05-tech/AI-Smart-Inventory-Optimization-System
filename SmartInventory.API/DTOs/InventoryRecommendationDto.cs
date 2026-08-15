namespace SmartInventory.API.DTOs;

public class InventoryRecommendationDto
{
    public string ProductName { get; set; } = string.Empty;

    public int TotalQuantitySold { get; set; }

    public double AverageDailySales { get; set; }

    public string DemandLevel { get; set; } = string.Empty;

    public string Recommendation { get; set; } = string.Empty;

    public int SuggestedRestockQuantity { get; set; }

    public string Priority { get; set; } = string.Empty;
}