"""A simple 5x5 maze game."""
import doctest


def make_board():
    """
    Create a 5x5 game board.

    :return: a list
    """
    board = []
    for i in range(0, 5):
        for j in range(0, 5):
            board.append((i, j))
    return board


def make_character():
    """
    Create a character.

    :return: a dictionary
    """
    character = {"Current Position": (0, 0)}
    return character


def get_user_choice():
    """
    Get user direction choice.

    :return: a string
    """
    choice = input("*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n" + "Which direction would you like to go?\n" +
                   "*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n" + "1. North\n" + "2. East\n" + "3. South\n" +
                   "4. West\n" + "*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n" + "Please type number from 1 - 4\n" +
                   "*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n" + "Choice: ")
    while int(choice) < 1 or int(choice) > 4:
        print("*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n" + "That's not a valid choice!\n" +
              "Please input your choice again.\n" + "*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n")
        choice = input("*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n" + "Which direction would you like to go?\n" +
                       "*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n" + "1. North\n" + "2. East\n" + "3. South\n" +
                       "4. West\n" + "*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n" +
                       "Please type number from 1 - 4\n" + "*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n" + "Choice: ")
    return choice


def validate_move(board, character, direction):
    """
    Check if move is valid.

    :param board: a list
    :param character: a dictionary
    :param direction: a string
    :precondition: board must be a list of tuples
    :precondition: character must be a dictionary with a key "Current Position"
    :precondition: direction must be a string
    :postcondition: check if move is valid within the board
    :return: a boolean

    >>> validate_move([(0, 0), (0, 1), (1, 0), (1, 1)], {"Current Position": (0, 0)}, "2")
    True
    >>> validate_move([(0, 0), (0, 1), (1, 0), (1, 1)], {"Current Position": (0, 0)}, "1")
    False
    """
    if direction == "1":
        move = (character["Current Position"][0], character["Current Position"][1] - 1)
    elif direction == "2":
        move = (character["Current Position"][0] + 1, character["Current Position"][1])
    elif direction == "3":
        move = (character["Current Position"][0], character["Current Position"][1] + 1)
    elif direction == "4":
        move = (character["Current Position"][0] - 1, character["Current Position"][1])
    if move in board:
        result = True
    else:
        result = False
    return result


def move_character(character, direction):
    """
    Move a character one step.

    :param character: a dictionary
    :param direction: a string
    :precondition: character must be a dictionary with a key "Current Position"
    :precondition: direction must be a string
    :postcondition: move character one step in specified direction

    >>> move_character({"Current Position": (0, 1)}, "1")
    *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
    Your current position (x, y) is: (0, 0)
    *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
    <BLANKLINE>
    >>> move_character({"Current Position": (0, 0)}, "2")
    *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
    Your current position (x, y) is: (1, 0)
    *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
    <BLANKLINE>
    >>> move_character({"Current Position": (0, 0)}, "3")
    *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
    Your current position (x, y) is: (0, 1)
    *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
    <BLANKLINE>
    >>> move_character({"Current Position": (1, 0)}, "4")
    *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
    Your current position (x, y) is: (0, 0)
    *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
    <BLANKLINE>
    """
    if direction == "1":
        character["Current Position"] = (character["Current Position"][0], character["Current Position"][1] - 1)
        print("*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n" + "Your current position (x, y) is: " +
              str(character["Current Position"]) + "\n" + "*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n")
    elif direction == "2":
        character["Current Position"] = (character["Current Position"][0] + 1, character["Current Position"][1])
        print("*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n" + "Your current position (x, y) is: " +
              str(character["Current Position"]) + "\n" + "*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n")
    elif direction == "3":
        character["Current Position"] = (character["Current Position"][0], character["Current Position"][1] + 1)
        print("*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n" + "Your current position (x, y) is: " +
              str(character["Current Position"]) + "\n" + "*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n")
    elif direction == "4":
        character["Current Position"] = (character["Current Position"][0] - 1, character["Current Position"][1])
        print("*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n" + "Your current position (x, y) is: " +
              str(character["Current Position"]) + "\n" + "*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n")


def check_if_exit_reached(character):
    """
    Check if character has reached the end.

    :param character: a dictionary
    :precondition: character must be a dictionary with a key "Current Position"
    :postcondition: check if character is at the end coordinate
    :return: a boolean

    >>> check_if_exit_reached({"Current Position": (4, 4)})
    True
    >>> check_if_exit_reached({"Current Position": (0, 0)})
    False
    """


def game():
    pass


if __name__ == "__main__":
    # doctest.testmod()
    # game()
