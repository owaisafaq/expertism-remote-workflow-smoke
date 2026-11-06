import unittest

from greetings import greet


class GreetingTests(unittest.TestCase):
    def test_named_greeting(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")

    def test_empty_name(self):
        self.assertEqual(greet(""), "Hello, World!")

    def test_padded_name_is_trimmed(self):
        self.assertEqual(greet("  Ada  "), "Hello, Ada!")
        self.assertEqual(greet("\tAda\n"), "Hello, Ada!")

    def test_whitespace_only_name_uses_world(self):
        self.assertEqual(greet("   "), "Hello, World!")
        self.assertEqual(greet(" \t\n "), "Hello, World!")

    def test_internal_whitespace_is_preserved(self):
        self.assertEqual(greet("Mary Ann"), "Hello, Mary Ann!")
        self.assertEqual(greet("  Mary  Ann  "), "Hello, Mary  Ann!")


if __name__ == "__main__":
    unittest.main()
