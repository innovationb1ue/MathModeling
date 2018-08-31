import numpy as np
import matplotlib.pyplot as plt1
import xlrd
from mpl_toolkits.mplot3d import Axes3D

wordbook = xlrd.open_workbook('C:/Users/Administrator/Desktop/01.xlsx')

plt = Axes3D(plt1.figure(1))


booksheet = wordbook.sheet_by_index(0)

x1 = booksheet.col_values(0)
y1 = booksheet.col_values(4)


x2 = booksheet.col_values(1)
y2 = booksheet.col_values(5)

x3 = booksheet.col_values(2)
y3 = booksheet.col_values(6)
plt.set_xlabel('X Label')
plt.set_ylabel('Y Label')
plt.set_zlabel('Z Label')

plt.scatter(x1,y1, color='blue', alpha=0.5)
plt.scatter(x2,y2, color='red', alpha=0.5)
plt.scatter(x3,y3, color = 'yellow', alpha=0.5)


f1 = np.polyfit(x1,y1, 1)
f = np.poly1d(f1)

plt.plot(x1, f(x1), color='black')

plt1.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.viridis)

plt.show()
