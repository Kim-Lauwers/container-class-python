import unittest

from projects.divable.divisible import Divisible


class DivableTestCase(unittest.TestCase):
    def test_is_divable(self):
        self.assertEqual(Divisible.is_divisible_by(5, 5), True)
        self.assertEqual(Divisible.is_divisible_by(10, 5), True)

    def test_is_not_divable(self):
        self.assertEqual(Divisible.is_divisible_by(5, 6), False)
        self.assertEqual(Divisible.is_divisible_by(10, 6), False)
