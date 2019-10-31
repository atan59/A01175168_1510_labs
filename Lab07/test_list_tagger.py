from unittest import TestCase
from Lab07.midterm import list_tagger


class TestListTagger(TestCase):
    def test_list_tagger_empty_list(self):
        actual = list_tagger([])
        expected = [0]
        self.assertEqual(expected, actual)

    def test_list_tagger_list_length_one(self):
        actual = list_tagger([0])
        expected = [1, 0]
        self.assertEqual(expected, actual)

    def test_list_tagger_list_length_greater_than_one(self):
        actual = list_tagger([1, 2, 3, 4, 5])
        expected = [5, 1, 2, 3, 4, 5]
        self.assertEqual(expected, actual)
