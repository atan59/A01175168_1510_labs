from unittest import TestCase
from Lab04.time_calculator import calculate_seconds_in_days


class TestCalculateSecondsInDays(TestCase):
    def test_calculate_seconds_in_days_zero(self):
        self.assertEqual(calculate_seconds_in_days(0), 0)

    def test_calculate_seconds_in_days_one_day(self):
        self.assertEqual(calculate_seconds_in_days(1), 86400)
