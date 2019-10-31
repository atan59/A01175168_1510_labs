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
