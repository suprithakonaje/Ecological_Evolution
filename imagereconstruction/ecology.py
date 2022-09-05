import numpy as np

from imagereconstruction.lotka_volterra_model import solve_GLV
from ecology_constants import GROWTH_RATE
from imagereconstruction.ecology_model_utils_for_image_reconstruction import create_random_population


def start_ecological_evolution(env, time, w, env_array):
    initial_pop = create_random_population()
    sol = solve_GLV(initial_pop, time, w, GROWTH_RATE, env, env_array)
    return sol


if __name__ == '__main__':
    start_ecological_evolution()
