from unittest import TestCase
from unittest.mock import patch
import io
from Lab05.lab05 import print_character


class TestPrintCharacter(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_without_inventory(self, mock_stdout):
        print_character(['Cece', ['Strength', 3], ['Dexterity', 3], ['Constitution', 3], ['Intelligence', 3],
                         ['Wisdom', 3], ['Charisma', 3]])
        actual = mock_stdout.getvalue()
        expected = "*~~~~~~~~~~Character Sheet~~~~~~~~~~*\n" + "Name: Cece\n" + \
                   "*~~~~~~~~~~~~~~~Stats~~~~~~~~~~~~~~~*\n" + "Strength: 3\n" + "Dexterity: 3\n" + \
                   "Constitution: 3\n" + "Intelligence: 3\n" + "Wisdom: 3\n" + "Charisma: 3\n"
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_with_inventory(self, mock_stdout):
        print_character(['Cece', ['Strength', 3], ['Dexterity', 3], ['Constitution', 3], ['Intelligence', 3],
                         ['Wisdom', 3], ['Charisma', 3], ['Bow', 'Shield', 'Sword']])
        actual = mock_stdout.getvalue()
        expected = "*~~~~~~~~~~Character Sheet~~~~~~~~~~*\n" + "Name: Cece\n" + \
                   "*~~~~~~~~~~~~~~~Stats~~~~~~~~~~~~~~~*\n" + "Strength: 3\n" + "Dexterity: 3\n" + \
                   "Constitution: 3\n" + "Intelligence: 3\n" + "Wisdom: 3\n" + "Charisma: 3\n" + \
                   "*~~~~~~~~~~Inventory~~~~~~~~~~*\n" + "1. Bow\n" + "2. Shield\n" + "3. Sword\n"
        self.assertEqual(expected, actual)
