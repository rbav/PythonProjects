#Matplotlib Canvas Demo
# matplotlib's low-level Agg backend is non interactive and only renders images to files.

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas 
from matplotlib.figure import Figure
import numpy as np
import os

os.makedirs("Demos/Figures", exist_ok=True)

#____________________________________Section 1
fig = Figure()
canvas = FigureCanvas(fig)


# ---------------------------
# First Figure (Normal Distribution)
# ---------------------------
fig1 = Figure()
canvas1 = FigureCanvas(fig1)

x = np.random.randn(10000)

ax1 = fig1.add_subplot(111)
ax1.hist(x, 100)
ax1.set_title(r'Normal distribution with $\mu=0, \sigma=1$')
ax1.grid(True)

fig1.savefig('Demos/Figures/matplotlib_histogram.png')
#______________________________________________________________________

# ---------------------------
# Second Figure (Integer Counts)
# ---------------------------
fig2 = Figure()
canvas2 = FigureCanvas(fig2)

x2 = np.random.randint(0, 20, 10000)

ax2 = fig2.add_subplot(111)
ax2.hist(x2, bins=20)
ax2.set_title('Count exact occurrence of integers')
ax2.grid(True)
fig2.savefig('Demos/Figures/random_integers_histogram.png')