import numpy as np
import xlrd

notebook = xlrd.open_workbook('D:/算算算.xlsx')
booksheet = notebook.sheet_by_index(0)


matrix1 = []
for i in range(27):
    matrix1.append(booksheet.row_values(i))

print(matrix1)
print(len(matrix1))

booksheet2 = notebook.sheet_by_index(1)
matrix2 = []
for i in range(107):
    matrix2.append(booksheet2.row_values(i))

print(len(matrix2))


# 2-D array: 2 x 3
two_dim_matrix_one = matrix1
# 2-D array: 3 x 2
two_dim_matrix_two = matrix2

two_multi_res = np.dot(two_dim_matrix_one, two_dim_matrix_two)

print(len(two_multi_res[0]))


matrix3 = [19.986,13.055,11.459,8.733,6.706,5.575,5.250,4.195,3.123,3.037,2.433,2.259,1.867,1.705,1.591,1.524,1.348,1.128,0.998,]

two_dim_matrix_one = two_multi_res
# 2-D array: 3 x 2
two_dim_matrix_two = matrix3

two_multi_res = np.dot(two_dim_matrix_one, two_dim_matrix_two)

print(two_multi_res)


final_temp = {}


for i in enumerate(two_multi_res):
    final_temp[i[1]] = i[0]

print(final_temp)

final_keys = sorted(final_temp)

print(final_keys)

final_order = []
for i in final_keys:
    final_order.append(final_temp[i])
    print(final_order)
