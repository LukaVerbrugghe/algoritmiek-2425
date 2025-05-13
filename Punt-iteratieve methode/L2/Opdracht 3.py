import numpy as np

#beginwaarden instellen
x_1 = [0,1]
x_2 = [0,1]
x_3 = [0,1]
x_4 = [0,1]

#initializeren van x1, x2, x3 en x4
x1 = 0
x2 = 0
x3 = 0
x4 = 0

def L2(x1, x2, x3, x4):
    summation = (x1**2 + x2**2 + x3**2 + x4**2)
    L2 = np.sqrt(summation)
    return L2


while abs((L2(x_1[-1], x_2[-1], x_3[-1], x_4[-1]) ) - L2(x_1[-2], x_2[-2], x_3[-2], x_4[-2])) > 0.001:
    x1 = (4 - 2*x2 - 3*x3 + x4) / 8
    x2 = (-1 + 4*x1 + 5*x3 - 4*x4) / -7
    x3 = (1 + 3*x2 + 2*x4) / 2
    x4 = (-2 + 2*x1 + 5*x3) / 5

    x_1.append(x1)
    x_2.append(x2)
    x_3.append(x3)
    x_4.append(x4)

    print("\nx1:", round(x1, 3), "\nx2:", round(x2, 3), "\nx3:", round(x3, 3), "\nx4:", round(x4, 3))

#vergelijking met Gauss-Jordan:
#[['1.00', '0.00', '0.00', '0.00', '0.67'], ['0.00', '1.00', '0.00', '0.00', '-0.24'], ['0.00', '0.00', '1.00', '0.00', '-0.49'], ['0.00', '0.00', '0.00', '1.00', '-0.62']]
