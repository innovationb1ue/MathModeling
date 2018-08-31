import xlrd
import math
import numpy as np
import scipy.stats as stats
import scipy.optimize as opt

workbook = xlrd.open_workbook('D:/附件1-葡萄酒品尝评分表.xls')
# sheet 1
booksheet = workbook.sheet_by_index(0)

wineNames_temp = booksheet.col_values(0)
wineNames = []

for i in wineNames_temp:
    if '酒样品' in i:
        wineNames.append(i)
print(wineNames, '\n', len(wineNames))

averagePoints = []
for i in enumerate(wineNames_temp):
    if '整体' in i[1]:
        averagePoints.append(booksheet.row_values(i[0])[2:])

print(averagePoints)
print(wineNames)

A_points = []
for i in averagePoints:
    total = 0
    for j in i:
        total += j
    A_points.append(total)

print(A_points)

def getAveragePointsSum(booksheet1):
    booksheet = booksheet1
    wineNames_temp = booksheet.col_values(0)
    wineNames = []

    for i in wineNames_temp:
        if '酒样品' in i:
            wineNames.append(i)
    print(wineNames, '\n', len(wineNames))

    averagePoints = []
    for i in enumerate(wineNames_temp):
        if '整体' in i[1]:
            averagePoints.append(booksheet.row_values(i[0])[2:])

    print(averagePoints)
    print(wineNames)

    A_points = []
    for i in averagePoints:
        total = 0
        for j in i:
            total += j
        A_points.append(total)

    print(A_points)
    return A_points
booksheet_B = workbook.sheet_by_index(1)
B_points = getAveragePointsSum(booksheet_B)
print(B_points)
print(A_points)

sum_A = 0
for i in A_points:
    sum_A += i

sum_B = 0
for i in B_points:
    sum_B += i

avr_A = sum_A/27
print('avr_A=',avr_A)
avr_B = sum_B/27
print('avr_B=',avr_B)

Avr = (avr_A + avr_B)/2

S = 0
for i in A_points:
    S += (i-avr_A)**2
for i in B_points:
    S += (i-avr_A)**2
print(S)


Sa2 = 27 * ((avr_A - Avr)**2 + (avr_B - Avr)**2 )
print(Sa2)

Se = S - Sa2
print(Se)

Se2 = Se/ 52
print(Se2)

F152 = Sa2/Se2
print(F152)










r, p=stats.pearsonr(A_points,B_points)
print(r, p)
