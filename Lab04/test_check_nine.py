from unittest import TestCase
from Lab04.roman_numbers import check_nine


class TestCheck_nine(TestCase):
    def test_check_nine_true(self):
        self.assertTrue(check_nine(9))

    def test_check_nine_false(self):
        self.assertFalse(check_nine(1))
