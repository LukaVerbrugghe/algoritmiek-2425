import matplotlib.pyplot as plt

def alternerendeRij(startwaarde):
    x = []
    # herhaal 10 keer
    for i in range(10):
        x.append(startwaarde)
        startwaarde = -startwaarde * 2
    print(x)
    for i in range(len(x)):
        plt.scatter(i, x[i])
    plt.show()
alternerendeRij(1)