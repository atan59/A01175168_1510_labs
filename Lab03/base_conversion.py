"""Copy of base_conversion.py from Lab 02"""


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
