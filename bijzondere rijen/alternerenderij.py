def alternerendeRij(startwaarde):
    x = []
    # herhaal 10 keer
    for i in range(10):
        x.append(startwaarde)
        startwaarde = -startwaarde * 2
    print(x)

alternerendeRij(1)