from unittest import TestCase
from unittest.mock import patch
import io
from Lab04.time_calculator import time_calculator


class TestTime_calculator(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_time_calculator_zero(self, mock_stdout):
        time_calculator(0)
        actual_value = mock_stdout.getvalue()
        self.assertEqual(actual_value, '0 Day/s 0 Hour/s 0 Minute/s 0 Second/s\n')

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_time_calculator_only_seconds(self, mock_stdout):
        time_calculator(1)
        actual_value = mock_stdout.getvalue()
        self.assertEqual(actual_value, '0 Day/s 0 Hour/s 0 Minute/s 1 Second/s\n')

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_time_calculator_only_minutes(self, mock_stdout):
        time_calculator(60)
        actual_value = mock_stdout.getvalue()
        self.assertEqual(actual_value, '0 Day/s 0 Hour/s 1 Minute/s 0 Second/s\n')

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_time_calculator_only_hours(self, mock_stdout):
        time_calculator(3600)
        actual_value = mock_stdout.getvalue()
        self.assertEqual(actual_value, '0 Day/s 1 Hour/s 0 Minute/s 0 Second/s\n')

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_time_calculator_only_days(self, mock_stdout):
        time_calculator(86400)
        actual_value = mock_stdout.getvalue()
        self.assertEqual(actual_value, '1 Day/s 0 Hour/s 0 Minute/s 0 Second/s\n')

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_time_calculator_seconds_and_minutes(self, mock_stdout):
        time_calculator(61)
        actual_value = mock_stdout.getvalue()
        self.assertEqual(actual_value, '0 Day/s 0 Hour/s 1 Minute/s 1 Second/s\n')

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_time_calculator_seconds_and_hours(self, mock_stdout):
        time_calculator(3601)
        actual_value = mock_stdout.getvalue()
        self.assertEqual(actual_value, '0 Day/s 1 Hour/s 0 Minute/s 1 Second/s\n')

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_time_calculator_seconds_and_days(self, mock_stdout):
        time_calculator(86401)
        actual_value = mock_stdout.getvalue()
        self.assertEqual(actual_value, '1 Day/s 0 Hour/s 0 Minute/s 1 Second/s\n')

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_time_calculator_minutes_and_hours(self, mock_stdout):
        time_calculator(3660)
        actual_value = mock_stdout.getvalue()
        self.assertEqual(actual_value, '0 Day/s 1 Hour/s 1 Minute/s 0 Second/s\n')

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_time_calculator_minutes_and_days(self, mock_stdout):
        time_calculator(86460)
        actual_value = mock_stdout.getvalue()
        self.assertEqual(actual_value, '1 Day/s 0 Hour/s 1 Minute/s 0 Second/s\n')

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_time_calculator_hours_and_days(self, mock_stdout):
        time_calculator(90000)
        actual_value = mock_stdout.getvalue()
        self.assertEqual(actual_value, '1 Day/s 1 Hour/s 0 Minute/s 0 Second/s\n')

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_time_calculator_seconds_minutes_and_hours(self, mock_stdout):
        time_calculator(3661)
        actual_value = mock_stdout.getvalue()
        self.assertEqual(actual_value, '0 Day/s 1 Hour/s 1 Minute/s 1 Second/s\n')

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_time_calculator_seconds_minutes_and_days(self, mock_stdout):
        time_calculator(86461)
        actual_value = mock_stdout.getvalue()
        self.assertEqual(actual_value, '1 Day/s 0 Hour/s 1 Minute/s 1 Second/s\n')

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_time_calculator_minutes_hours_and_days(self, mock_stdout):
        time_calculator(90060)
        actual_value = mock_stdout.getvalue()
        self.assertEqual(actual_value, '1 Day/s 1 Hour/s 1 Minute/s 0 Second/s\n')

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_time_calculator_seconds_hours_and_days(self, mock_stdout):
        time_calculator(90001)
        actual_value = mock_stdout.getvalue()
        self.assertEqual(actual_value, '1 Day/s 1 Hour/s 0 Minute/s 1 Second/s\n')

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_time_calculator_seconds_minutes_hours_and_days(self, mock_stdout):
        time_calculator(90061)
        actual_value = mock_stdout.getvalue()
        self.assertEqual(actual_value, '1 Day/s 1 Hour/s 1 Minute/s 1 Second/s\n')
