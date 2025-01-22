import matplotlib.pyplot as plt

# Functie maken voor de rij
def Alternerend(n):
    x = []

    # loop om waarden toe te voegen
    for k in range(n):
        l = (-2)**n
        x.append(l)

    print(x)

    # rij plotten
    for h in range(len(x)):
        plt.scatter(h, x[h], color='r')
        plt.title('Alternerend')
        plt.xlabel('Index')
        plt.ylabel('Waarde')
    plt.show()



Alternerend(10)