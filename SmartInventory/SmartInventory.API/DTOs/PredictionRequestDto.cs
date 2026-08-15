namespace SmartInventory.API.DTOs;

public class PredictionRequestDto
{
    public string ProductName { get; set; } = string.Empty;

    public string StoreName { get; set; } = string.Empty;

    public int QuantitySold { get; set; }

    public decimal Revenue { get; set; }

    public int StockAvailable { get; set; }

    public int LeadTimeDays { get; set; }

    public int Promotion { get; set; }

    public int Month { get; set; }

    public int DayOfWeek { get; set; }
}