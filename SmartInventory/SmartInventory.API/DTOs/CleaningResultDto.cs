namespace SmartInventory.API.DTOs;

public class CleaningResultDto
{
    public int OriginalRows { get; set; }

    public int CleanRows { get; set; }

    public int RemovedRows { get; set; }

    public List<SalesCsvDto> CleanData { get; set; } = new();
}