import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x ** 3 - 8 * x - 3

def g(x):
    return x * 0

# plot graphics
x = np.linspace(-5, 5, 500)
y_1 = f(x)
y_2 = g(x)
plt.plot(x, y_1)
plt.plot(x, y_2)

# zoek snijpunt
links = -3.0
rechts = -2.0

aantalIteraties = 1
# Loop maken
while rechts - links > 1E-13:
    print("START NU ITERATIE:")
    print(aantalIteraties)
    print()
    aantalIteraties += 1
    # midden zoeken => gemiddelde zoeken van de 2 waarden
    midden = (links + rechts) / 2

    print("Midden")
    print(midden)

    # VUL AAN: welke lus hier? => door leerlingen
    # midden = # VUL AAN: hoe bepaal je de waarde van midden?

    # Nieuwe grenzen stellen
    # if # VUL AAN: welke conditie?
    if (g(midden) > f(midden)):
        # VUL AAN: wat verander je hier?
        links = midden
        # else:
    else:
        # VUL AAN: wat verander je hier?
        rechts = midden

    print("Links")
    print(links)
    print("Rechts")
    print(rechts)
    print()
    print()
    print()

plt.scatter(links, f(links), color='r')
plt.show()