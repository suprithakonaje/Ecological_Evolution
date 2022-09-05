import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
import numpy as np

import ecology_constants


def plot_LV_graph(time, sol):
    color = iter(cm.rainbow(np.linspace(0, 1, ecology_constants.NUMBER_OF_SPECIES)))
    for i in range(len(sol)):
        c = next(color)
        plt.plot(time, sol[i], color=c)


def show_graph():
    plt.savefig('LV_Iterations_4_species')
    plt.show()




