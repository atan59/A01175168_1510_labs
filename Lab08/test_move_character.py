from unittest import TestCase
from unittest.mock import patch
from Lab08.maze import move_character
import io


class TestMoveCharacter(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_character_north(self, mock_stdout):
        move_character({"Current Position": (0, 1)}, "1")
        actual = mock_stdout.getvalue()
        expected = "*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n" + "Your current position (x, y) is: (0, 0)\n" +\
                   "*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n\n"
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_character_east(self, mock_stdout):
        move_character({"Current Position": (0, 0)}, "2")
        actual = mock_stdout.getvalue()
        expected = "*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n" + "Your current position (x, y) is: (1, 0)\n" + \
                   "*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n\n"
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_character_south(self, mock_stdout):
        move_character({"Current Position": (0, 0)}, "3")
        actual = mock_stdout.getvalue()
        expected = "*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n" + "Your current position (x, y) is: (0, 1)\n" + \
                   "*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n\n"
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_character_west(self, mock_stdout):
        move_character({"Current Position": (1, 0)}, "4")
        actual = mock_stdout.getvalue()
        expected = "*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n" + "Your current position (x, y) is: (0, 0)\n" + \
                   "*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n\n"
        self.assertEqual(expected, actual)
