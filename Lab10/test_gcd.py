from unittest import TestCase
from Lab10.question_2 import gcd


class TestGcd(TestCase):
    def test_gcd_a_equal_to_b(self):
        expected = 2
        actual = gcd(2, 2)
        self.assertEqual(expected, actual)

    def test_gcd_a_greater_than_b(self):
        expected = 2
        actual = gcd(4, 2)
        self.assertEqual(expected, actual)

    def test_gcd_b_greater_than_a(self):
        expected = 2
        actual = gcd(2, 4)
        self.assertEqual(expected, actual)

    def test_gcd_a_positive_b_negative(self):
        expected = -2
        actual = gcd(4, -2)
        self.assertEqual(expected, actual)

    def test_gcd_a_negative_b_positive(self):
        expected = 2
        actual = gcd(-4, 2)
        self.assertEqual(expected, actual)

    def test_gcd_both_negative(self):
        expected = -2
        actual = gcd(-4, -2)
        self.assertEqual(expected, actual)
