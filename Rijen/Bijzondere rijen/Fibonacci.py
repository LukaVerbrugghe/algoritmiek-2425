import matplotlib.pyplot as plt
import numpy as np

def Fibonacci(n):
    x= []
    vorigGetal = 0
    nieuwGetal = 1
    x.append(vorigGetal)
    x.append(nieuwGetal)

    #algoritme voor alle waarden te berekenen
    for n in range(10):
        #fibonacci
        uitkomst = vorigGetal + nieuwGetal
        x.append(uitkomst)
        vorigGetal = nieuwGetal
        nieuwGetal = uitkomst

    return x



x = Fibonacci(10)
print(x)


for h in range(len(x)):
    plt.scatter(h,x[h],color = 'r')
plt.xlabel('Index')
plt.ylabel('Fibonacci waarde')
plt.title('Fibonacci rij')
plt.show()