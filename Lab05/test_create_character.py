from unittest import TestCase
from unittest.mock import patch
import io
from Lab05.lab05 import create_character


class TestCreate_character(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_create_character_negative(self, mock_stdout):
        create_character(-1)
        actual = mock_stdout.getvalue()
        expected = "This is an invalid name length.\n"
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    def test_create_character_zero(self, mock_randint):
        actual = create_character(0)
        expected = ['', ['Strength', 3], ['Dexterity', 3], ['Constitution', 3], ['Intelligence', 3], ['Wisdom', 3],
                    ['Charisma', 3]]
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    def test_create_character_one(self, mock_randint):
        actual = create_character(1)
        expected = ['Ce', ['Strength', 3], ['Dexterity', 3], ['Constitution', 3], ['Intelligence', 3], ['Wisdom', 3],
                    ['Charisma', 3]]
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    def test_create_character_positive(self, mock_randint):
        actual = create_character(2)
        expected = ['Cece', ['Strength', 3], ['Dexterity', 3], ['Constitution', 3], ['Intelligence', 3], ['Wisdom', 3],
                    ['Charisma', 3]]
        self.assertEqual(expected, actual)
