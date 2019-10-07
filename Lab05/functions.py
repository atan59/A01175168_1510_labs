"""A module of functions for Lab 5."""
import random
import doctest


def roll_die(number_of_rolls, number_of_sides):
    """
    Roll a die with a specific number of sides a certain number of times.

    :param number_of_rolls: a positive int
    :param number_of_sides: a positive int
    :precondition: number_of_rolls must be an int greater than 0
    :precondition: number_of_sides must be an int greater than 0
    :postcondition: calculate total number after a certain number of rolls.
    :return: an int
    """
    if (number_of_rolls <= 0) or (number_of_sides <= 0):
        total = 0
    else:
        total = 0

        for rolls in range(number_of_rolls):
            total += random.randint(1, number_of_sides + 1)
    return total


def choose_inventory(inventory, selection):
    """
    Choose a certain number of items in an inventory.

    :param inventory: a list
    :param selection: a positive int
    :precondition: inventory must be a populated list
    :precondition: selection must be a positive int
    :postcondition: make a list with randomly selected items from the inventory
    :return: a list
    """
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
    """
    Generate a random vowel.

    :return: a string
    """
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
    print("*~~~~~~~~~~Character Sheet~~~~~~~~~~*" + "\n" +
          "Name: " + character[0] + "\n" +
          "*~~~~~~~~~~~~~~~Stats~~~~~~~~~~~~~~~*" + "\n" +
          character[1][0] + ": " + str(character[1][1]) + "\n" +
          character[2][0] + ": " + str(character[2][1]) + "\n" +
          character[3][0] + ": " + str(character[3][1]) + "\n" +
          character[4][0] + ": " + str(character[4][1]) + "\n" +
          character[5][0] + ": " + str(character[5][1]) + "\n" +
          character[6][0] + ": " + str(character[6][1]))


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
