"""
Matplotlib tutorial

http://www.labri.fr/perso/nrougier/teaching/matplotlib/matplotlib.html
python 3.6

"""

import numpy as np
import matplotlib.pyplot as plt
"""
#x values:
X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
#y values:
C,S = np.cos(X), np.sin(X)

#each .plot(x,y) is a data series.
plt.plot(X,C)
plt.plot(X,S)

"""

# Create a new figure of size 8x6 points, using 100 dots per inch
plt.figure(figsize=(8,6), dpi=100)

# Create a new subplot from a grid of 1x1
plt.subplot(111)

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

# Plot cosine using blue color with a continuous line of width 1 (pixels)
plt.plot(X, C, color="blue", linewidth=1.0, linestyle="-", label='cosine')

# Plot sine using green color with a continuous line of width 1 (pixels)
plt.plot(X, S, color="green", linewidth=1.0, linestyle="-", label='sine')

# Set x limits
plt.xlim(-4.0,4.0)

# Set x ticks
plt.xticks(np.linspace(-4,4,9,endpoint=True))
#directly specify ticks:
#plt.xticks( [-np.pi, -np.pi/2, 0, np.pi/2, np.pi])

# Set y limits
plt.ylim(-1.0,1.0)

#another way to set limits:
#plt.ylim(C.min()*1.1, C.max()*1.1)

# Set y ticks
plt.yticks(np.linspace(-1,1,5,endpoint=True))

# Save figure using 72 dots per inch
plt.savefig("C:\python36scripts\plot1.png",dpi=72)

#to get a legend, the plt.plot must include label="series"
plt.legend(loc='upper left', frameon=False)

plt.show()