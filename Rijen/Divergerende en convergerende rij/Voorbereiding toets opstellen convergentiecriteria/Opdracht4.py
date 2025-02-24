import matplotlib.pyplot as plt

def berekening():
    x = []

    for i in range(100):
        if (i == 0):
            i = i+1
        uitkomst = ((3*i) + 5) / (1-2*i)
        x.append(uitkomst)

    print(x)
    for h in range(len(x)):
        plt.scatter(h, x[h], color='r')
    plt.xlabel('Index')
    plt.ylabel('Waarde')
    plt.title('Rij')
    plt.show()

# berekening()

# Besluit: rij convergeerd naar -1.5 => convergentiecriteria opstellen

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
        j = ((3*i) + 5) / (1-2*i)

        # uitkomst toevoegen aan lijst
        x.append(j)

        # residual toevoegen aan lijst
        residuals.append(abs(x[-1] - x[-2]))

        # aantal iteraties toevoegen aan lijst
        iteraties.append(i)

        plt.scatter(i, j, color='r')

    print(x)

    plt.xlabel('Index')
    plt.ylabel('Waarde')
    plt.title('Rij')
    plt.show()


    plt.yscale('log')
    plt.scatter(iteraties, residuals, color='g', label='Residuals')
    plt.xlabel('Index')
    plt.ylabel('Residual')
    plt.title('Rij')
    plt.legend()
    plt.show()

berekeningMetConvergentiecriteria()