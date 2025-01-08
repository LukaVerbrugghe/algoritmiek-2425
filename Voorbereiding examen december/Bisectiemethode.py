import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x ** 3 - 8 * x - 3

x = np.linspace(-3,5,50)
y_1 = f(x)
plt.plot(x,y_1)

# Snijpunt zoeken
links = -4.0
rechts = -2.0

i = 0

while rechts - links > 1E-13:
    i+=1
    midden = (links + rechts) / 2
    if midden**3 - 8 * midden - 3 < 0:
        links = midden
    else:
        rechts = midden

print(i)
print(links)
plt.scatter(links,f(links),color = 'r')
plt.show()