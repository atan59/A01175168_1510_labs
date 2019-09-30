from unittest import TestCase
from Lab04.roman_numbers import check_two_digits


class TestCheck_two_digits(TestCase):
    def test_check_two_digits_one(self):
        self.assertEqual(check_two_digits(1), 'I')

    def test_check_two_digits_four(self):
        self.assertEqual(check_two_digits(4), 'IV')

    def test_check_two_digits_five(self):
        self.assertEqual(check_two_digits(5), 'V')

    def test_check_two_digits_six(self):
        self.assertEqual(check_two_digits(6), 'VI')

    def test_check_two_digits_nine(self):
        self.assertEqual(check_two_digits(9), 'IX')

    def test_check_two_digits_ten(self):
        self.assertEqual(check_two_digits(10), 'X')

    def test_check_two_digits_twenty(self):
        self.assertEqual(check_two_digits(20), 'XX')

    def test_check_two_digits_forty(self):
        self.assertEqual(check_two_digits(40), 'XL')

    def test_check_two_digits_fifty(self):
        self.assertEqual(check_two_digits(50), 'L')

    def test_check_two_digits_sixty(self):
        self.assertEqual(check_two_digits(60), 'LX')

    def test_check_two_digits_ninety(self):
        self.assertEqual(check_two_digits(90), 'XC')
