import matplotlib.pyplot as plt

from Oplossingen.Bissectiemethode.Bissectiemethode_oplossing import iteraties


def berekening():
    x = []

    for i in range(100):
        if (i == 0):
            i = i+1
        uitkomst = -i / (i+1)
        x.append(uitkomst)

    print(x)
    for h in range(len(x)):
        plt.scatter(h, x[h], color='r')
    plt.xlabel('Index')
    plt.ylabel('Waarde')
    plt.title('Rij')
    plt.show()

# berekening()

# Besluit: rij convergeert naar -1 => convergentiecriteria opstellen

def berekeningMetConvergentiecriteria():
    x = []

    i = 0
    j = 1
    k = 0

    # beginwaarden in list steken
    x.append(j)
    x.append(k)

    residuals = []
    iteraties = []

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
    plt.xlabel('Index')
    plt.ylabel('Waarde')
    plt.title('Rij')
    plt.show()

    print(x)

    plt.yscale('log')
    plt.scatter(iteraties, residuals)
    plt.xlabel('Aantal iteraties')
    plt.ylabel('Residual')
    plt.title('Rij')
    plt.show()

berekeningMetConvergentiecriteria()

