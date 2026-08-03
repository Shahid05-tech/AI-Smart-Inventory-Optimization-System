using CsvHelper;
using CsvHelper.Configuration;
using Microsoft.AspNetCore.Http;
using SmartInventory.API.DTOs;
using SmartInventory.API.Interfaces;
using System.Globalization;

namespace SmartInventory.API.Services;

public class CsvImportService : ICsvImportService
{
    public async Task<List<SalesCsvDto>> ImportSalesAsync(IFormFile file)
    {
        using var stream = file.OpenReadStream();
        using var reader = new StreamReader(stream);

        var config = new CsvConfiguration(CultureInfo.InvariantCulture)
        {
            HeaderValidated = null,
            MissingFieldFound = null
        };

        using var csv = new CsvReader(reader, config);

        var records = csv.GetRecords<SalesCsvDto>().ToList();

        return await Task.FromResult(records);
    }
}