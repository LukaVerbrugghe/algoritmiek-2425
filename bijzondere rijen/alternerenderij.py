import matplotlib.pyplot as plt

def alternerendeRij(startwaarde):
    # leeg array voor oplossingen (y-waarden)
    x = []
    # herhaal 10 keer
    for i in range(10):
        # huidige oplossing aan het array toevoegen
        x.append(startwaarde)
        # de nieuwe waarde berekenen
        startwaarde = -startwaarde * 2
    # de oplossing weergeven
    print(x)
    for i in range(len(x)):
        plt.scatter(i, x[i])
    plt.show()
alternerendeRij(1)