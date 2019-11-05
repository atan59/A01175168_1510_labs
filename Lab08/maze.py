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
    pass


def move_character(character, direction):
    pass


def check_if_exit_reached(character):
    pass


def game():
    pass


if __name__ == "__main__":
    # doctest.testmod()
    # game()
