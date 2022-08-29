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

    def test_substract_calculator_integer(self):
        self.assertEqual(Calculator.substract(5, 5), 0)
        self.assertEqual(Calculator.substract(6, 5), 1)

    def test_substract_calculator_float(self):
        self.assertEqual(Calculator.substract(5.5, 5), 0.5)
        self.assertEqual(Calculator.substract(6, 4.5), 1.5)

    def test_multiply_calculator_integer(self):
        self.assertEqual(Calculator.multiply(5, 5), 25)
        self.assertEqual(Calculator.multiply(4, 5), 20)
        self.assertEqual(Calculator.multiply(7, 7), 49)

    def test_multiply_calculator_float(self):
        self.assertEqual(Calculator.multiply(5.5, 5), 27.5)
        self.assertEqual(Calculator.multiply(6, 5.5), 33)
        self.assertEqual(Calculator.multiply(6.5, 7.5), 48.75)

    def test_divide_calculator_integer(self):
        self.assertEqual(Calculator.divide(5, 5), 1)
        self.assertEqual(Calculator.divide(20, 5), 4)

    def test_divide_calculator_float(self):
        self.assertEqual(Calculator.divide(5, 2), 2.5)
        self.assertEqual(Calculator.divide(8, 3), 2.6666666666666665)
