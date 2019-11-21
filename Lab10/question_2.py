"""Calculate greatest common denominator of two numbers."""
import doctest


def gcd(a: int, b: int) -> int:
    """
    Calculate greatest common denominator

    :param a: an int
    :param b: an int
    :precondition: a must be an int
    :precondition: b must be an int
    :postcondition: calculate the greatest common denominator
    :return: an int

    >>> gcd(4, 2)
    2
    >>> gcd(2, 4)
    2
    >>> gcd(2, 0)
    2
    """
    while b != 0:
        (a, b) = (b, a % b)
    return a


if __name__ == "__main__":
    doctest.testmod()
