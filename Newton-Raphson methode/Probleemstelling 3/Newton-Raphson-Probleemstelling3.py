import numpy as np
import matplotlib.pyplot as plt


def newton_raphson(a, b, c, d, x0, tol, i):
    iteraties = []
    residual = []
    x_n = x0
    x_n1 = 0  # moet verschillende zijn van x0, anders geen iteraties

    while abs(x_n1 - x_n) > tol:
        x_n = x_n1
        i = i + 1  # aantal iteraties
        f = a * x_n ** 3 + b * x_n ** 2 + c * x_n + d  # veelterm functie
        df = 3 * a * x_n ** 2 + 2 * b * x_n + c

        if df == 0:
            df += 1

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


newton_raphson(0, 1, 0, -2, 2, 1E-13, 0)

