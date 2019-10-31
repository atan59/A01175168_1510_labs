from unittest import TestCase
from Lab07.midterm import cutoff


class TestCutoff(TestCase):
    def test_cutoff_empty_list_zero(self):
        actual = cutoff([], 0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_cutoff_empty_list_five(self):
        actual = cutoff([], 5)
        expected = 0
        self.assertEqual(expected, actual)

    def test_cutoff_list_length_one_zero(self):
        actual = cutoff([0], 0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_cutoff_list_length_one_five(self):
        actual = cutoff([0], 5)
        expected = 0
        self.assertEqual(expected, actual)

    def test_cutoff_list_length_two_two(self):
        actual = cutoff([2], 2)
        expected = 1
        self.assertEqual(expected, actual)

    def test_cutoff_list_length_two_four(self):
        actual = cutoff([2], 4)
        expected = 0
        self.assertEqual(expected, actual)

    def test_cutoff_list_length_five_zero(self):
        actual = cutoff([1, 2, 3, 4, 5], 0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_cutoff_list_length_five_even(self):
        actual = cutoff([1, 2, 3, 4, 5], 2)
        expected = 2
        self.assertEqual(expected, actual)

    def test_cutoff_list_length_five_identical_even(self):
        actual = cutoff([2, 2, 2, 2, 2], 2)
        expected = 5
        self.assertEqual(expected, actual)

    def test_cutoff_list_length_five_identical_odd(self):
        actual = cutoff([2, 2, 2, 2, 2], 10)
        expected = 0
        self.assertEqual(expected, actual)

    def test_cutoff_list_length_five_different_even(self):
        actual = cutoff([3, 6, 9, 12, 15], 3)
        expected = 5
        self.assertEqual(expected, actual)


"""
I would also write multiple tests with negative numbers in the list.
"""
