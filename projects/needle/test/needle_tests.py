import unittest

from projects.needle.needle_finder import NeedleFinder


class NeedleTestCase(unittest.TestCase):
    def test_needle_found(self):
        self.assertEqual(NeedleFinder.find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]), 'found the needle at position 3')
        self.assertEqual(NeedleFinder.find_needle(
            ['283497238987234', 'a dog', 'a cat', 'some random junk', 'a piece of hay', 'needle', 'something somebody lost a while ago']),
            'found the needle at position 5')
        self.assertEqual(NeedleFinder.find_needle(
            [1, 2, 3, 4, 5, 6, 7, 8, 8, 7, 5, 4, 3, 4, 5, 6, 67, 5, 5, 3, 3, 4, 2, 34, 234, 23, 4, 234, 324, 324, 'needle', 1, 2, 3, 4, 5, 5, 6, 5, 4, 32, 3,
             45, 54]), 'found the needle at position 30')

    def test_needle_not_found(self):
        self.assertEqual(NeedleFinder.find_needle(['3', '123124234', None, 'world', 'hay', 2, '3', True, False]), 'no needle in the haystack')

    def test_needle_empty(self):
        self.assertEqual(NeedleFinder.find_needle([]), 'No haystack found')
        self.assertEqual(NeedleFinder.find_needle(None), 'No haystack found')
