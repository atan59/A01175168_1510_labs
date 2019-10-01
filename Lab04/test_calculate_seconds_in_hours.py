from unittest import TestCase
from Lab04.time_calculator import calculate_seconds_in_hours


class TestCalculate_seconds_in_hours(TestCase):
    def test_calculate_seconds_in_hours_zero(self):
        self.assertEqual(calculate_seconds_in_hours(0), 0)

    def test_calculate_seconds_in_hours_one_hour(self):
        self.assertEqual(calculate_seconds_in_hours(1), 3600)
