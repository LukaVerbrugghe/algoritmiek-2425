import matplotlib.pyplot as plt

#rijen van un = (un-1 + 10) / 2
def rij(startwaarde):
    x = []
    for i in range(10):
        x.append(startwaarde)
        startwaarde = (startwaarde + 10) / 2
    print(x)
    for i in range(len(x)):
        plt.scatter(i, x[i])
    plt.show()

rij(2)