from unittest import TestCase
from Lab04.roman_numbers import convert_to_roman_numeral


class TestConvertToRomanNumeral(TestCase):
    def test_convert_to_roman_numeral_one(self):
        self.assertEqual(convert_to_roman_numeral(1), 'I')

    def test_convert_to_roman_numeral_four(self):
        self.assertEqual(convert_to_roman_numeral(4), 'IV')

    def test_convert_to_roman_numeral_five(self):
        self.assertEqual(convert_to_roman_numeral(5), 'V')

    def test_convert_to_roman_numeral_six(self):
        self.assertEqual(convert_to_roman_numeral(6), 'VI')

    def test_convert_to_roman_numeral_nine(self):
        self.assertEqual(convert_to_roman_numeral(9), 'IX')

    def test_convert_to_roman_numeral_ten(self):
        self.assertEqual(convert_to_roman_numeral(10), 'X')

    def test_convert_to_roman_numeral_twenty(self):
        self.assertEqual(convert_to_roman_numeral(20), 'XX')

    def test_convert_to_roman_numeral_forty(self):
        self.assertEqual(convert_to_roman_numeral(40), 'XL')

    def test_convert_to_roman_numeral_fifty(self):
        self.assertEqual(convert_to_roman_numeral(50), 'L')

    def test_convert_to_roman_numeral_sixty(self):
        self.assertEqual(convert_to_roman_numeral(60), 'LX')

    def test_convert_to_roman_numeral_ninety(self):
        self.assertEqual(convert_to_roman_numeral(90), 'XC')

    def test_convert_to_roman_numeral_ninety_nine(self):
        self.assertEqual(convert_to_roman_numeral(99), 'XCIX')

    def test_convert_to_roman_numeral_one_hundred(self):
        self.assertEqual(convert_to_roman_numeral(100), 'C')

    def test_convert_to_roman_numeral_four_hundred(self):
        self.assertEqual(convert_to_roman_numeral(400), 'CD')

    def test_convert_to_roman_numeral_five_hundred(self):
        self.assertEqual(convert_to_roman_numeral(500), 'D')

    def test_convert_to_roman_numeral_nine_hundred(self):
        self.assertEqual(convert_to_roman_numeral(900), 'CM')

    def test_convert_to_roman_numeral_nine_hundred_ninety_nine(self):
        self.assertEqual(convert_to_roman_numeral(999), 'CMXCIX')

    def test_convert_to_roman_numeral_one_thousand(self):
        self.assertEqual(convert_to_roman_numeral(1000), 'M')

    def test_convert_to_roman_numeral_five_thousand(self):
        self.assertEqual(convert_to_roman_numeral(5000), 'MMMMM')

    def test_convert_to_roman_numeral_nine_thousand_nine_hundred_ninety_nine(self):
        self.assertEqual(convert_to_roman_numeral(9999), 'MMMMMMMMMCMXCIX')

    def test_convert_to_roman_numeral_ten_thousand(self):
        self.assertEqual(convert_to_roman_numeral(10000), 'MMMMMMMMMM')
