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

    #We rekenen hier met niet afgeronde waarden, we ronden af op het einde
    x_1 = (4 - 2 * x_2 - 3 * x_3 + x_4) / 8
    x_2 = (-1 + 4 * x_1 + 5 * x_3 - 4 * x_4) / -7
    x_3 = (1 + 3 * x_2 + 2 * x_4) / 2
    x_4 = (-2 + 2 * x_1 + 5 * x_3) / 5

    # Nieuwe oplossingen toevoegen aan de lijst
    oplossingenx_1.append(x_1)
    oplossingenx_2.append(x_2)
    oplossingenx_3.append(x_3)
    oplossingenx_4.append(x_4)

print("Oplossing punt-iteratief:")
print("Oplossing x1: ", round(x_1,3), "\nOplossing x2: ", round(x_2,3), "\nOplossing x3: ", round(x_3, 3), "\nOplossing x4: ", round(x_4, 3), "\n\nAantal iteraties: ", i)

print("\n\nOplossing Gauss-Jordan:")
print("[['1.00', '0.00', '0.00', '0.00', '0.67'], ['0.00', '1.00', '0.00', '0.00', '-0.24'], ['0.00', '0.00', '1.00', '0.00', '-0.49'], ['0.00', '0.00', '0.00', '1.00', '-0.62']]")

print("\n\nConclusie: We zien dat de 2 methodes elkaar sterk gaan benaderen op gebied van de uitkomsten.\nWe zien wel dat de punt-iteratieve methode iets minder werk is om te implementeren.")