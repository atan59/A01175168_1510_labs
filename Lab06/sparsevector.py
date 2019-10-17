"""Calculate the sum of two vectors.

Q6.
You would not be able to return the length of the vector because we have not included the zero values in the dictionary.
This means that there could be trailing zero values that we don't know about. If we use the len() function on the
current dictionary, it would just return the length of the vector with only non-zero values.

I would ask the team lead to clarify whether they want the length of the vector with or without the zero values. If they
want it with the zero values, I would also ask if they want to include the leading and trailing zero values in the
length or if they just want to include the zeros in between the non-zero values.
"""
import doctest


def sparse_add(sparse_vector_1, sparse_vector_2):
    """
    Calculate sum of the values of two sparse vector dictionaries.

    :param sparse_vector_1: a dictionary
    :param sparse_vector_2: a dictionary
    :precondition: sparse_vector_1 must be a dictionary with no strings as values
    :precondition: sparse_vector_2 must be a dictionary with no strings as values
    :postcondition: calculate the sum of the values of the two sparse vector dictionaries
    :return: a dictionary

    >>> sparse_add({0: 1, 3: 5, 4: 2}, {0: 2, 3: 4, 4: 5})
    {0: 3, 3: 9, 4: 7}
    """
    sparse_vector_sum = {}

    for key in sparse_vector_1:
        if key not in sparse_vector_2:
            sparse_vector_2[key] = 0
    for key in sparse_vector_2:
        if key not in sparse_vector_1:
            sparse_vector_1[key] = 0

    for key in sparse_vector_1:
        sparse_vector_sum[key] = sparse_vector_1[key] + sparse_vector_2[key]

        if sparse_vector_sum[key] == 0:
            del sparse_vector_sum[key]

    return sparse_vector_sum


if __name__ == "__main__":
    doctest.testmod()
