using Microsoft.EntityFrameworkCore;
using SmartInventory.API.Models;

namespace SmartInventory.API.Data;

public class ApplicationDbContext : DbContext
{
    public ApplicationDbContext(
        DbContextOptions<ApplicationDbContext> options)
        : base(options)
    {
    }

    public DbSet<Product> Products => Set<Product>();

    public DbSet<Supplier> Suppliers => Set<Supplier>();

    public DbSet<Store> Stores => Set<Store>();

    public DbSet<Inventory> Inventories => Set<Inventory>();

    public DbSet<Sale> Sales => Set<Sale>();

    public DbSet<Recommendation> Recommendations => Set<Recommendation>();

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        base.OnModelCreating(modelBuilder);

        //---------------------------------
        // Product
        //---------------------------------

        modelBuilder.Entity<Product>()
            .HasKey(p => p.ProductId);

        modelBuilder.Entity<Product>()
            .Property(p => p.UnitPrice)
            .HasPrecision(18, 2);

        modelBuilder.Entity<Product>()
            .HasOne(p => p.Supplier)
            .WithMany(s => s.Products)
            .HasForeignKey(p => p.SupplierId);

        //---------------------------------
        // Supplier
        //---------------------------------

        modelBuilder.Entity<Supplier>()
            .HasKey(s => s.SupplierId);

        //---------------------------------
        // Store
        //---------------------------------

        modelBuilder.Entity<Store>()
            .HasKey(s => s.StoreId);

        //---------------------------------
        // Inventory
        //---------------------------------

        modelBuilder.Entity<Inventory>()
            .HasKey(i => i.InventoryId);

        modelBuilder.Entity<Inventory>()
            .HasOne(i => i.Product)
            .WithMany(p => p.Inventories)
            .HasForeignKey(i => i.ProductId);

        modelBuilder.Entity<Inventory>()
            .HasOne(i => i.Store)
            .WithMany(s => s.Inventories)
            .HasForeignKey(i => i.StoreId);

        //---------------------------------
        // Sale
        //---------------------------------

        modelBuilder.Entity<Sale>()
            .HasKey(s => s.SaleId);

        modelBuilder.Entity<Sale>()
            .Property(s => s.Revenue)
            .HasPrecision(18, 2);

        modelBuilder.Entity<Sale>()
            .HasOne(s => s.Product)
            .WithMany(p => p.Sales)
            .HasForeignKey(s => s.ProductId);

        modelBuilder.Entity<Sale>()
            .HasOne(s => s.Store)
            .WithMany(st => st.Sales)
            .HasForeignKey(s => s.StoreId);

        //---------------------------------
        // Recommendation
        //---------------------------------

        modelBuilder.Entity<Recommendation>()
            .HasKey(r => r.RecommendationId);

        modelBuilder.Entity<Recommendation>()
            .HasOne(r => r.Product)
            .WithMany()
            .HasForeignKey(r => r.ProductId);
    }
}