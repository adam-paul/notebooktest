import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

def plotter(x, y):
    x = np.asarray(x)
    y = np.asarray(y)

    plt.plot(x, y)
    plt.savefig('testplot.png')

x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

plotter(x, y)
