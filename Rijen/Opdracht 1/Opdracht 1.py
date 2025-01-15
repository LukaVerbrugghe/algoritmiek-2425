import matplotlib.pyplot as plt
import numpy as np

def berekening():
    x= []

    # algoritme voor alle waarden te berekenen
    for i in range(10):
        #als de eerste term 0 is, dan gebruiken we U1
        if i == 0:
            uitkomst = 2
        else:
            uitkomst = (x[i-1] + 10) / 2

        x.append(uitkomst)

    # lijst weergeven
    print(x)

    # Lijst plotten
    for h in range(len(x)):
        plt.scatter(h,x[h],color = 'r')
    plt.xlabel('Index')
    plt.ylabel('Waarde')
    plt.title('Rij')
    plt.show()

berekening()