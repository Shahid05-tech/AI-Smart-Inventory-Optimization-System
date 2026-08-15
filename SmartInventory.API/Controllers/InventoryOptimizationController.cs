using Microsoft.AspNetCore.Mvc;
using SmartInventory.API.DTOs;
using SmartInventory.API.Interfaces;

namespace SmartInventory.API.Controllers;

[ApiController]
[Route("api/[controller]")]
public class InventoryOptimizationController : ControllerBase
{
    private readonly IInventoryOptimizationService _service;

    public InventoryOptimizationController(IInventoryOptimizationService service)
    {
        _service = service;
    }

    [HttpPost]
    public IActionResult Generate([FromBody] List<SalesCsvDto> sales)
    {
        var result = _service.GenerateRecommendations(sales);
        return Ok(result);
    }
}