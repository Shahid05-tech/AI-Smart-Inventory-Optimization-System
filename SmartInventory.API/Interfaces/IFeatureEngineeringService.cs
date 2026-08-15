using SmartInventory.API.DTOs;

namespace SmartInventory.API.Interfaces;

public interface IFeatureEngineeringService
{
    List<FeatureEngineeringDto> GenerateFeatures(List<SalesCsvDto> sales);
}