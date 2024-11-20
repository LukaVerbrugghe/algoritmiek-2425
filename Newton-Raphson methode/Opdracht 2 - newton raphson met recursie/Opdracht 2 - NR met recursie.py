import numpy as np
import matplotlib.pyplot as plt


def newton_raphson(a, b, c, d, x0, tol, i):
    iteraties = []
    residual = []
    # x_n = x0
    # x_n1 = 4  # moet verschillende zijn van x0, anders geen iteraties

    # while abs(x_n1 - x_n) > tol:
    #     x_n = x_n1
    #     i = i + 1  # aantal iteraties
    #     f = a * x_n ** 3 + b * x_n ** 2 + c * x_n + d  # veelterm functie
    #     df = 3 * a * x_n ** 2 + 2 * b * x_n + c
    #     if df == 0:
    #         df += 1
    #     x_n1 = x_n - f / df
    #     iteraties.append(i)
    #     residual.append(abs(x_n1 - x_n))

    i = i + 1

    # functie opstellen
    f = a * x0 ** 3 + b * x0 ** 2 + c * x0 + d

    # Afgeleide berekenen
    df = 3 * a * x0 ** 2 + 2 * b * x0 + c

    # Bepaal conditie om uit de loop te gaan
    if abs(f) < tol:
        x = np.linspace(-5, 5, 100)
        y = a * x ** 3 + b * x ** 2 + c * x + d
        plt.plot(x, y, color='b', label='functie')
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')
        plt.grid(True, which='both')
        print("aantal iteraties: ")
        print(i)
        print("nulwaarde")
        print(x0)
        plt.scatter(x0, f, color='r', label='kleinste nulwaarde')
        plt.legend()
        return x0

    else:
        # Recursie maken
        return newton_raphson(a, b, c, d, x0 - f / df, tol, i)


def horner(a, b, c, d, x0, tol, i):
    x0 = newton_raphson(a, b, c, d, x0, tol, i)
    b = a * x0 + b
    c = b * x0 + c
    d = c * x0 + d
    print('de waarde d moet nul zijn', d)
    return (a, b, c)


def vierkantsvergelijking(a, b, c):
    D = float(b ** 2 - 4 * a * c)
    if D > 0:
        return ((-b + np.sqrt(D)) / (2 * a), (-b - np.sqrt(D)) / (2 * a))
    elif D == 0:
        return -b / (2 * a), None
    else:
        print("Deze tweedegraadsvergelijking heeft geen snijpunten met de x-as")
        return None, None


def vind_alle_nulpunten(a, b, c, d, x0, tol, i):
    a, b, c = horner(a, b, c, d, x0, tol, i)
    u = vierkantsvergelijking(a, b, c)
    if len(u) > 0:
        for i in range(len(u)):
            plt.scatter(u[i], 0, color='r')
    plt.grid(True, which='both')
    plt.show()

vind_alle_nulpunten(1, 0, -8, -3, 2.5, 1E-13, 0)


