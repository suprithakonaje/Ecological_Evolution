import ecology
import ecology_constants
import numpy as np

import graph_plots
from ecology_model_utils import create_initial_community_matrix
import seaborn as sns; sns.set_theme()
import matplotlib.pyplot as mp

initial_time = 0
t = ecology_constants.TIME
ts = ecology_constants.TIMESTEPS


def update_time(iterations):
    updated_start = iterations
    updated_end = iterations + ecology_constants.TIME
    time = np.linspace(updated_start, updated_end, ts)
    return time, updated_end


def start_simulation():
    t = ecology_constants.TIME
    plot_time = []
    time = np.linspace(initial_time, t, ts)
    w = create_initial_community_matrix()
    for i in range(6):

        if i == 0 or i == ecology_constants.NUMBER_OF_EVOLUTIONS - 1:
            env = 0
        # elif i % 2 != 0:
        #     env = 1
        # elif i % 2 == 0:
        #     env = 2

        plot_time.append(time)

        sol = ecology.start_ecological_evolution(env, time, w)
        if i == 0:
            formatted_array = np.copy(sol)
        elif i != 0:
            formatted_array = np.append(formatted_array, sol, axis=0)

        time, t = update_time(t)

    sns.heatmap(w, annot=True, cmap='gray')
    mp.show()
    plot_time = np.concatenate(plot_time, axis=0)
    p = [[row[i] for row in formatted_array] for i in range(ecology_constants.NUMBER_OF_SPECIES)]

    # graph_plots.plot_LV_graph(plot_time, p)
    # graph_plots.show_graph()
    # graph_plots.save_graph()
