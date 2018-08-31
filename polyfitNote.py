import numpy as np
import random
import matplotlib.pyplot as plt

x = np.linspace(0, 100, num=100)
print(len(x))
print(x)
y = []
def func(x1):
    return (x1**2+0.2*x1**3)

y = func(x)
len(y)
print(y)
for i in enumerate(y):
    y[i[0]] = i[1] + random.random()*1000
print(y)

z1 = np.polyfit(x, y, 3)
print(z1)

p1 = np.poly1d(z1)

y1 = p1(x)

plt.plot(x, y1)
plt.scatter(x,y)
plt.show()
