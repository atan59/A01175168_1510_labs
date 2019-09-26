"""Module where various errors are intentionally generated."""


def main():
    """
    Generate three types of errors.
    """
    word = "Hello"
    number = 12

    print(1/0)  # Generates ZeroDivisionError

    print(word[6])  # Generates IndexError
    print(word[-7])  # Generates IndexError

    print(word + number)  # Generates TypeError
    print(len(number[0]))  # Generates TypeError


if __name__ == "__main__":
    main()
