import matplotlib.pyplot as plt

def rij(startwaarde):
    x = []
    # de eerste 10 termen
    for i in range(10):
        x.append(startwaarde)
        startwaarde = (-2 * startwaarde ** 2 + startwaarde + 4)/2
    print(x)
    for i in range(len(x)):
        plt.scatter(i, x[i], color='r')
    plt.show()

rij(2)

# welke datastructuur heb ik gebruikt?
# een array

# waarom heb ik deze datastructuur gebruikt?
# om de verschillende waarden van de functie op te slaan voor later de volledige rij en de grafiek te kunnen opstellen

# welk besluit neem ik uit het gedrag op oneindig uit dit voorschrift
# de rij waarden 2, -1 en 0.5 blijven terugkomen (de rij is dus (un): 2, -1, 0.5, 2, -1, 0.5, ...