#initiele waarde instellen
x_1 = 0
x_2 = 0
x_3 = 0
x_4 = 0

#aantal iteraties
i = 0

#lists aanmaken voor de oplossingen
oplossingenx_1 = []
oplossingenx_2 = []
oplossingenx_3 = []
oplossingenx_4 = []

#initiele waarde toevoegen aan list
oplossingenx_1.append(x_1)
oplossingenx_2.append(x_2)
oplossingenx_3.append(x_3)
oplossingenx_4.append(x_4)

x_1 = (4 - 2*x_2 - 3*x_3 + x_4) / 8
x_2 = (-1 + 4*x_1 + 5*x_3 - 4*x_4) / -7
x_3 = (1 + 3*x_2 + 2*x_4) / 2
x_4 = (-2 + 2*x_1 + 5*x_3) / 5

#Nieuwe oplossingen toevoegen aan de lijst
oplossingenx_1.append(x_1)
oplossingenx_2.append(x_2)
oplossingenx_3.append(x_3)
oplossingenx_4.append(x_4)

#convergentiecriteria opstellen
while(abs(oplossingenx_2[-1] - oplossingenx_2[-2]) > 0.001):
    i += 1

    x_1 = (4 - 2 * x_2 - 3 * x_3 + x_4) / 8
    x_2 = (-1 + 4 * x_1 + 5 * x_3 - 4 * x_4) / -7
    x_3 = (1 + 3 * x_2 + 2 * x_4) / 2
    x_4 = (-2 + 2 * x_1 + 5 * x_3) / 5

    # Nieuwe oplossingen toevoegen aan de lijst
    oplossingenx_1.append(x_1)
    oplossingenx_2.append(x_2)
    oplossingenx_3.append(x_3)
    oplossingenx_4.append(x_4)

print("Oplossingen\nOplossing x1: ", x_1, "\nOplossing x2: ", x_2, "\nOplossing x3: ", x_3, "\nOplossing x4: ", x_4, "\nAantal iteraties: ", i)