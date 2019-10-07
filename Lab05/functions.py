"""A module of functions for Lab 5."""
import random


def roll_die(number_of_rolls, number_of_sides):
    if (number_of_rolls <= 0) or (number_of_sides <= 0):
        total = 0
    else:
        total = 0
        for rolls in range(number_of_rolls):
            total += random.randint(1, number_of_sides + 1)
    return total


def choose_inventory(inventory, selection):
    pass


def generate_vowel():
    pass


def generate_consonant():
    pass


def generate_name(syllables):
    pass


def create_character(name_length):
    pass


def print_character(character):
    pass
