from unittest import TestCase
from Lab04.time_calculator import calculate_days


class TestCalculate_days(TestCase):
    def test_calculate_days_zero(self):
        self.assertEqual(calculate_days(0), 0)

    def test_calculate_days_one_day(self):
        self.assertEqual(calculate_days(86400), 1)

    def test_calculate_days_one_day_truncated(self):
        self.assertEqual(calculate_days(90000), 1)
