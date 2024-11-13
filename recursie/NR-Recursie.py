def NewtonRaphson(a, b, c, d, x0, tol, i):
    # aantal iteraties
    i = i + 1

    # veelterm functie
    f = a * x0 ** 3 + b * x0 ** 2 + c * x0 + d

    # afgeleide van veelterm functie
    df = 3 * a * x0 ** 2 + b * x0 ** 2 + c

    # conditie om uit de loop te stappen
    if abs(f) < tol:
        return x0

    # verder gaan met Newton-Raphson omdat we het antwoord nog niet gevonden hebben
    else:
        return NewtonRaphson(a, b, c, d, x0 - f / df, tol, i)

print(NewtonRaphson(1, 0, -8, -3, 0, 1E-13, 0))