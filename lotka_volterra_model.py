import ecology_constants
import ecology_model_utils as eu
import numpy as np
import scipy as sci
from scipy import integrate

N = ecology_constants.NUMBER_OF_SPECIES


def GLV(x, time, w, m, env):
    dxdt = np.zeros(N)
    for i in range(N):
        k = eu.getCarryingCapacity(env, i)
        dxdt[i] = ((m * x[i]) / k) * (k + eu.getSumOfSpeciesInteraction(i, x, w))
    eu.update_interaction_matrix(x, w, k)
    return dxdt


def solve_GLV(x, time, w, m, env):
    return sci.integrate.odeint(GLV, x, time, args=(w, m, env))
