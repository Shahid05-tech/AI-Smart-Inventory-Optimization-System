using CsvHelper;
using CsvHelper.Configuration;
using SmartInventory.API.DTOs;
using SmartInventory.API.Interfaces;
using System.Formats.Asn1;
using System.Globalization;

namespace SmartInventory.API.Services;

public class CsvImportService : ICsvImportService
{
    public async Task<List<SalesCsvDto>> ImportSalesAsync(string filePath)
    {
        using var reader = new StreamReader(filePath);

        using var csv = new CsvReader(
            reader,
            new CsvConfiguration(CultureInfo.InvariantCulture)
            {
                HeaderValidated = null,
                MissingFieldFound = null
            });

        var records = csv.GetRecords<SalesCsvDto>().ToList();

        return await Task.FromResult(records);
    }
}