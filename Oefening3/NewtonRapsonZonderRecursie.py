import numpy as np
import matplotlib.pyplot as plt


# bepalen van nulpunt via Newton-Raphson zonder recursie + opstellen van een functie in Python

def newton_raphson(a, b, c, d, x0, tol, i):
    # afgeleide van veelterm functie

    x_n = x0
    x_n1 = 10000  # moet verschillende zijn van x0, anders geen iteraties

    while abs(x_n1 - x_n) > tol:
        if i != 0:
            x_n = x_n1
        i = i + 1  # aantal iteraties
        f = a * x_n ** 3 + b * x_n ** 2 + c * x_n + d  # veelterm functie
        df = 3 * a * x_n ** 2 +2 * b * x_n + c

        x_n1 = x_n - f / df

        print(x_n1)
        if abs(x_n1 - x_n) <= tol:
            break
    print(x_n)

newton_raphson(0, 1, 0, 2, 1.5, 1E-2, 0)
