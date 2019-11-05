from unittest import TestCase
from Lab08.maze import make_character


class TestMakeCharacter(TestCase):
    def test_make_character_correct_key(self):
        actual = make_character().keys()
        expected = "Current Position"
        self.assertIn(expected, actual)

    def test_make_character_correct_starting_value(self):
        actual = make_character().values()
        expected = (0, 0)
        self.assertIn(expected, actual)

    def test_make_character_correct_item(self):
        actual = make_character().items()
        expected = ("Current Position", (0, 0))
        self.assertIn(expected, actual)

    def test_make_character_type(self):
        actual = type(make_character())
        expected = type({"Current Position": (0, 0)})
        self.assertEqual(expected, actual)
