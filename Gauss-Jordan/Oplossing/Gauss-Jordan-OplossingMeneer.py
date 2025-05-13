def verwissel(stelsel, index_1, index_2):
    hulp = stelsel[index_1]
    stelsel[index_1] = stelsel[index_2]
    stelsel[index_2] = hulp


def deel_door(rij, deler):
    for i in range(len(rij)):
        rij[i] = rij[i] / deler


def trek_veelvoud_af(rij_1, rij_2, factor):
    for i in range(len(rij_1)):
        rij_1[i] -= rij_2[i] * factor


def niet_nul_element(stelsel, k, n):
    if k == n - 1:
        r = k
        if stelsel[k][k + 1] != 0.0:
            print("strijdig stelsel :")
        else:
            for i in range(0, n):
                for j in range(len(stelsel[0])):
                    stelsel[i][j] = f"{stelsel[i][j]:.2f}"
                for i in range(0, n):
                    for j in range(len(stelsel[0])):
                        if stelsel[i][j] == '-0.00':
                            stelsel[i][j] = '0.00'
            return None
    else:
        r = k + 1
    while stelsel[r][k] == 0:
        r += 1
    return r


def Gauss_jordan(stelsel):
    n = len(stelsel)

    for k in range(0, n):
        if stelsel[k][k] == 0:
            nieuwe_rij = niet_nul_element(stelsel, k, n)
            if nieuwe_rij == None:
                print(stelsel)
                return stelsel
            else:
                verwissel(stelsel, k, nieuwe_rij)
        deel_door(stelsel[k], stelsel[k][k])
        for r in range(0, n):
            if r != k:
                trek_veelvoud_af(stelsel[r], stelsel[k], stelsel[r][k])
    for i in range(0, n):
        for j in range(len(stelsel[0])):
            stelsel[i][j] = f"{stelsel[i][j]:.2f}"
    for u in range(0, n):
        for j in range(len(stelsel[0])):
            if stelsel[u][j] == '-0.00':
                stelsel[u][j] = '0.00'
    print(stelsel)
    return stelsel


# test Gauss_jordan methode

stelsel = [
    [10,2,4,5],
    [4,9,5,16],
    [0,-3,2,12]
]

Gauss_jordan(stelsel)
