import random
import numpy as np


def normalize_row(matrix: np.array):
    """
    normalizes each row by dividing each elements of row i by the sum of row i
    :param matrix:
    :return: normalized matrix
    """
    matrix = matrix.astype(float)
    for i in range(len(matrix)):
        row_sum = sum(matrix[i])
        matrix[i] = matrix[i] / row_sum if row_sum != 0 else matrix[i] / 1
    return matrix


def random_walk(matrix, s, e):
    """
    computes the steps it takes for a random walk to get from s to e
    :param matrix: adjacency matrix
    :param s: starting index (starting node)
    :param e: ending index (ending node)
    :return: number of steps from start to end
    """
    # matrix -> adj matrix
    # s -> starting row
    # e -> ending row
    matrix = normalize_row(matrix)
    elements = np.arange(matrix.shape[0])
    c_index = s  # current index for this iteration
    count = 0  # count of transitions

    while True:
        count += 1
        probs = matrix[c_index]  # probability of transitions
        # sample from probs
        sample = np.random.choice(elements, p=probs)  # sample a target using probs
        c_index = sample  # go to target
        if sample == e:  # if target is our ending point
            return count  # stop walking
        # return -1 indicating end node cannot be reached
        # currently set the max count arbitrarily to n^3
        if count >= pow(len(matrix), 3):
            return -1


