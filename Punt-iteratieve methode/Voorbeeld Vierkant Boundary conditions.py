import math

import numpy as np
import matplotlib.pyplot as plt

#initiele waarden instellen
x = 0
y = 0
z = 0

x_1 = []
x_2 = []
x_3 = []

x_1.append(x)
x_2.append(y)
x_3.append(z)

x = (7 - y - z) / 2
y = (2 + x + z) / 3
z = (5 - x + y) / 2

x_1.append(x)
x_2.append(y)
x_3.append(z)

UB = 10  # upper boundary
LB = 40  # lower boundary
LEB = 20  # left boundary
REB = 30  # right boundary

n = 5 #meshgrid
x = np.linspace(0,1,n) #2D
y = np.linspace(0,1,n) #2D

temp = np.ones((n,n)) #5x5 matrix maken met waarden 1

#opstellen van lijsten voor convergentiecriteria toe te passen
L_2_series = []
L_2_series.append(0)
L_2_series.append(1)

iteraties = []
residual = []
i = 0

def L2 (x,y,z): #L2 norm
    summation = 0
    L2 = 0
    summation = x**2 + y**2 + z**2
    L2 = math.sqrt(summation)
    return L2

while abs(L2(x_1[-1], x_2[-1], x_3[-1]) - L2(x_1[-2], x_2[-2], x_3[-2])) > 0.001:
    i += 1
    x = (7 - y - z) / 2
    y = (2 + x + z) / 3
    z = (5 - x + y) / 2

    x_1.append(x)
    x_2.append(y)
    x_3.append(z)

    L_2_series.append(L2(x,y,z))
    iteraties.append(i)
    residual.append(abs(L2(x_1[-1], x_2[-1], x_3[-1]) - L2(x_1[-2], x_2[-2], x_3[-2])))
