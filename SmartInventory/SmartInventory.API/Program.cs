using FluentValidation;
using Microsoft.EntityFrameworkCore;
using SmartInventory.API.Data;
using SmartInventory.API.Interfaces;
using SmartInventory.API.Mappings;
using SmartInventory.API.Middleware;
using SmartInventory.API.Repositories;
using SmartInventory.API.Seed;
using SmartInventory.API.Services;
using SmartInventory.API.Validators;
using SmartInventory.API.DTOs;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllers();

builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

// Database
builder.Services.AddDbContext<ApplicationDbContext>(options =>
    options.UseSqlServer(
        builder.Configuration.GetConnectionString("DefaultConnection")));

// Repository Dependency Injection
builder.Services.AddScoped<IProductRepository, ProductRepository>();

// Service Dependency Injection
builder.Services.AddScoped<IProductService, ProductService>();

// AutoMapper
builder.Services.AddAutoMapper(typeof(MappingProfile));

// FluentValidation
builder.Services.AddValidatorsFromAssemblyContaining<ProductValidator>();
builder.Services.AddScoped<IDashboardService, DashboardService>();
builder.Services.AddScoped<ICsvImportService, CsvImportService>();
builder.Services.AddScoped<IDataCleaningService, DataCleaningService>();
builder.Services.AddScoped<IFeatureEngineeringService, FeatureEngineeringService>();
builder.Services.AddScoped<IInventoryOptimizationService, InventoryOptimizationService>();
builder.Services.AddHttpClient<IPythonPredictionService, PythonPredictionService>(
    client =>
    {
        client.BaseAddress = new Uri("http://127.0.0.1:5000/");
        client.Timeout = TimeSpan.FromSeconds(30);
    });
var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}
using (var scope = app.Services.CreateScope())
{
    var context = scope.ServiceProvider
        .GetRequiredService<ApplicationDbContext>();

    DatabaseSeeder.Seed(context);
}
// Global Exception Middleware
app.UseMiddleware<ExceptionMiddleware>();

app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

app.Run();