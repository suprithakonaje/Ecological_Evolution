import ecology
import ecology_constants
import numpy as np

import graph_plots
from ecology_model_utils import create_initial_community_matrix

initial_time = 0
t = 50
ts = ecology_constants.TIMESTEPS


def update_time(iterations):
    updated_start = iterations
    updated_end = iterations + 50
    time = np.linspace(updated_start, updated_end, ts)
    return time, updated_end


def start_simulation():
    t = 50
    time = np.linspace(initial_time, t, ts)
    w = create_initial_community_matrix()
    for i in range(ecology_constants.NUMBER_OF_EVOLUTIONS):

        if i == 0 or i == ecology_constants.NUMBER_OF_EVOLUTIONS - 1:
            env = 0
        elif i % 2 != 0:
            env = 1
        elif i % 2 == 0:
            env = 2

        ecology.start_ecological_evolution(env, time, w)
        time, t = update_time(t)
    graph_plots.show_graph()
    graph_plots.save_graph()
