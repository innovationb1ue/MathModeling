# ref = https://blog.csdn.net/your_answer/article/details/79131000

from scipy import optimize as op
import numpy as np


'''
solve the problems
max(z) = 2x1 + 3x2 -5x3
    s.t.
        x1 + x2 + x3 = 7
        2x1 -5x2 + x3 >= 10
        x1 + 3x2 + x3 <= 12
        x1,x2,x3 > 0


'''

# linear coefficient
c=np.array([2,3,-5])
# input coefficient, change the form to less or equal to xxx.
A_ub=np.array([[-2,5,-1],[1,3,1]])
# costant
B_ub=np.array([-10,12])

# equation limit
A_eq=np.array([[1,1,1]])
# costant of equation
B_eq=np.array([7])

# set boudary of variables
x1=(0,7)
x2=(0,7)
x3=(0,7)

# use -c if solve for max.
res=op.linprog(-c,A_ub,B_ub,A_eq,B_eq,bounds=(x1,x2,x3))

print(res)
