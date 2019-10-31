"""Implementation of solutions for the six coding questions from the midterm."""


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
    :precondition: num must be a positive int
    :postcondition: count number of values in int_list that are multiples of num
    :return: an int
    """
    count = 0
    for i in int_list:
        if i % num == 0:
            count += 1

    return count

