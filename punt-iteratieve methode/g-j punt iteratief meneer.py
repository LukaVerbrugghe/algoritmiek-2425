import numpy as np

x_1 = [0,1]
x_2 = [0,1]
x_3 = [0,1]

x = 0
y = 0
z = 0

# functie voor de L2 norm
def L2(x,y,z):
    summation = 0
    l2 = 0
    summation = x**2 + y**2 + z**2
    l2 = np.sqrt(summation)
    return l2

while abs(L2(x_1[-1],x_2[-1],x_3[-1]) - L2(x_1[-2],x_2[-2],x_3[-2])) > 0.001:
    x = (7 - y -z) / 2
    y = (2 + x + z) / 3
    z = (5 - x + y) / 2

    x_1.append(x)
    x_2.append(y)
    x_3.append(z)

# uitkomst printen
print(x,y,z)