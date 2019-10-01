from unittest import TestCase
from Lab04.time_calculator import calculate_seconds_in_minutes


class TestCalculate_seconds_in_minutes(TestCase):
    def test_calculate_seconds_in_minutes_zero(self):
        self.assertEqual(calculate_seconds_in_minutes(0), 0)

    def test_calculate_seconds_in_minutes_one_minute(self):
        self.assertEqual(calculate_seconds_in_minutes(1), 60)
