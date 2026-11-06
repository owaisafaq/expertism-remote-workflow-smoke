import unittest

from greetings import greet


class GreetingTests(unittest.TestCase):
    def test_named_greeting(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")

    def test_empty_name(self):
        self.assertEqual(greet(""), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
