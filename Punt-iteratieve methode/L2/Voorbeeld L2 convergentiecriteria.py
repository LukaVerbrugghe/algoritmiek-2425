import numpy as np

#Beginwaarden voor parameters x1, x2, x3
x_1 = [0,1]
x_2 = [0,1]
x_3 = [0,1]

#initializeren van x, y en z
x = 0
y = 0
z = 0

def L2(x, y, z):
    summation = 0
    L2 = 0
    summation = x**2 + y **2 + z ** 2
    L2 = np.sqrt(summation)
    return L2

while abs((L2(x_1[-1], x_2[-1], x_3[-1]) ) - L2(x_1[-2], x_2[-2], x_3[-2])) > 0.001:
    x = (7 - y - z) /  2
    y = (2 + x + z) / 3
    z = (5 - x + y ) / 2

    x_1.append(x)
    x_2.append(y)
    x_3.append(z)

    print(x, y, z)