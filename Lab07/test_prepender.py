from unittest import TestCase
from Lab07.midterm import prepender


class TestPrepender(TestCase):
    def test_prepender_empty_list_empty_string(self):
        actual = prepender([], "")
        expected = []
        self.assertEqual(expected, actual)

    def test_prepender_empty_list_non_empty_string(self):
        actual = prepender([], "Python")
        expected = []
        self.assertEqual(expected, actual)

    def test_prepender_non_empty_list_empty_string(self):
        actual = prepender(["Python"], "")
        expected = ['Python']
        self.assertEqual(expected, actual)

    def test_prepender_list_length_one_non_empty_string(self):
        actual = prepender(["Python"], "I love ")
        expected = ['I love Python']
        self.assertEqual(expected, actual)

    def test_prepender_positive_list_length_empty_string(self):
        actual = prepender(["Python", "is", "better", "than", "JavaScript"], "")
        expected = ['Python', 'is', 'better', 'than', 'JavaScript']
        self.assertEqual(expected, actual)

    def test_prepender_positive_list_length_non_empty_string(self):
        actual = prepender(["Python", "is", "better", "than", "JavaScript"], "Umm... ")
        expected = ['Umm... Python', 'Umm... is', 'Umm... better', 'Umm... than', 'Umm... JavaScript']
        self.assertEqual(expected, actual)


"""
I would also write test for empty strings in the list.
"""
