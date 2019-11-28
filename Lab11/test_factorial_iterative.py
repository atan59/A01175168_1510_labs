from unittest import TestCase
from Lab11.lab11 import factorial_iterative


class TestFactorialIterative(TestCase):
    def test_factorial_iterative_0(self):
        expected = (0, 1)
        actual = factorial_iterative(0)
        self.assertEqual(expected, actual)

    def test_factorial_iterative_1(self):
        expected = (1, 1)
        actual = factorial_iterative(1)
        self.assertEqual(expected, actual)

    def test_factorial_iterative_5(self):
        expected = (5, 120)
        actual = factorial_iterative(5)
        self.assertEqual(expected, actual)
