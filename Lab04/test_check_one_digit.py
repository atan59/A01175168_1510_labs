from unittest import TestCase
from Lab04.roman_numbers import check_one_digit


class TestCheck_one_digit(TestCase):
    def test_check_one_digit_one(self):
        self.assertEqual(check_one_digit(1), 'I')

    def test_check_one_digit_four(self):
        self.assertEqual(check_one_digit(4), 'IV')

    def test_check_one_digit_five(self):
        self.assertEqual(check_one_digit(5), 'V')

    def test_check_one_digit_six(self):
        self.assertEqual(check_one_digit(6), 'VI')

    def test_check_one_digit_nine(self):
        self.assertEqual(check_one_digit(9), 'IX')
