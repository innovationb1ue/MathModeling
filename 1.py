            import numpy as np
import math
import xlrd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

workbook = xlrd.open_workbook('C:/Users/Administrator/Documents/Tencent Files/517262600/FileRecv/5、历年建模竞赛题目/2010-2017年全国数学建模竞赛题/CUMCM2017Problems/B/附件一：已结束项目任务数据.xls')

booksheet = workbook.sheet_by_index(0)
latitude = booksheet.col_values(1)[1:]
longitude = booksheet.col_values(2)[1:]

print(len(latitude))
print(len(longitude))

coordinates = []
for i in range(0,len(latitude)):
    coordinates.append([latitude[i], longitude[i]])


for i in coordinates:
    plt.scatter(i[0], i[1])

# ua为A精度， va为纬度
def distance(ua,va,ub,vb):
    return 6370*math.acos(math.cos(ua-ub)*math.cos(va)*math.cos(vb) + math.sin(va)*math.sin(vb))

d = 10
finalDict = {}
for coordinate in coordinates:
    coordinate_temp = coordinates.copy()
    coordinate_temp.remove(coordinate)
    count = 0
    for coordinate1 in coordinate_temp:
        if distance(coordinate[1], coordinate[0], coordinate1[1], coordinate1[0]) <= 20:
            count += 1
    finalDict[str(coordinate)] = count

print(finalDict)


x = np.linspace(0, 100, num= 1000)
y = np.linspace(0, 100, num= 1000)

result = []
for i in x:
    for j in y:
        if math.sin(i)*math.cos(j) <= 1/3:
            result.append([i, j])
print(len(result))

x, y = [], []
for i in result:
    x.append(i[0])
    y.append(i[1])

plt.scatter(x,y)
plt.xlim(0,1)
plt.ylim(0, 10)


plt.show()
