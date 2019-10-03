from unittest import TestCase
from Lab04.roman_numbers import check_three_digits


class TestCheckThreeDigits(TestCase):
    def test_check_three_digits_one(self):
        self.assertEqual(check_three_digits(1), 'I')

    def test_check_three_digits_four(self):
        self.assertEqual(check_three_digits(4), 'IV')

    def test_check_three_digits_five(self):
        self.assertEqual(check_three_digits(5), 'V')

    def test_check_three_digits_six(self):
        self.assertEqual(check_three_digits(6), 'VI')

    def test_check_three_digits_nine(self):
        self.assertEqual(check_three_digits(9), 'IX')

    def test_check_three_digits_ten(self):
        self.assertEqual(check_three_digits(10), 'X')

    def test_check_three_digits_twenty(self):
        self.assertEqual(check_three_digits(20), 'XX')

    def test_check_three_digits_forty(self):
        self.assertEqual(check_three_digits(40), 'XL')

    def test_check_three_digits_fifty(self):
        self.assertEqual(check_three_digits(50), 'L')

    def test_check_three_digits_sixty(self):
        self.assertEqual(check_three_digits(60), 'LX')

    def test_check_three_digits_ninety(self):
        self.assertEqual(check_three_digits(90), 'XC')

    def test_check_three_digits_ninety_nine(self):
        self.assertEqual(check_three_digits(99), 'XCIX')

    def test_check_three_digits_one_hundred(self):
        self.assertEqual(check_three_digits(100), 'C')

    def test_check_three_digits_four_hundred(self):
        self.assertEqual(check_three_digits(400), 'CD')

    def test_check_three_digits_five_hundred(self):
        self.assertEqual(check_three_digits(500), 'D')

    def test_check_three_digits_nine_hundred(self):
        self.assertEqual(check_three_digits(900), 'CM')

    def test_check_three_digits_nine_hundred_ninety_nine(self):
        self.assertEqual(check_three_digits(999), 'CMXCIX')
