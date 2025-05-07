import numpy as np

x_1 = [0,1]
x_2 = [0,1]
x_3 = [0,1]

x = 0
y = 0
z = 0

i = 0

# functie voor de L2 norm
def L2(x,y,z):
    summation = 0
    l2 = 0
    summation = x**2 + y**2 + z**2
    l2 = np.sqrt(summation)
    return l2

while abs(L2(x_1[-1],x_2[-1],x_3[-1]) - L2(x_1[-2],x_2[-2],x_3[-2])) > 0.001:
    x = (5 - 2 * y - 4 * z) / 10
    y = (16 - 4 * x - 5 * z) / 9
    z = (12 + 3 * y) / 2

    print("iteratie",i)
    x_1.append(x)
    print("x",x)
    x_2.append(y)
    print("y",y)
    x_3.append(z)
    print("z",z)
    print()
    i+=1

# uitkomst printen
print()
print("Na",i,"iteraties")
print(round(x,2),round(y,2),round(z,2))