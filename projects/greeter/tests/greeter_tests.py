import unittest

from projects.greeter.greeter import Greeter


class GreeterTestCase(unittest.TestCase):
    def test_default_greeting_set(self):
        greeter = Greeter()
        self.assertEqual(greeter.message, 'Hello world!')
