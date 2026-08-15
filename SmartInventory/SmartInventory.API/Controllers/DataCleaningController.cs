using Microsoft.AspNetCore.Mvc;
using SmartInventory.API.DTOs;
using SmartInventory.API.Interfaces;

namespace SmartInventory.API.Controllers;

[ApiController]
[Route("api/[controller]")]
public class DataCleaningController : ControllerBase
{
    private readonly IDataCleaningService _service;

    public DataCleaningController(IDataCleaningService service)
    {
        _service = service;
    }

    [HttpPost]
    public IActionResult Clean([FromBody] List<SalesCsvDto> sales)
    {
        var result = _service.Clean(sales);
        return Ok(result);
    }
}