import matplotlib.pyplot as plt
import numpy as np


# zoek het kleinste snijpunt van de functies
#     f(x) = 2^x en g(x) = x^2
# door het interval herhaaldelijk te halveren

# f(x) = 2^x
# f = blauwe lijn
def f(x):
    return x ** 3 - 8 * x - 3


# g(x) = x^2
# g = oranje
def g(x):
    return x * 0


# plot graphics
x = np.linspace(-5, 5, 50)
y_1 = f(x)
y_2 = g(x)
plt.plot(x, y_1)
plt.plot(x, y_2)

# zoek snijpunt
links = -4.0  # g(links) > f(links)
rechts = -2.0  # g(rechts) < f(rechts)

#var aanmaken voor aantal keer iteratie bij te houden
Iteraties = 0

midden = 0

# Loop maken
while rechts - links > 1E-13:
    #aantal keer iteratie ++
    Iteraties += 1

    # midden zoeken => gemiddelde zoeken van de 2 waarden
    midden = (links + rechts) / 2

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

print("Midden")
print(midden)

print("")

print("Aantal iteraties")
print(Iteraties)

plt.scatter(links, f(links), color='r')
plt.show()