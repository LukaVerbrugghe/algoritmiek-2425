import numpy as np
import matplotlib as plt

UB = 10 #upper bound
LB = 40 #lower bound
LeB = 20 #left bound
RB = 30 #right bound
n = 5 #grid
x = np.linspace(0,1,n)
y = np.linspace(0,1,n)

temp = np.ones((n,n)) # een array met n*n elementen die 1 zijn

#opstellen van lijsten voor convergentiecriteria toe te passen
L_2_series = []
L_2_series.append(0)
L_2_series.append(1)
iteraties = []
residual = []
i = 0
