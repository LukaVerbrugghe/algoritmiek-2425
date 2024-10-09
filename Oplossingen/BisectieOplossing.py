import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x ** 3 - 8 * x - 3


x = np.linspace(-5, 5, 100)
y = f(x)
plt.plot(x, y, color='b', label='functie')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.grid(True, which='both')

# zoek de kleinste nulwaarde van f(x) = x^3 -8x - 3
i = 0  # initiële conditie aantal iteraties
links = -4.0  # f(links) < 0
rechts = -2.0  # f(rechts) > 0
iteraties = []
residual = []
tol = 1E-13
while rechts - links > tol:
    i += 1
    midden = (links + rechts) / 2
    if f(midden) < 0:
        links = midden
    else:
        rechts = midden

    iteraties.append(i)
    residual.append(rechts - links)

print("aantal iteraties: ", i)
print("kleinste nulwaarde: ", links)

plt.scatter(links, f(links), color='r', label='kleinste nulwaarde')
plt.legend()
plt.show()

plt.yscale("log")
plt.axhline(y=tol, color='g', linestyle='-', label='tolerantie')
plt.plot(iteraties, residual, label='residual')
plt.xlabel("iteraties")
plt.ylabel("residual")
plt.scatter(iteraties, residual, color='r')
plt.legend()

plt.show()
