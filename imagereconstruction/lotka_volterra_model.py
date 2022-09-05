import ecology_constants
import imagereconstruction.ecology_model_utils_for_image_reconstruction as eu
import numpy as np
import scipy as sci
from scipy import integrate

N = ecology_constants.NUMBER_OF_SPECIES


def GLV(x, time, w, m, env, env_array):
    dxdt = np.zeros(N)
    for i in range(N):
        k = eu.getCarryingCapacity(env, i)
        dxdt[i] = ((m * x[i]) / k) * (k + eu.getSumOfSpeciesInteraction(i, env_array, w))
    eu.update_interaction_matrix(x, env_array, w, k)
    return dxdt


def solve_GLV(x, time, w, m, env, env_array):
    return sci.integrate.odeint(GLV, x, time, args=(w, m, env, env_array))
