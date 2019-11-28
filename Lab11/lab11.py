import time
import doctest
# import sys


def timer(func):
    """Time how long it takes for a function to execute

    :param func: a function
    :precondition: func must be a function
    :postcondition: record time it took to execute func
    :return: a function
    """
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        function_name = func.__name__
        write_to_file(function_name, value[0], start_time, end_time, run_time)
        return value
    return wrapper_timer


def write_to_file(func_name: str, num: int, start: float, end: float, run: float) -> None:
    """Write to file

    :param func_name: a string
    :param num: an int
    :param start: a floating point number
    :param end: a floating point number
    :param run: a floating point number
    :precondition: func_name must be a string
    :precondition: num must be an int
    :precondition: start, end, run must be floating point numbers
    :postcondition: write func_name, int, start, end, and run to result.txt
    :return: None
    """
    with open("result.txt", "a") as file_object:
        file_object.write(f"{func_name}({num}) started at {start} and ended at {end}\n"
                          f"The run time is {run}\n\n")


@timer
def factorial_iterative(my_int: int) -> tuple:
    """Calculate factorial of my_int

    This function is decorated with the timer function to calculate how long it takes to execute the function.

    :param my_int: an int
    :precondition: my_int must be an int
    :postcondition: calculate factorial of my_int
    :return: a tuple

    >>> factorial_iterative(0)
    (0, 1)
    >>> factorial_iterative(1)
    (1, 1)
    >>> factorial_iterative(5)
    (5, 120)
    """
    result = 1
    for i in range(my_int):
        result *= i+1
    return my_int, result


@timer
def factorial_recursive(my_int: int) -> tuple:
    """Calculate factorial of my_int using recursion

    This function is decorated with the timer function to calculate how long it takes to execute the function.

    :param my_int: an int
    :precondition: my_int must be an int
    :postcondition: Calculate factorial of my_int using recursion
    :return: a tuple

    >>> factorial_recursive(0)
    (0, 1)
    >>> factorial_recursive(1)
    (1, 1)
    >>> factorial_recursive(5)
    (5, 120)
    """
    return my_int, factorial_recursive_helper(num=my_int)


def factorial_recursive_helper(num: int) -> int:
    """Calculate the factorial of num using recursion

    :param num: an int
    :precondition: num must an int
    :postcondition: calculate the factorial of num using recursion
    :return: an int

    >>> factorial_recursive_helper(0)
    1
    >>> factorial_recursive_helper(1)
    1
    >>> factorial_recursive_helper(5)
    120
    """
    if num <= 1:
        return 1
    return num * factorial_recursive_helper(num=num-1)


def main():
    """Run factorial_recursive and factorial_iterative"""
    # sys.setrecursionlimit(1000000)
    for i in range(1, 101):
        factorial_recursive(my_int=i)

    for i in range(1, 101):
        factorial_iterative(my_int=i)

    doctest.testmod()


if __name__ == "__main__":
    main()
