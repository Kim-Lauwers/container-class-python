from projects.income_tax.income_tax_calculator import TaxCalculator

__income: int = 45000

print("Given income", __income)
print("Total tax to pay is", TaxCalculator.calculate_tax(__income))
