using AutoMapper;
using SmartInventory.API.DTOs;
using SmartInventory.API.Interfaces;
using SmartInventory.API.Models;

namespace SmartInventory.API.Services;

public class ProductService : IProductService
{
    private readonly IProductRepository _repository;
    private readonly IMapper _mapper;

    public ProductService(
        IProductRepository repository,
        IMapper mapper)
    {
        _repository = repository;
        _mapper = mapper;
    }

    public async Task<IEnumerable<ProductDto>> GetAllAsync()
    {
        var products = await _repository.GetAllAsync();
        return _mapper.Map<IEnumerable<ProductDto>>(products);
    }

    public async Task<ProductDto?> GetByIdAsync(int id)
    {
        var product = await _repository.GetByIdAsync(id);

        if (product == null)
            return null;

        return _mapper.Map<ProductDto>(product);
    }

    public async Task<ProductDto> CreateAsync(ProductDto dto)
    {
        var product = _mapper.Map<Product>(dto);

        await _repository.AddAsync(product);
        await _repository.SaveAsync();

        return _mapper.Map<ProductDto>(product);
    }

    public async Task<bool> UpdateAsync(int id, ProductDto dto)
    {
        var product = await _repository.GetByIdAsync(id);

        if (product == null)
            return false;

        _mapper.Map(dto, product);

        _repository.Update(product);

        await _repository.SaveAsync();

        return true;
    }

    public async Task<bool> DeleteAsync(int id)
    {
        var product = await _repository.GetByIdAsync(id);

        if (product == null)
            return false;

        _repository.Delete(product);

        await _repository.SaveAsync();

        return true;
    }
}