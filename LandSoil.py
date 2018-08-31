import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import xlrd

workbook = xlrd.open_workbook('./landsoil.xls')

booksheet = workbook.sheet_by_index(0)

x_temp = booksheet.col_values(1)[1:]

y_temp = booksheet.col_values(2)[1:]


z_temp = booksheet.col_values(3)[1:]

ax = Axes3D(plt.figure(1))
booksheet2 = workbook.sheet_by_index(1)
z = booksheet2.col_values(1)[3:]
ax.plot_trisurf(x_temp, y_temp, z)

for i in range(1, 320):
    row = booksheet.row_values(i)
    if row[4] == 1:
        ax.scatter(row[1], row[2],, row[3], color='red')
    if row[4] == 2:
        ax.scatter(row[1], row[2],, row[3], color='blue')
    if row[4] == 3:
        ax.scatter(row[1], row[2], row[3], color='green')
    if row[4] == 4:
        ax.scatter(row[1], row[2],, row[3], color='yellow')
    if row[4] == 5:
        ax.scatter(row[1], row[2],, row[3], color='brown')



# ax.plot_trisurf(x_temp, y_temp, z_temp, cmap=plt.cm.jet)







ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()

#
