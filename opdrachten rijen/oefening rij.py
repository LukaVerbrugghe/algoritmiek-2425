import matplotlib.pyplot as plt

#rijen van un = (un-1 + 10) / 2
def rij(startwaarde):
    # een leeg array voor oplossing
    x = []
    # we willen 10 rijen
    for i in range(10):
        x.append(startwaarde)
        # functievoorschrift
        startwaarde = (startwaarde + 10) / 2
    # de oplossing weergeven
    print(x)
    for i in range(len(x)):
        plt.scatter(i, x[i])
    plt.show()

rij(2)