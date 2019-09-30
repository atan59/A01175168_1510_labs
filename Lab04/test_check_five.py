from unittest import TestCase
from Lab04.roman_numbers import check_five


class TestCheck_five(TestCase):
    def test_check_five_true(self):
        self.assertTrue(check_five(5))

    def test_check_five_false(self):
        self.assertFalse(check_five(1))
