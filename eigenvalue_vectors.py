# src = https://blog.csdn.net/jiangzhouyue/article/details/52926039

import numpy as np      ##引入numpy模块
x=numpy.diag((1,2,3))   ##写入对角阵x


                     ##输出对角阵x
x = array([[1,0,0],
[0,2,0],
[0,0,3]])
a,b=numpy.linalg.elg(x) ##特征值赋值给a，对应特征向量赋值给b

                     ##特征值 1 2 3
a = array([1.,2.,3.])

                      ##特征向量
b = array([1.,0.,0.],
[0.,1.,0.],
[0.,0.,1.])
