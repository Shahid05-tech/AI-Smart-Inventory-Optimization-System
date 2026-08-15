using Microsoft.AspNetCore.Mvc;
using SmartInventory.API.DTOs;
using SmartInventory.API.Interfaces;

namespace SmartInventory.API.Controllers;

[ApiController]
[Route("api/[controller]")]
public class InventoryOptimizationController : ControllerBase
{
    private readonly IInventoryOptimizationService _service;

    public InventoryOptimizationController(
        IInventoryOptimizationService service)
    {
        _service = service;
    }

    [HttpPost]
    public async Task<IActionResult> Generate(
        [FromBody] List<SalesCsvDto> sales)
    {
        var result = await _service
            .GenerateRecommendationsAsync(sales);

        return Ok(result);
    }
}