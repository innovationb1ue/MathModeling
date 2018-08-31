import numpy as np
import xlrd


workbook = xlrd.open_workbook('D:/附件2-指标总表.xls')
booksheet = workbook.sheet_by_index(0)

Examples = []
for i in range(0, 27):
    Examples.append(booksheet.row_values(i))

print(Examples)

print(len(Examples[0][1:]))

total = []
for i in range(1, 108):
    count = 0
    col = booksheet.col_values(i)
    for j in col:
        count += j
    count = count /27
    total.append(count)


uj = total.copy()
print(uj)

sj_temp = []
for i in range(1, 108):
    count = 0
    col = booksheet.col_values(i)
    print(col)
    for j in col:
        count += (j-uj[i-1])**2
    count = count /26
    sj_temp.append(count)

print(sj_temp)
print(len(sj_temp))

sj = sj_temp.copy()

aij = []
for i in range(27):
    aij.append([])


for i in range(0, 27):
    row = booksheet.row_values(i)
    for j in range(1, 108):
        aij[i].append((row[j] - uj[j-1])/sj[j-1])

print(aij)
print(len(aij[0]))
