using Microsoft.AspNetCore.Mvc;
using SmartInventory.API.DTOs;
using SmartInventory.API.Interfaces;

namespace SmartInventory.API.Controllers;

[ApiController]
[Route("api/[controller]")]
public class FeatureEngineeringController : ControllerBase
{
    private readonly IFeatureEngineeringService _service;

    public FeatureEngineeringController(IFeatureEngineeringService service)
    {
        _service = service;
    }

    [HttpPost]
    public IActionResult Generate([FromBody] List<SalesCsvDto> sales)
    {
        var result = _service.GenerateFeatures(sales);
        return Ok(result);
    }
}