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

    def test_multiply_calculator_integer(self):
        self.assertEqual(Calculator.multiply(5, 5), 25)
        self.assertEqual(Calculator.multiply(4, 5), 20)
        self.assertEqual(Calculator.multiply(7, 7), 49)

    def test_multiply_calculator_float(self):
        self.assertEqual(Calculator.multiply(5.5, 5), 27.5)
        self.assertEqual(Calculator.multiply(6, 5.5), 33)
        self.assertEqual(Calculator.multiply(6.5, 7.5), 48.75)
