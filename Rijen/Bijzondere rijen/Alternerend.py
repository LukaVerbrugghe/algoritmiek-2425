import matplotlib.pyplot as plt

def Alternerend(n):
    x = []
    #dit is voor recursief
    # startwaarde = 1
    # x.append(startwaarde)

    #algoritme voor alle waarden te berekenen - recursief
    # for n in range(10):
    #     uitkomst = -startwaarde * 2
    #     startwaarde = uitkomst
    #     x.append(uitkomst)

    #algoritme voor alle waarden te brekenen - expliciet
    for k in range(n):
        l = (-2)**k
        x.append(l)

    print(x)

    #Lijst plotten
    plt.plot(x)
    plt.xlabel('Index')
    plt.ylabel('Alternerend waarde')
    plt.title('Alternerend rij')
    plt.show()

Alternerend(10)
