from random import gauss


def verwissel(stelsel, index_1, index_2):
    origineelRij1 = stelsel[index_1]
    origineelRij2 = stelsel[index_2]
    stelsel[index_1] = origineelRij2
    stelsel[index_2] = origineelRij1
    #print(stelsel)

def deel_door(rij, deler):  # vul aan
    for i in range(len(rij)):
        rij[i] = rij[i]/deler
    #print("Rij: " + str(rij))

def trek_veelvoud_af(rij_1, rij_2, factor):
    for i in range(len(rij_1)):
        rij_1[i] = rij_1[i] - factor * rij_2[i]
    #print(stelsel)

def niet_nul_element(stelsel, k):
    r = k + 1
    while stelsel[r][k] == 0:
        r = r + 1
    #print(r)
    return r

def Gauss_jordan(stelsel):  # vul aan
    n = len(stelsel)
    for k in range(0,n):
        if stelsel[k][k] == 0:
            nieuwe_rij = niet_nul_element(stelsel, k)
            verwissel(stelsel,k,nieuwe_rij)
        deel_door(stelsel[k],stelsel[k][k])
        for r in range(0,n):
            if r != k:
                trek_veelvoud_af(stelsel[r],stelsel[k],stelsel[r][k])

    #print("Stelsel: \n")
    #print(stelsel)

    return stelsel

stelsel = [
    [1, 1, 1, 1, 19],
    [0, 1, 0, -1, 2],
    [-1, 0, 1, 0, 1],
    [91, 10, 10, 91, 838]
]

#Gauss_jordan(stelsel)

def display_matrix(matrix):
    print("Stelsel:\n")
    for row in matrix:
        print("[", " ".join(f"{val:.2f}" for val in row), "]")

print("\n\n")
display_matrix(Gauss_jordan(stelsel))
