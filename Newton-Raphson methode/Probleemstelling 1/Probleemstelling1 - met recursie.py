import numpy as np
import matplotlib.pyplot as plt


# bepalen van nulpunt + recursie + opstellen van een functie in Python

def newton_raphson(a, b, c, d, x0, tol, i):
    # aantal iteraties
    i = i + 1

    # veelterm functie
    f = a * x0 ** 3 + b * x0 ** 2 + c * x0 + d

    # afgeleide van veelterm functie
    df = 3 * a * x0 ** 2 + b * x0 ** 2 + c


    # if (Vul aan, welke conditie hier?):


    # else (Vul aan, welke conditie hier?)


newton_raphson(0, 1, 0, -2, 1.5, 1E-13, 0)
