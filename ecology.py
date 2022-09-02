import graph_plots
from ecology_constants import GROWTH_RATE
from ecology_model_utils import create_initial_community_matrix, create_random_population
import numpy as np

from lotka_volterra_model import solve_GLV


def start_ecological_evolution(env, time, w):
    initial_pop = create_random_population()
    sol = solve_GLV(initial_pop, time, w, GROWTH_RATE, env)
    graph_plots.plot_LV_graph(time, sol)


if __name__ == '__main__':
    start_ecological_evolution()
