from matplotlib.widgets import ToolLineHandles


def NewtonRaphson(a, b, c, d, x0, tol, i):
    i += 1

    #functie opstellen
    f = a * x0 ** 3 + b * x0 ** 2 + c * x0 + d

    #Afgeleide berekenen
    df = 3 * a * x0 ** 2 + 2 * b * x0 + c

    #Bepaal conditie om uit de loop te gaan
    if abs(f) < tol:
        return x0
    else:
        if df == 0:
            df += 1
        else:
            # Recursie maken
            return NewtonRaphson(a, b, c, d, x0 - f / df, tol, i)

print(NewtonRaphson(1,0,-8,-3,0,1E-13,0))