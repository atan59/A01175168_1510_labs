from unittest import TestCase
from Lab04.time_calculator import calculate_minutes


class TestCalculate_minutes(TestCase):
    def test_calculate_minutes_zero(self):
        self.assertEqual(calculate_minutes(0), 0)

    def test_calculate_minutes_one_minute(self):
        self.assertEqual(calculate_minutes(60), 1)

    def test_calculate_minutes_one_minute_truncated(self):
        self.assertEqual(calculate_minutes(70), 1)
