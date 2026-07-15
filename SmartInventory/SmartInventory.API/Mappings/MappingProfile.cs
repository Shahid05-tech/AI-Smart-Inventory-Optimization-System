using AutoMapper;
using SmartInventory.API.DTOs;
using SmartInventory.API.Models;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace SmartInventory.API.Mappings;

public class MappingProfile : Profile
{
    public MappingProfile()
    {
        CreateMap<Product, ProductDto>().ReverseMap();
    }
}