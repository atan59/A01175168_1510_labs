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
    pass


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
