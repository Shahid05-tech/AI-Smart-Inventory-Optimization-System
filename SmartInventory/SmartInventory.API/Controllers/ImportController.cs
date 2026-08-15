using Microsoft.AspNetCore.Mvc;
using SmartInventory.API.Interfaces;

namespace SmartInventory.API.Controllers;

[ApiController]
[Route("api/[controller]")]
public class ImportController : ControllerBase
{
    private readonly ICsvImportService _csvService;

    public ImportController(ICsvImportService csvService)
    {
        _csvService = csvService;
    }

    [HttpPost]
    public async Task<IActionResult> Import(IFormFile file)
    {
        if (file == null || file.Length == 0)
            return BadRequest("No file uploaded.");

        var data = await _csvService.ImportSalesAsync(file);

        return Ok(data);
    }
}