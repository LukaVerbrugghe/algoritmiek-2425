import matplotlib.pyplot as plt


def berekening():
    x = []
    i = 0
    j = 1
    k =0

    #beginwaarden in list steken
    x.append(j)
    x.append(k)

    residuals = []
    iteraties = []

    #x[-1] = laatste element van lijst
    #convergentiecriteria opstellen
    while abs(x[-1] - x[-2]) > 0.00001:
        i = i + 1
        j = (-5*i) / (1 + 25*i)

        #uitkomst toevoegen aan lijst
        x.append(j)

        #residual toevoegen aan lijst
        residuals.append(abs(x[-1] - x[-2]))

        #aantal iteraties toevoegen aan lijst
        iteraties.append(i)

        plt.scatter(i, j, color='r')

    plt.show()
    plt.yscale("log")
    plt.scatter(iteraties, residuals, color='g', label="residuals")
    plt.legend()
    plt.show()

berekening()

#besluit: functie convergeerd naar een waarde namelijk -0,2 dus we gaan convergentiecriteria opstellen
