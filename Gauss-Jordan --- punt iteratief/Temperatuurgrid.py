import numpy as np
import matplotlib.pyplot as plt

UB = 10  # upper boundary
LB = 40  # lower boundary
LEB = 20  # left boundary
REB = 30  # right boundary
n = 5  # meshgrid
x = np.linspace(LEB, REB, n)
y = np.linspace(LB, UB, n)

temp = np.ones((n, n))

L_2_series = []
L_2_series.append(0)
L_2_series.append(1)
iteraties = []
residual = []
i = 0

def L2(temp):
    summation = 0
    for i in range(len(temp[0])):
        for j in range(len(temp[:,0])):
            summation += temp[i][j] ** 2
    L2 = np.sqrt(summation)
    return L2

def iteration(temp,UB,LB,LEB,REB):
    for i in range(n):
        if i == 0:
            temp[i,:] = UB
        elif i == n-1:
            temp[i,:] = LB
        else:
            for j in range(n):
                if j == 0:
                    temp[i,j] = LEB
                elif j == n-1:
                    temp[i,j] = REB
                else:
                    temp[i,j] = (temp[i-1,j] + temp[i+1,j] + temp[i,j-1] + temp[i,j+1]) / 4
    L_2_series.append(L2(temp))