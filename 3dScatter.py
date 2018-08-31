import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


ax = Axes3D(plt.figure(1))
ax.scatter(1,1,1)
xs = np.linspace(0,100, num= 50)
ys = np.linspace(0, 50, num=50)
zs = np.linspace(0, 10, num=50)
ax.plot(xs,ys,zs)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()
