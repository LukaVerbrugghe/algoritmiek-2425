import numpy as np
import matplotlib.pyplot as plt


# bepalen van nulpunt via Newton-Raphson zonder recursie + opstellen van een functie in Python

def newton_raphson(a, b, c, d, x0, tol, i):
    # afgeleide van veelterm functie

    x_n = x0
    x_n1 = 10000  # moet verschillende zijn van x0, anders geen iteraties

    while abs(x_n1 - x_n) > tol:

        #waarde van x_n aanpassen naar x_n1
        if i != 0:
            x_n = x_n1

        # aantal iteraties
        i = i + 1

        # veelterm functie
        f = a * x_n ** 3 + b * x_n ** 2 + c * x_n + d

        # afgeleide van veelterm functie
        df = 3 * a * x_n ** 2 + 2 * b * x_n + c

        #Newton raphson implementeren
        x_n1 = x_n - (f/df)

        #Waarde tonen
        print(x_n1)


newton_raphson(0, 1, 0, -2, 1.5, 1E-13, 0)
