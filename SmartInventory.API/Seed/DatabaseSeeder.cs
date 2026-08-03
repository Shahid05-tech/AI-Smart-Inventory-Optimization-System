using SmartInventory.API.Data;
using SmartInventory.API.Models;

namespace SmartInventory.API.Seed;

public static class DatabaseSeeder
{
    public static void Seed(ApplicationDbContext context)
    {
        context.Database.EnsureCreated();

        if (context.Suppliers.Any())
            return;

        //--------------------------
        // Suppliers
        //--------------------------

        var suppliers = new List<Supplier>
        {
            new Supplier
            {
                SupplierName="Tech Distributors",
                Email="tech@example.com",
                Phone="9876543210"
            },

            new Supplier
            {
                SupplierName="Global Electronics",
                Email="global@example.com",
                Phone="9876543211"
            },

            new Supplier
            {
                SupplierName="Prime Supplies",
                Email="prime@example.com",
                Phone="9876543212"
            }
        };

        context.Suppliers.AddRange(suppliers);
        context.SaveChanges();

        //--------------------------
        // Stores
        //--------------------------

        var stores = new List<Store>
        {
            new Store
            {
                StoreName="Bangalore Store",
                City="Bangalore"
            },

            new Store
            {
                StoreName="Hyderabad Store",
                City="Hyderabad"
            },

            new Store
            {
                StoreName="Chennai Store",
                City="Chennai"
            }
        };

        context.Stores.AddRange(stores);
        context.SaveChanges();

        //--------------------------
        // Products
        //--------------------------

        var products = new List<Product>
        {
            new Product
            {
                ProductName="Laptop",
                Category="Electronics",
                UnitPrice=55000,
                SupplierId=1
            },

            new Product
            {
                ProductName="Mouse",
                Category="Electronics",
                UnitPrice=700,
                SupplierId=1
            },

            new Product
            {
                ProductName="Keyboard",
                Category="Electronics",
                UnitPrice=1500,
                SupplierId=2
            },

            new Product
            {
                ProductName="Monitor",
                Category="Electronics",
                UnitPrice=12000,
                SupplierId=2
            },

            new Product
            {
                ProductName="Printer",
                Category="Office",
                UnitPrice=18000,
                SupplierId=3
            }
        };

        context.Products.AddRange(products);
        context.SaveChanges();

        //--------------------------
        // Inventory
        //--------------------------

        var inventory = new List<Inventory>
        {
            new Inventory
            {
                ProductId=1,
                StoreId=1,
                CurrentStock=80,
                MinimumStock=20,
                MaximumStock=100
            },

            new Inventory
            {
                ProductId=2,
                StoreId=1,
                CurrentStock=45,
                MinimumStock=10,
                MaximumStock=60
            },

            new Inventory
            {
                ProductId=3,
                StoreId=2,
                CurrentStock=30,
                MinimumStock=15,
                MaximumStock=50
            },

            new Inventory
            {
                ProductId=4,
                StoreId=3,
                CurrentStock=18,
                MinimumStock=10,
                MaximumStock=40
            },

            new Inventory
            {
                ProductId=5,
                StoreId=2,
                CurrentStock=12,
                MinimumStock=5,
                MaximumStock=25
            }
        };

        context.Inventories.AddRange(inventory);
        context.SaveChanges();
    }
}