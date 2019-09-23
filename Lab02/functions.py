"""Module with various functions"""


def format_name(first_name, last_name):
    """
    Format two strings.

    :param first_name: a string
    :param last_name: a string
    :precondition: first_name must be a string
    :precondition: last_name must be a string
    :postcondition: format first_name and last_name
    :return: formatted name
    """
    first_name_formatted = first_name.strip()
    last_name_formatted = last_name.strip()

    formatted_name = first_name_formatted.title() + " " + last_name_formatted.title()

    return formatted_name


def tripler(operand):
    """
    Triple a string, int, or float.

    :param operand: a string, int, or float
    :precondition: operand must be a string, int, or float
    :postcondition: triple operand
    :return: a string with the operand repeated three times
    """
    tripled = str(operand) * 3

    return tripled


def this_year():
    """
    Calculate 2019.

    :return: an int equal to 2019
    """
    year = int(50 * 40 + 26 % 16 + 6 * 6 - 3 * 9)

    return year


def base_conversion():
    """
    Convert a base 10 number into a number of another base.
    """
    destination_base = int(input("Input a destination base between 2 and 9: "))

    max_decimal = destination_base ** 4 - 1

    print("The maximum value is: " + str(max_decimal))

    decimal = int(input("Input a base 10 number equal to or less than " + str(max_decimal) + ": "))

    fourth_digit = decimal % destination_base
    quotient = decimal / destination_base

    third_digit = int(quotient) % destination_base
    quotient = int(quotient) / destination_base

    second_digit = int(quotient) % destination_base
    quotient = int(quotient) / destination_base

    first_digit = int(quotient) % destination_base
    quotient = int(quotient) / destination_base

    new_base_number = str(first_digit) + str(second_digit) + str(third_digit) + str(fourth_digit)

    print(int(new_base_number))


def main():
    """
    Run the main program.

    Test the functions in this module.
    """
    print(format_name("    aMy  ", "Tan    "))
    print(tripler(1))
    print(tripler(1.1))
    print(tripler("One"))
    print(this_year())
    base_conversion()


if __name__ == "__main__":
    main()
