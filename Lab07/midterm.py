"""Implementation of solutions for the six coding questions from the midterm."""
import random
import doctest


def list_tagger(batch):
    """
    Tag a list with its length at the beginning.

    :param batch: a list
    :precondition: batch must be a list
    :postcondition: insert length of list at the beginning of the list
    :return: a list

    >>> list_tagger([])
    [0]
    >>> list_tagger([1, 2, 3])
    [3, 1, 2, 3]
    """
    result = []
    result.insert(0, len(batch))

    return result


def cutoff(int_list, num):
    """
    Count the amount of values in a list that are multiples of a certain number.

    :param int_list: a list
    :param num: an int
    :precondition: int_list must be a list of integers
    :precondition: num must be a positive int
    :postcondition: count number of values in int_list that are multiples of num
    :return: an int
    """
    count = 0
    for i in int_list:
        if i % num == 0:
            count += 1

    return count


def prepender(string_list, prefix):
    """
    Add prefix to all strings in a list.

    :param string_list: a list
    :param prefix: a string
    :precondition: string_list must be a list of strings
    :precondition: prefix must be a string
    :postcondition: add prefix to all strings in a list
    """
    for i in range(0, len(string_list)):
        string_list[i] = prefix + string_list[i]


def name_list():
    """
    Create a dictionary to store lengths of names.

    :return: a dictionary
    """
    user_input = ""
    names = {}

    while user_input.lower() != "quit":
        user_input = input("Type a name (Type \"quit\" to exit): ")
        if user_input.lower() == "quit":
            break
        else:
            if len(user_input) not in names.keys():
                names[len(user_input)] = [user_input]
            else:
                names[len(user_input)].append(user_input)

    return names


def multiples_of_3(upper_bound):
    """
    Calculate sum of multiples of 3 in a range from 1 to upper_bound.

    :param upper_bound: an int
    :precondition: upper_bound must be a positive int greater than 1
    :postcondition: calculate the sum of the multiples of 3 in a range from 1 to upper_bound
    :return: an int
    """
    positive_integers = range(1, upper_bound)
    sum_of_multiples = 0
    for num in positive_integers:
        if num % 3 == 0:
            sum_of_multiples += num

    return sum_of_multiples


def create_tally(num_of_sides):
    tally = {}
    for i in range(1, num_of_sides + 1):
        tally[i] = 0

    return tally


def roll_die(num_of_sides):
    return random.randint(1, num_of_sides)


def tally_roll(roll_result, tally):
    tally[roll_result] += 1


def simulate_rolls(num_of_sides, num_of_rolls, tally):
    times_rolled = 0
    while times_rolled < num_of_rolls:
        roll_result = roll_die(num_of_sides)
        tally_roll(roll_result, tally)
        times_rolled += 1


def print_tally(tally):
    for key, value in tally:
        print("You rolled " + str(key) + " " + str(value) + " times.")


def main():
    num_of_sides = int(input("How many sides are on the die?: "))
    num_of_rolls = int(input("How many die rolls?: "))

    tally = create_tally(num_of_sides)

    simulate_rolls(num_of_sides, num_of_rolls, tally)
    print_tally(tally)

    doctest.testmod()


if __name__ == "__main__":
    main()
