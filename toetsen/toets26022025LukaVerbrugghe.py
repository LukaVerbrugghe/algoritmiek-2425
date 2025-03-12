import matplotlib.pyplot as plt
import numpy as np

# In een vierkant met zijde 12cm vormen de middens van de vier zijden opnieuw een vierkant. Hierop herhaal je deze procedure. Je bekomt zo een groot aantal vierkanten in elkaar.
# Gevraagd: Een algoritme waarbij je deze procedure minstens moet herhalen om een vierkant te bekomen met omtrek kleiner dan 2 cm
zijde = 12
aantalIteraties = 0
x = [12]

# we stoppen wanneer de zijde kleiner is dan 2 cm (2)
while(zijde > 2):
    aantalIteraties += 1
    # bereken nieuwe zijde met de stelling van pytagoras
    zijde = np.sqrt((zijde/2)**2 + (zijde/2)**2)
    x.append(zijde)
print("Aantal iteraties:")
print(aantalIteraties)
print("")
print("")
print("X-punten op de grafiek:")
print(x)

# residuals en zijde zijn in dit geval altijd hetzelfde
for i in range(len(x)):
    plt.scatter(i, x[i], color='r')
    plt.title("Residual en lengte zijde: ")
    plt.xlabel("aantal iteraties")
    plt.ylabel("lengte zijde")
plt.show()

# antwoord op vraag d
# we gebruiken dezelfde list voor het opslaan van de residuals als voor het opslaan van de lengte van de zijde omdat deze hetzelfde zijn