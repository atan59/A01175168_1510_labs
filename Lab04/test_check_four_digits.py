from unittest import TestCase
from Lab04.roman_numbers import check_four_digits


class TestCheck_four_digits(TestCase):
    def test_check_four_digits_one(self):
        self.assertEqual(check_four_digits(1), 'I')

    def test_check_four_digits_four(self):
        self.assertEqual(check_four_digits(4), 'IV')

    def test_check_four_digits_five(self):
        self.assertEqual(check_four_digits(5), 'V')

    def test_check_four_digits_six(self):
        self.assertEqual(check_four_digits(6), 'VI')

    def test_check_four_digits_nine(self):
        self.assertEqual(check_four_digits(9), 'IX')

    def test_check_four_digits_ten(self):
        self.assertEqual(check_four_digits(10), 'X')

    def test_check_four_digits_twenty(self):
        self.assertEqual(check_four_digits(20), 'XX')

    def test_check_four_digits_forty(self):
        self.assertEqual(check_four_digits(40), 'XL')

    def test_check_four_digits_fifty(self):
        self.assertEqual(check_four_digits(50), 'L')

    def test_check_four_digits_sixty(self):
        self.assertEqual(check_four_digits(60), 'LX')

    def test_check_four_digits_ninety(self):
        self.assertEqual(check_four_digits(90), 'XC')

    def test_check_four_digits_one_hundred(self):
        self.assertEqual(check_four_digits(100), 'C')

    def test_check_four_digits_four_hundred(self):
        self.assertEqual(check_four_digits(400), 'CD')

    def test_check_four_digits_five_hundred(self):
        self.assertEqual(check_four_digits(500), 'D')

    def test_check_four_digits_nine_hundred(self):
        self.assertEqual(check_four_digits(900), 'CM')

    def test_check_four_digits_one_thousand(self):
        self.assertEqual(check_four_digits(1000), 'M')

    def test_check_four_digits_five_thousand(self):
        self.assertEqual(check_four_digits(5000), 'MMMMM')
