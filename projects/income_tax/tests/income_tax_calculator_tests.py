import unittest

from projects.income_tax.income_tax_calculator import TaxCalculator


class TaxCalculatorTestCase(unittest.TestCase):
    def test_income_scale_1(self):
        self.assertEqual(TaxCalculator.calculate_tax(9999), 0)
        self.assertEqual(TaxCalculator.calculate_tax(10000), 0)

    def test_income_scale_2(self):
        self.assertEqual(TaxCalculator.calculate_tax(10001), 0.1)
        self.assertEqual(TaxCalculator.calculate_tax(19999), 999.9)

    def test_income_scale_3(self):
        self.assertEqual(TaxCalculator.calculate_tax(20000), 1000)
        self.assertEqual(TaxCalculator.calculate_tax(20001), 1000.2)
        self.assertEqual(TaxCalculator.calculate_tax(45000), 6000)
