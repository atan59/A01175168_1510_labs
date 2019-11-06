from unittest import TestCase
from Lab08.maze import check_if_exit_reached


class TestCheckIfExitReached(TestCase):
    def test_check_if_exit_reached_true(self):
        actual = check_if_exit_reached({"Current Position": (4, 4)})
        expected = True
        self.assertEqual(expected, actual)

    def test_check_if_exit_reached_false(self):
        actual = check_if_exit_reached({"Current Position": (0, 0)})
        expected = False
        self.assertEqual(expected, actual)

    def test_check_if_exit_reached_true_type(self):
        actual = type(check_if_exit_reached({"Current Position": (4, 4)}))
        expected = type(True)
        self.assertEqual(expected, actual)

    def test_check_if_exit_reached_false_type(self):
        actual = type(check_if_exit_reached({"Current Position": (0, 0)}))
        expected = type(False)
        self.assertEqual(expected, actual)
