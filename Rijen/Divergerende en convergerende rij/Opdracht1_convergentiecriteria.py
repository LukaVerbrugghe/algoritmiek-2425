import matplotlib.pyplot as plt

def berekening():
    x = []

    for i in range(100):
        if (i == 0):
            i = i+1
        uitkomst = i**2 - (1/i)
        x.append(uitkomst)

    print(x)
    for h in range(len(x)):
        plt.scatter(h, x[h], color='r')
    plt.xlabel('Index')
    plt.ylabel('Waarde')
    plt.title('Rij')
    plt.show()

berekening()

#convergeerd niet