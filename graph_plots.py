import matplotlib.pyplot as plt


def plot_LV_graph(time, sol):
    plt.plot(time, sol[:, 0], color="blue", label="HH")
    plt.plot(time, sol[:, 1], color="red", label="HL")
    plt.plot(time, sol[:, 2], color="yellow", label="LH")
    plt.plot(time, sol[:, 3], color="purple", label="LL")


def show_graph():
    plt.show()


def save_graph():
    plt.savefig('LV_Iterations_4_species.png')
