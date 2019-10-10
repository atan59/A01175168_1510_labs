from unittest import TestCase
from unittest.mock import patch
import io
from Lab05.lab05 import choose_inventory


class TestChooseInventory(TestCase):
    @patch('random.choices', return_value=['Sword'])
    def test_choose_inventory_empty_list_selection_zero(self, mock_choices):
        actual = choose_inventory([], 0)
        expected = []
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_inventory_selection_negative_stdout(self, mock_stdout):
        choose_inventory(['Sword', 'Shield', "Bow"], -1)
        actual = mock_stdout.getvalue()
        expected = "You can't make a negative selection!\n"
        self.assertEqual(expected, actual)

    @patch('random.choices', return_value=['Sword'])
    def test_choose_inventory_selection_negative_return_value(self, mock_choices):
        actual = choose_inventory(['Sword', 'Shield', "Bow"], -1)
        expected = []
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_inventory_selection_greater_than_list_length_stdout(self, mock_stdout):
        choose_inventory(['Sword', 'Shield', "Bow"], 4)
        actual = mock_stdout.getvalue()
        expected = "Your selection is greater than the amount of items in the inventory."
        self.assertEqual(expected, actual)

    @patch('random.choices', return_value=['Sword'])
    def test_choose_inventory_selection_greater_than_list_length_return_value(self, mock_choices):
        actual = choose_inventory(['Sword', 'Shield', "Bow"], 4)
        expected = ['Bow', 'Shield', 'Sword']
        self.assertEqual(expected, actual)

    @patch('random.choices', return_value=['Sword'])
    def test_choose_inventory_selection_equal_to_list_length(self, mock_choices):
        actual = choose_inventory(['Sword', 'Shield', 'Bow'], 3)
        expected = ['Bow', 'Shield', 'Sword']
        self.assertEqual(expected, actual)

    @patch('random.choices', return_value=['Sword', 'Shield'])
    def test_choose_inventory_selection_positive(self, mock_choices):
        actual = choose_inventory(['Sword', 'Shield', 'Bow'], 2)
        expected = ['Shield', 'Sword']
        self.assertEqual(expected, actual)
