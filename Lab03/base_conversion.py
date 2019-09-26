"""Decomposition of base_conversion function from lab 02"""
import doctest


def max_decimal(base):
    """
    Calculate maximum decimal number that can be represented with given base.

    :param base: an int
    :precondition: base must be an int from 2 to 9
    :postcondition: calculate maximum decimal number
    :return: an int
    >>> max_decimal(2)
    15
    >>> max_decimal(5)
    624
    >>> max_decimal(9)
    6560
    """
    return base ** 4 - 1


def divide(dividend, divisor):
    """
    Divide two numbers.

    :param dividend: an int
    :param divisor: an int
    :precondition: dividend must be an int
    :precondition: divisor must be an int
    :postcondition: divide dividend by divisor
    :return: an int
    >>> divide(0, 1)
    0.0
    >>> divide(1, 1)
    1.0
    >>> divide(6560, 5)
    1312.0
    """
    return dividend / divisor


def remainder(dividend, divisor):
    """
    Calculate remainder of two numbers.

    :param dividend: an int
    :param divisor: an int
    :precondition: dividend must be an int
    :precondition: divisor must be an int
    :postcondition: calculate remainder when dividend is divided by divisor
    :return: an int
    >>> remainder(2, 1)
    0
    >>> remainder(5, 2)
    1
    >>> remainder(30, 4)
    2
    """
    return dividend % divisor


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

    new_base_number = str(first_digit)+str(second_digit)+str(third_digit)+str(fourth_digit)

    print(int(new_base_number))


if __name__ == "__main__":
    doctest.testmod()
    base_conversion()
