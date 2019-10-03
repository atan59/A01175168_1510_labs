from unittest import TestCase
from Lab04.roman_numbers import check_four


class TestCheckFour(TestCase):
    def test_check_four_true(self):
        self.assertTrue(check_four(4))

    def test_check_four_false(self):
        self.assertFalse(check_four(1))
