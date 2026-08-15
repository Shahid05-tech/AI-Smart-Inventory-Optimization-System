namespace SmartInventory.API.Models;

public class Recommendation
{
    public int RecommendationId { get; set; }

    public int ProductId { get; set; }

    public string RecommendationText { get; set; } = string.Empty;

    public double PredictedDemand { get; set; }

    public DateTime GeneratedOn { get; set; } = DateTime.UtcNow;

    public Product? Product { get; set; }
}