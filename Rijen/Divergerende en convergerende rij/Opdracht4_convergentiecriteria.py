import matplotlib.pyplot as plt

def berekening():
    x = []
    residuals = []
    iteraties = []

    i = 0
    j = 1
    k = 0

    x.append(j)
    x.append(k)

    # for i in range(200):
    #     if (i == 0):
    #         i = i+1
    #     uitkomst = ((3*i) + 5) / (1-2*i)
    #     x.append(uitkomst)

    #we berekenen hier het verschil tussen de laatste elementen van de lijst
    while abs(x[-1] - x[-2]) > 0.00001:
        i = i+1
        j = ((3*i) + 5) / (1-2*i)

        x.append(j)

        residuals.append(abs(x[-1] - x[-2]))

        iteraties.append(i)

        plt.scatter(i, j, color='r')

    print(x)

    plt.show()
    plt.yscale("log")
    plt.scatter(iteraties, residuals, color='g', label="residuals")
    plt.legend()
    plt.show()


berekening()

#besluit: functie is convergerend naar -1.5