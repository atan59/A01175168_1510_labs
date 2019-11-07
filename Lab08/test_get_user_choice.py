from unittest import TestCase
from unittest.mock import patch
from Lab08.maze import get_user_choice
import io


class TestGetUserChoice(TestCase):
    @patch('builtins.input', return_value="1")
    def test_get_user_choice_valid(self, mock_input):
        expected = '1'
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["0", "1"])
    def test_get_user_choice_less_than_one(self, mock_input):
        expected = '1'
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["5", "1"])
    def test_get_user_choice_greater_than_four(self, mock_input):
        expected = '1'
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["0", "1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_less_than_one_printed(self, mock_stdout, mock_input):
        expected = "*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n" + "That's not a valid choice!\n" + \
                   "Please input your choice again.\n" + "*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n\n"
        get_user_choice()
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["5", "1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_greater_than_four_printed(self, mock_stdout, mock_input):
        expected = "*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n" + "That's not a valid choice!\n" + \
                   "Please input your choice again.\n" + "*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n\n"
        get_user_choice()
        actual = mock_stdout.getvalue()
        self.assertEqual(expected, actual)
