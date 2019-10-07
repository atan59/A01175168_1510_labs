"""A module of functions for Lab 5."""
import random
import doctest


def roll_die(number_of_rolls, number_of_sides):
    if (number_of_rolls <= 0) or (number_of_sides <= 0):
        total = 0
    else:
        total = 0

        for rolls in range(number_of_rolls):
            total += random.randint(1, number_of_sides + 1)
    return total


def choose_inventory(inventory, selection):
    if (inventory == []) and (selection == 0):
        result = []
    elif selection < 0:
        print("You can't make a negative selection!")
        result = []
    elif selection > len(inventory):
        print("Your selection is greater than the amount of items in the inventory.")
        result = sorted(inventory)
    elif selection == len(inventory):
        result = sorted(inventory)
    else:
        result = []

        for i in range(0, selection):
            result.append(random.sample(inventory, selection))

        result = sorted(result)
    return result


def generate_vowel():
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'y']

    vowel = vowel_list[random.randint(0, len(vowel_list) - 1)]
    return vowel


def generate_consonant():
    consonant_list = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x',
                      'y', 'z']

    consonant = consonant_list[random.randint(0, len(consonant_list) - 1)]
    return consonant


def generate_name(syllables):
    name = ''

    for i in range(0, syllables):
        syllable = generate_consonant() + generate_vowel()
        name += syllable
    return name.capitalize()


def create_character(name_length):
    if name_length < 0:
        print("This is an invalid name length.")
    else:
        character_stats = []
        attribute_names = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']

        character_stats.append(generate_name(name_length))

        for i in range(0, 6):
            attribute = [attribute_names[i], roll_die(3, 6)]
            character_stats.append(attribute)
    return character_stats


def print_character(character):
    pass

if __name__ = "__main__":
    doctest.testmod()