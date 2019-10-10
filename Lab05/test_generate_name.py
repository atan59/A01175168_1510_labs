from unittest import TestCase
from unittest.mock import patch
from Lab05.lab05 import generate_name


class TestGenerate_name(TestCase):
    @patch('random.randint', return_value=0)
    def test_generate_vowel_zero(self, mock_randint):
        actual = generate_name(0)
        expected = ''
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=0)
    def test_generate_vowel_one(self, mock_randint):
        actual = generate_name(1)
        expected = 'Ba'
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=0)
    def test_generate_vowel_positive(self, mock_randint):
        actual = generate_name(2)
        expected = 'Baba'
        self.assertEqual(expected, actual)
