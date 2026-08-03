using FluentValidation;
using SmartInventory.API.DTOs;

namespace SmartInventory.API.Validators;

public class ProductValidator : AbstractValidator<ProductDto>
{
    public ProductValidator()
    {
        RuleFor(x => x.ProductName)
            .NotEmpty()
            .MaximumLength(100);

        RuleFor(x => x.Category)
            .NotEmpty();

        RuleFor(x => x.UnitPrice)
            .GreaterThan(0);

        RuleFor(x => x.SupplierId)
            .GreaterThan(0);
    }
}