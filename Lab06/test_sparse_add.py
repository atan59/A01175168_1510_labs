from unittest import TestCase
from Lab06.sparsevector import sparse_add


class TestSparseAdd(TestCase):

    def test_sparse_add_empty_dictionaries(self):
        expected = {}
        actual = sparse_add({}, {})
        self.assertEqual(expected, actual)

    def test_sparse_add_same_indices(self):
        expected = {0: 2, 1: 3}
        actual = sparse_add({0: 1, 1: 1}, {0: 1, 1: 2})
        self.assertEqual(expected, actual)

    def test_sparse_add_first_dictionary_empty(self):
        expected = {0: 1, 1: 2, 2: 3}
        actual = sparse_add({}, {0: 1, 1: 2, 2: 3})
        self.assertEqual(expected, actual)

    def test_sparse_add_second_dictionary_empty(self):
        expected = {0: 1, 1: 2, 2: 3}
        actual = sparse_add({0: 1, 1: 2, 2: 3}, {})
        self.assertEqual(expected, actual)

    def test_sparse_add_no_matching_indices(self):
        expected = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
        actual = sparse_add({0: 1, 2: 1, 4: 1}, {1: 1, 3: 1, 5: 1})
        self.assertEqual(expected, actual)

    def test_sparse_add_some_matching_indices(self):
        expected = {0: 2, 1: 1, 2: 1, 3: 3, 4: 5, 5: 2}
        actual = sparse_add({0: 1, 1: 1, 3: 1, 4: 2}, {0: 1, 2: 1, 3: 2, 4: 3, 5: 2})
        self.assertEqual(expected, actual)

    def test_sparse_add_all_values_zero(self):
        expected = {}
        actual = sparse_add({0: -1, 1: -2, 2: -3}, {0: 1, 1: 2, 2: 3})
        self.assertEqual(expected, actual)

    def test_sparse_add_some_values_zero(self):
        expected = {0: 1, 2: 3, 3: 1}
        actual = sparse_add({0: 1, 1: -1, 3: -2, 4: -3}, {1: 1, 2: 3, 3: 3, 4: 3})
        self.assertEqual(expected, actual)
