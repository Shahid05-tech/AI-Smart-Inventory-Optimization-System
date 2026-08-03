using Microsoft.AspNetCore.Mvc;
using SmartInventory.API.Interfaces;

namespace SmartInventory.API.Controllers;

[ApiController]
[Route("api/import")]
public class ImportController : ControllerBase
{
    private readonly ICsvImportService _csvService;

    public ImportController(ICsvImportService csvService)
    {
        _csvService = csvService;
    }

    [HttpGet]
    public async Task<IActionResult> Import()
    {
        var filePath = Path.Combine(
        Directory.GetCurrentDirectory(),
        "Imports",
        "sales.csv");
        var data = await _csvService.ImportSalesAsync(filePath);

        return Ok(data);
    }
}