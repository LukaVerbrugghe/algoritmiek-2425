import matplotlib.pyplot as plt


def berekening():
    x = []
    i = 0
    j = 1
    k = 0

    # beginwaarden in list steken
    x.append(j)
    x.append(k)

    residuals = []
    iteraties = []

    # x[-1] = laatste element van lijst
    # convergentiecriteria opstellen
    while abs(x[-1] - x[-2]) > 0.00001:
        i = i + 1
        j = -i / (i+1)

        # uitkomst toevoegen aan lijst
        x.append(j)

        # residual toevoegen aan lijst
        residuals.append(abs(x[-1] - x[-2]))

        # aantal iteraties toevoegen aan lijst
        iteraties.append(i)

        plt.scatter(i, j, color='r')

    print(x)

    plt.show()
    plt.yscale("log")
    plt.scatter(iteraties, residuals, color='g', label="residuals")
    plt.legend()
    plt.show()

    # for i in range(30):
    #     uitkomst = -i / (i+1)
    #     x.append(uitkomst)

    # for h in range(len(x)):
    #     plt.scatter(h, x[h], color='r')


berekening()

#besluit: functie convergeerd naar een waarde namelijk -1 dus we gaan convergentiecriteria opstellen
