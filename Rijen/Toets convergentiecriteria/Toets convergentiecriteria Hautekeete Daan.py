import matplotlib.pyplot as plt
import numpy as np

#opdracht a
def berekening():
    #lijsten aanmaken
    x = []
    residuals = []
    iteraties = []

    i = 0

    #startwaarden instellen en berekenen
    zijde = 12
    omtrek = 4 * zijde

    #eerste omtrek toevoegen aan de lijst
    x.append(omtrek)

    #algoritme voor een vierkant te maken met een omtrek kleiner dan 2cm
    while omtrek >= 2:
        #nieuwe zijde berekenen
        uitkomst = np.sqrt(((zijde / 2) ** 2) + ((zijde / 2) ** 2))

        #zijde gelijkstellen aan de nieuwe uitkomst
        zijde = uitkomst

        #omtrek berekenen van vierkant
        omtrek = 4 * zijde

        #omtrek toevoegen aan lijst
        x.append(float(omtrek))

        #aantal iteraties + 1
        i = i + 1

        residuals.append(abs(x[-1] - x[-2]))
        iteraties.append(i)


    print("Lijst met verschillende omtrekken:")
    #lijst met alle verschillende omtrekken weergeven
    print(x)

    print()
    #aantal iteraties weergeven => opdracht b
    print("Aantal iteraties: " + str(i))

    #residuals plotten => opdracht c
    plt.scatter(iteraties, residuals, color='g', label="residuals")
    plt.title("Toets Convergentiecriteria")
    plt.xlabel("Aantal iteraties")
    plt.ylabel("Waarde residual")
    plt.legend()
    plt.show()

berekening()

#Opdracht D: we gebruiken een list om de residuals op te slaan