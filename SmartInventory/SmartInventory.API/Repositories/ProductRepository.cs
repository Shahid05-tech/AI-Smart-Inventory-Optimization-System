using SmartInventory.API.Data;
using SmartInventory.API.Interfaces;
using SmartInventory.API.Models;

namespace SmartInventory.API.Repositories;

public class ProductRepository
    : Repository<Product>,
      IProductRepository
{
    public ProductRepository(
        ApplicationDbContext context)
        : base(context)
    {

    }
}