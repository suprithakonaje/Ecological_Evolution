from random import random
import numpy as np
import copy

import ecology_constants

N = ecology_constants.NUMBER_OF_SPECIES


def create_random_population():
    pop = np.zeros(N)
    for i in range(N):
        pop[i] = np.random.uniform(0.0, 0.1)
    return pop


def create_initial_community_matrix():
    w = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if i != j:
                w[i][j] = -0.2
            else:
                w[i][j] = -1
    return w


# Selection Coefficient
def selection_coefficient(xj, k):
    s = (ecology_constants.GROWTH_RATE * ecology_constants.CONSTANT_OF_PROPORTIONALITY_OF_SELECTION * xj) / k
    return s


# Rate of Adaptation (vij) for wij
def rate_of_adaptation(xi, xj, k):
    v = xi * ecology_constants.MUTATION_RATE * selection_coefficient(xj, k)
    return v


def update_interaction_matrix(x, w, k):
    for i in range(N):
        for j in range(N):
            if i != j:
                w[i][j] = rate_of_adaptation(x[i], x[j], k)
    return normalisation(w)


def sum_of_elements_for_row_norm(i, M):
    row_element_sum = 0.0
    for j in range(N):
        if i != j:
            row_element_sum += M[i][j]
    return row_element_sum


def sum_of_elements_for_col_norm(j, M):
    col_element_sum = 0.0
    for i in range(N):
        if i != j:
            col_element_sum += M[i][j]
    return col_element_sum


def row_norm(M):
    row_norm_updated = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            val = M[i][j] / sum_of_elements_for_row_norm(i, M)
            if val > 0:
                row_norm_updated[i][j] = - val
            else:
                row_norm_updated[i][j] = val
    return row_norm_updated


def column_norm(M):
    col_norm_updated = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            val = M[i][j] / sum_of_elements_for_col_norm(i, M)
            if val > 0:
                col_norm_updated[i][j] = - val
            else:
                col_norm_updated[i][j] = val

    return col_norm_updated


def normalise(w):
    M = copy.deepcopy(w)
    M_updated = column_norm(row_norm(M))
    if within_converging_accuracy(M, M_updated):
        return M_updated
    else:
        return M


def within_converging_accuracy(M, M_updated):
    sum_M = 0.0
    for i in range(len(M)):
        for j in range(len(M)):
            sum_M += (M_updated[i][j] - M[i][j]) ** 2
    if sum_M < (10 ** -5):
        return True
    else:
        return False


def normalisation(w):
    sum_w_ij = 0.0
    sum_w_ji = 0.0
    for i in range(N):
        for j in range(N):
            if i != j:
                sum_w_ij += w[i][j]
                sum_w_ji += w[j][i]

    if sum_w_ij == sum_w_ji and sum_w_ij < 0:
        normalise(w)
    return w


def getCarryingCapacity(env, i):
    if env == 0:
        return ecology_constants.CARRYING_CAPACITY
    elif env == 1:
        if i % 2 == 0:
            return getPositiveCarryingCapacity()
        else:
            return getNegativeCarryingCapacity()
    elif env == 2:
        if i % 2 != 0:
            return getPositiveCarryingCapacity()
        else:
            return getNegativeCarryingCapacity()


def getNegativeCarryingCapacity():
    return ecology_constants.CARRYING_CAPACITY - ecology_constants.VARIABLE_ENVIRONMENT_CONSTANT


def getPositiveCarryingCapacity():
    return ecology_constants.CARRYING_CAPACITY + ecology_constants.VARIABLE_ENVIRONMENT_CONSTANT


def getSumOfSpeciesInteraction(i, x, w):
    summation = 0
    for j in range(N):
        mat = w[i][j] * x[j]
        summation = summation + mat
    return summation
