import matplotlib.pyplot as plt
import numpy as np


# zoek het kleinste snijpunt van de functies
#     f(x) = 2^x en g(x) = x^2
# door het interval herhaaldelijk te halveren

# f(x) = 2^x
# f = blauwe lijn
def f(x):
    return 2.0 ** x


# g(x) = x^2
# g = oranje
def g(x):
    return x ** 2


# plot graphics
x = np.linspace(-3, 5, 50)
y_1 = f(x)
y_2 = g(x)
plt.plot(x, y_1)
plt.plot(x, y_2)

# zoek snijpunt
links = -1.0  # g(links) > f(links)
rechts = 0.0  # g(rechts) < f(rechts)

# Loop maken
while rechts - links > 1E-13:
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

plt.scatter(links, f(links), color='r')
plt.show()


