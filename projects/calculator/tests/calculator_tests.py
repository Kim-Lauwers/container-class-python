import unittest

from projects.calculator.calculator import Calculator


class CalculatorTestCase(unittest.TestCase):
    def test_sum_calculator_integer(self):
        self.assertEqual(Calculator.sum(5, 5), 10)
        self.assertEqual(Calculator.sum(6, 5), 11)
        self.assertEqual(Calculator.sum(6, 7), 13)

    def test_sum_calculator_float(self):
        self.assertEqual(Calculator.sum(5.5, 5), 10.5)
        self.assertEqual(Calculator.sum(6, 5.5), 11.5)
        self.assertEqual(Calculator.sum(6.5, 7.5), 14)
