from unittest import TestCase
from unittest.mock import patch
from Lab05.lab05 import generate_syllable


class TestGenerateSyllable(TestCase):
    @patch('random.randint', return_value=0)
    def test_generate_vowel_min(self, mock_randint):
        actual = generate_syllable()
        expected = 'ba'
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=3)
    def test_generate_vowel_mid(self, mock_randint):
        actual = generate_syllable()
        expected = 'fo'
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=5)
    def test_generate_vowel_max(self, mock_randint):
        actual = generate_syllable()
        expected = 'hy'
        self.assertEqual(expected, actual)
