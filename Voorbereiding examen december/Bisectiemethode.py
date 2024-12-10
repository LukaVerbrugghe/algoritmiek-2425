import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return 2.0 ** x

def g(x):
    return x ** 2

x = np.linspace(-3,5,50)
y_1 = f(x)
y_2 = g(x)
plt.plot(x,y_1)
plt.plot(x,y_2)

# Snijpunt zoeken
links = -1.0
rechts = 0.0

while rechts - links > 1E-13:
    midden = (links + rechts) / 2
    if g(midden) > f(midden):
        links = midden
    else:
        rechts = midden

print(links)
plt.scatter(links,f(links),color = 'r')
plt.show()