from unittest import TestCase
from Lab11.lab11 import factorial_recursive


class TestFactorialRecursive(TestCase):
    def test_factorial_recursive_0(self):
        expected = (0, 1)
        actual = factorial_recursive(0)
        self.assertEqual(expected, actual)

    def test_factorial_recursive_1(self):
        expected = (1, 1)
        actual = factorial_recursive(1)
        self.assertEqual(expected, actual)

    def test_factorial_recursive_5(self):
        expected = (5, 120)
        actual = factorial_recursive(5)
        self.assertEqual(expected, actual)
