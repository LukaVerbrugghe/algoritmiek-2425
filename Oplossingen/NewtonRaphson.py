import numpy as np
import matplotlib.pyplot as plt


def newton_raphson(a, b, c, d, x0, tol, i):
    iteraties = []
    residual = []
    x_n = x0
    x_n1 = 4  # moet verschillende zijn van x0, anders geen iteraties, mag iets anders zijn ook

    while abs(x_n1 - x_n) > tol:
        x_n = x_n1
        i = i + 1  # aantal iteraties
        f = a * x_n ** 3 + b * x_n ** 2 + c * x_n + d  # veelterm functie
        df = 3 * a * x_n ** 2 + 2 * b * x_n + c
        if df == 0:
            df = 1
        x_n1 = x_n - f / df
        iteraties.append(i)
        residual.append(abs(x_n1 - x_n))

    x = np.linspace(-5, 5, 100)
    y = a * x ** 3 + b * x ** 2 + c * x + d
    plt.plot(x, y, color='b', label='functie')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.grid(True, which='both')
    print("aantal iteraties: ")
    print(i)
    print("nulwaarde")
    print(x_n1)
    plt.scatter(x_n1, f, color='r', label='kleinste nulwaarde')
    plt.legend()
    plt.show()

    plt.yscale("log")
    plt.plot(iteraties, residual)
    plt.scatter(iteraties, residual, color='r')
    plt.axhline(y=tol, color='g', linestyle='-', label='tolerantie')
    plt.xlabel("iteraties")
    plt.ylabel("residual")

    plt.legend()
    plt.show()

    return x_n1

def horner(a, b, c, d, x0, tol, i):
    x0 = newton_raphson(a, b, c, d, x0, tol, i)
    b = x0 * a + b
    c = x0 * b + c
    d = x0 * c + d
    return a, b, c

def discriminant(a, b, c):
    D = float(b ** 2 - 4 * a * c)
    print("D = ", D)
    if D > 0:
        return ((-b + np.sqrt(D)) / (2 * a), (-b - np.sqrt(D)) / (2 * a))
    elif D == 0:
        return -b / (2 * a), None
    else:
        print("D < 0, geen nulpunten")
        return None, None

def vinden_alle_nulpunten(a, b, c, d, x0, tol, i):
    a, b, c = horner(a, b, c, d, x0, tol, i)
    U = discriminant(a, b, c)
    if len(U) > 0:
        for i in range(len(U)):
            plt.scatter(U[i], 0, color='r')
    plt.grid(True, which='both')
    plt.show()

horner(1, 0, -8, -3, 3, 1E-13, 0)
discriminant(1, 0, -8)
vinden_alle_nulpunten(1, 0, -8, -3, 3, 1E-13, 0)