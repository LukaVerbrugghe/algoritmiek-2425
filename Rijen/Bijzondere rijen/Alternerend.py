def Alternerend(n):
    x = []
    startwaarde = 1
    x.append(startwaarde)

    #algoritme voor alle waarden te berekenen
    for n in range(10):
        uitkomst = -startwaarde * 2
        startwaarde = uitkomst
        x.append(uitkomst)

    print(x)

Alternerend(10)
