from unittest import TestCase
from Lab04.time_calculator import calculate_hours


class TestCalculate_hours(TestCase):
    def test_calculate_hours_zero(self):
        self.assertEqual(calculate_hours(0), 0)

    def test_calculate_hours_one_hour(self):
        self.assertEqual(calculate_hours(3600), 1)

    def test_calculate_hours_one_hour_truncated(self):
        self.assertEqual(calculate_hours(4000), 1)
