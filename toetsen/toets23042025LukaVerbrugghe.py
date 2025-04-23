#initiele waarde instellen
X_2 = 0
x_2 = 0
X_3 = 0
X_4 = 0

#aantal iteraties
i = 0

#lists aanmaken voor de oplossingen
oplossingenX_1 = []
oplossingenX_2 = []
oplossingenX_3 = []
oplossingenX_4 = []

#initiele waarde toevoegen aan list
oplossingenX_1.append(X_2)
oplossingenX_2.append(x_2)
oplossingenX_3.append(X_3)
oplossingenX_4.append(X_4)

X_2 = (4 - 2 * x_2 - 3 * X_3 + X_4) / 8
x_2 = (-1 + 4 * X_2 + 5 * X_3 - 4 * X_4) / -7
X_3 = (1 + 3 * x_2 + 2 * X_4) / 2
X_4 = (-2 + 2 * X_2 + 5 * X_3) / 5

#Nieuwe oplossingen toevoegen aan de lijst
oplossingenX_1.append(X_2)
oplossingenX_2.append(x_2)
oplossingenX_3.append(X_3)
oplossingenX_4.append(X_4)

#convergentiecriteria opstellen
while abs(oplossingenX_2[-1] - oplossingenX_2[-2]) > 0.001:
    i += 1

    X_2 = (4 - 2 * x_2 - 3 * X_3 + X_4) / 8
    x_2 = (-1 + 4 * X_2 + 5 * X_3 - 4 * X_4) / -7
    X_3 = (1 + 3 * x_2 + 2 * X_4) / 2
    X_4 = (-2 + 2 * X_2 + 5 * X_3) / 5

    # Nieuwe oplossingen toevoegen aan de lijst
    oplossingenX_1.append(X_2)
    oplossingenX_2.append(x_2)
    oplossingenX_3.append(X_3)
    oplossingenX_4.append(X_4)

print("Oplossingen\nOplossing x1: ", X_2, "\nOplossing x2: ", x_2, "\nOplossing x3: ", X_3, "\nOplossing x4: ", X_4, "\nAantal iteraties: ", i)


# We berekenen handmatig de oplossingen als manier van controle
# Voor formule 1 kom ik 3.985 uit, ik ga er dus vanuit dat de oplossing correct is
# Voor formule 2 kom ik -0.957 uit, ik ga er dus vanuit dat de oplossing correct is
# Voor formule 3 kom ik 1.01 uit, ik ga er dus vanuit dat de oplossing correct is
# Voor formule 4 kom ik -1.998 uit, ik ga er dus vanuit dat de oplossing correct is


# Vergelijk deze oplossing met de Gauss-Jordan methode

# output GaussJordan.py (met de matrix ingevuld voor de huidige vergelijkingen)
# [['1.00', '0.00', '0.00', '0.00', '0.67'], ['0.00', '1.00', '0.00', '0.00', '-0.24'], ['0.00', '0.00', '1.00', '0.00', '-0.49'], ['0.00', '0.00', '0.00', '1.00', '-0.62']]

# Ik vergelijk als volgt: OPL_PUNT_ITERATIEF | OPL_GAUSS_JORDAN
# !!!! Ik rond of op 3 getallen na de komma !!!!
# X_1: 0.659 | 0.67
# X_2: -0.247 | -0.24
# X_3: -0.466 | -0.49
# X_4: -0.602 | -0.62

# Conclusie
# We zien dat de punt iteratieve methode nauwkeuriger is dan de Gauss-Jordan methode.