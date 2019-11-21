"""Calculate greatest common denominator of two numbers."""
import doctest


def gcd(a: int, b: int) -> int:
    """
    Calculate greatest common denominator

    :param a: an int
    :param b: an int
    :precondition: a must be a non-zero int
    :precondition: b must be a non-zero int
    :postcondition: calculate the greatest common denominator
    :return: an int

    >>> gcd(4, 2)
    2
    >>> gcd(2, 4)
    2
    >>> gcd(-4, 2)
    2
    >>> gcd(4, -2)
    -2
    """
    if a == 0 or b == 0:
        raise ValueError('Zero is not a valid integer.')

    while b != 0:
        (a, b) = (b, a % b)
    return a


if __name__ == "__main__":
    doctest.testmod()
