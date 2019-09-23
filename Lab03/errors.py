"""Module where various errors are intentionally generated."""


def main():
    """
    Generate three types of errors.
    """
    word = "Hello"
    a_list = [1, 2]

    print(1/0)  # Generates ZeroDivisionError

    print(word[6])  # Generates IndexError
    print(a_list[3])  # Generates IndexError

    print(word + a_list[0])  # Generates TypeError
    print(len(a_list[0]))  # Generates TypeError


if __name__ == "__main__":
    main()
