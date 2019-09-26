"""Decomposition of base_conversion function from lab 02"""


def max_decimal(base):
    """
    Calculate maximum decimal number that can be represented with given base.

    :param base: an int
    :precondition: base must be an int
    :postcondition: calculate maximum decimal number
    :return: an int
    """
    return base ** 3


def divide(dividend, divisor):
    """
    Divide two numbers.

    :param dividend: an int
    :param divisor: an int
    :precondition: dividend must be an int
    :precondition: divisor must be an int
    :postcondition: divide dividend by divisor
    :return: an int
    """
    return dividend / divisor


def remainder(number, base):
    """
    Calculate remainder of two numbers.

    :param number: an int
    :param base: an int
    :precondition: number must be an int
    :precondition: base must be an int
    :postcondition: calculate remainder when number is divided by base
    :return: an int
    """
    return number % base


def concatenate(string_1, string_2, string_3, string_4):
    """
    Concatenate four strings into one string.

    :param string_1: a string
    :param string_2: a string
    :param string_3: a string
    :param string_4: a string
    :precondition: string_1 must be a string
    :precondition: string_2 must be a string
    :precondition: string_3 must be a string
    :precondition: string_4 must be a string
    :postcondition: concatenate four strings into one string
    :return: a string
    """
    return string_1 + string_2 + string_3 + string_4


def base_conversion():
    """
    Convert a base 10 number into a number of another base.
    """
    destination_base = int(input("Input a destination base between 2 and 9: "))

    max_num = max_decimal(destination_base)

    print("The maximum value is: " + str(max_num))

    decimal = int(input("Input a base 10 number equal to or less than " + str(max_num) + ": "))

    fourth_digit = remainder(decimal, destination_base)
    quotient = divide(decimal, destination_base)

    third_digit = remainder(int(quotient), destination_base)
    quotient = divide(int(quotient), destination_base)

    second_digit = remainder(int(quotient), destination_base)
    quotient = divide(int(quotient), destination_base)

    first_digit = remainder(int(quotient), destination_base)

    new_base_number = concatenate(str(first_digit), str(second_digit), str(third_digit), str(fourth_digit))

    print(int(new_base_number))
