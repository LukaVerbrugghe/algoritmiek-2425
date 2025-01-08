import matplotlib.pyplot as plt

def fibonachi():
    vorigGetal = 0
    huidigeGetal = 1
    x = []
    #repeat 10 times
    for i in range(10):
        x.append(vorigGetal)
        nieuweGetal = vorigGetal + huidigeGetal
        vorigGetal = huidigeGetal
        huidigeGetal = nieuweGetal
    print(x)

    plt.plot(x)
    plt.show()

fibonachi()