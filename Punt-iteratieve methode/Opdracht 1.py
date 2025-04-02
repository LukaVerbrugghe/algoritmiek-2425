#initiele waarden instellen
x_1 = 0
x_2 = 0
x_3 = 0

#Aantal iteraties instellen
i = 0

#lists aanmaken voor de oplossingen
oplossingenx_1 = []
oplossingenx_2 = []
oplossingenx_3 = []

#De initiele waarde opslaan in de list
oplossingenx_1.append(x_1)
oplossingenx_2.append(x_2)
oplossingenx_3.append(x_3)

x_1 = (7 - x_2 - x_3) / 2
x_2 = (2 + x_1 + x_3) / 3
x_3 = (5 - x_1 + x_2) / 2

#Nieuwe oplossingen opslaan in list
oplossingenx_1.append(x_1)
oplossingenx_2.append(x_2)
oplossingenx_3.append(x_3)

# Convergentiecriterie opstellen
while(abs(oplossingenx_1[-1] - oplossingenx_1[-2]) > 0.001):
    i += 1
    x_1 = round(((7 - x_2 - x_3) / 2), 3)
    x_2 = round(((2 + x_1 + x_3) / 3), 3)
    x_3 = round(((5 - x_1 + x_2) / 2),3)

    oplossingenx_1.append(x_1)
    oplossingenx_2.append(x_2)
    oplossingenx_3.append(x_3)

print("Oplossingen\nOplossing x1: ", x_1, "\nOplossing x2: ", x_2, "\nOplossing x3: ", x_3, "\nAantal iteraties: ", i)