from unittest import TestCase
from Lab11.lab11 import factorial_recursive_helper


class TestFactorialRecursiveHelper(TestCase):
    def test_factorial_recursive_helper_0(self):
        expected = 1
        actual = factorial_recursive_helper(0)
        self.assertEqual(expected, actual)

    def test_factorial_recursive_helper_1(self):
        expected = 1
        actual = factorial_recursive_helper(1)
        self.assertEqual(expected, actual)

    def test_factorial_recursive_helper_5(self):
        expected = 120
        actual = factorial_recursive_helper(5)
        self.assertEqual(expected, actual)
