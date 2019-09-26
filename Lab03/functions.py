"""Module with functions using the random module."""
import random
import doctest


def roll_die(number_of_rolls, number_of_sides):
    """
    Calculate total after rolling a die a specified number of times.

    :param number_of_rolls: a positive int
    :param number_of_sides: a positive int
    :precondition: number_of_rolls must be a positive int
    :precondition: number_of_sides must be a positive int
    :postcondition: calculate total of all the rolls
    :return: a positive int
    >>> roll_die(0, 0)
    0
    >>> roll_die(-1, 2)
    0
    >>> roll_die(2, -1)
    0
    """
    if number_of_rolls <= 0 or number_of_sides <= 0:
        total = 0
    elif number_of_rolls > 0 and number_of_sides > 0:
        roll_1 = random.randint(1, number_of_sides)
        roll_2 = random.randint(1, number_of_sides)
        roll_3 = random.randint(1, number_of_sides)

        if number_of_rolls == 1:
            total = roll_1
        elif number_of_rolls == 2:
            total = roll_1 + roll_2
        elif number_of_rolls == 3:
            total = roll_1 + roll_2 + roll_3
    return total


def create_name(length):
    """
    Generate a random name of a specified length.

    :param length: a positive int
    :precondition: length must be a positive int
    :postcondition: Generate a random name with a specified length
    :return: a string
    >>> create_name(0) is None
    True
    >>> create_name(-1) is None
    True
    """
    if length <= 0:
        name = None
    elif length > 0:
        letter_1 = chr(random.randint(97, 122))
        letter_2 = chr(random.randint(97, 122))
        letter_3 = chr(random.randint(97, 122))
        letter_4 = chr(random.randint(97, 122))
        letter_5 = chr(random.randint(97, 122))

        if length == 1:
            name = letter_1.capitalize()
        elif length == 2:
            name = (letter_1 + letter_2).capitalize()
        elif length == 3:
            name = (letter_1 + letter_2 + letter_3).capitalize()
        elif length == 4:
            name = (letter_1 + letter_2 + letter_3 + letter_4).capitalize()
        elif length == 5:
            name = (letter_1 + letter_2 + letter_3 + letter_4 + letter_5).capitalize()
    return name


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
