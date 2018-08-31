# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 13:47:57 2017

@author: 燃烧杯
"""

import numpy as np
import matplotlib.pyplot as plt

#在这里设置迭代停止条件，要多尝试一些不同数值，最好设置大一点
MAXCOUNT = 100

#数据在这里输入，依次键入每个城市的坐标
cities = np.array([
        [53.7, 15.3],
        [56.5432, 21.4188],
        [20.1050, 15.4562],
        [26.2418, 18.1760],
        [28.2694, 29.0011],
        [8.9586, 24.6635],
        [31.9499, 17.6309],
        [43.5474, 3.9061],
        [23.9222, 7.6306],
        [21.5051, 24.0909]
        ])

def calDist(xindex, yindex):
    return (np.sum(np.power(cities[xindex] - cities[yindex], 2))) ** 0.5

def calPathDist(indexList):
    sum = 0.0
    for i in range(1, len(indexList)):
        sum += calDist(indexList[i], indexList[i - 1])
    return sum

#path1长度比path2短则返回true
def pathCompare(path1, path2):
    if calPathDist(path1) <= calPathDist(path2):
        return True
    return False

def generateRandomPath(bestPath):
    a = np.random.randint(len(bestPath))
    # a取0到点总数中的一个随机值， 即起点随机
    while True:
        b = np.random.randint(len(bestPath))
        # 终点随机
        if np.abs(a - b) > 1:   # 检测相邻与否， 不相邻则跳出
            break
    if a > b:
        # 若 a>b ， 则起点为b， 终点为a， 取出相应路径
        return b, a, bestPath[b:a+1]
    else:
        return a, b, bestPath[a:b+1]

def reversePath(path):
    rePath = path.copy()
    rePath[1:-1] = rePath[-2:0:-1]  #头尾去掉一个，然后翻转
    return rePath

def updateBestPath(bestPath):
    count = 0
    while count < MAXCOUNT:
        print(calPathDist(bestPath)) # 计算路程总长度
        print(bestPath.tolist())
        start, end, path = generateRandomPath(bestPath)
        rePath = reversePath(path)
        if pathCompare(path, rePath):   # 比较翻转之后的路径， 如果原path较长则继续
            count += 1
            continue
        else:   # 若新path较短则替换
            count = 0
            bestPath[start:end+1] = rePath
    return bestPath


def draw(bestPath):
    ax = plt.subplot(111, aspect='equal')
    ax.plot(cities[:, 0], cities[:, 1], 'x', color='blue')
    for i,city in enumerate(cities):
        ax.text(city[0], city[1], str(i))
    ax.plot(cities[bestPath, 0], cities[bestPath, 1], color='red')
    plt.show()

def opt2():
    #随便选择一条可行路径
    bestPath = np.arange(0, len(cities))

    bestPath = np.append(bestPath, 0)
    # 从1号到9号按顺序走

    bestPath = updateBestPath(bestPath)

    draw(bestPath)

opt2()
