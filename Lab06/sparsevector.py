"""Calculate the sum of two vectors."""


def sparse_add(sparse_vector_1, sparse_vector_2):
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
