def verwissel(stelsel, index_1, index_2):  # vul aan
    #index 1 = rij dat je wil wisselen
    #index 2 = rij waarmee je de eerste ingegeven rij wisselt

    #rijen opslaan in variabelen
    origineel = stelsel[index_1]
    wissel = stelsel[index_2]

    #rijen wisselen
    stelsel[index_1] = wissel
    stelsel[index_2] = origineel

    #Stelsel printen
    print()
    print("stelsel")
    print(stelsel)

def deel_door(rij, deler):  # vul aan
    for i in range(len(rij)):
        rij[i] = rij[i] / deler
    print(rij)

def trek_veelvoud_af(rij_1, rij_2, factor):
    #Alle elementen in rij 1 overlopen
    for i in range(len(rij_1)):
        rij_1[i] = rij_1[i] - factor * rij_2[i]

    print(stelsel)

def niet_nul_element(stelsel, k):
    print("Element: a", k, k, sep="")
    print(stelsel[k][k])

    r = k + 1

    #Loop maken om te voorzorgen dat het element niet 0 is
    while stelsel[r][k] == 0:
        r += 1

    print()
    print("Element: a",r,k, sep= "")
    print(stelsel[r][k])

    #teruggeefwaarde instellen
    return r

def Gauss_jordan(stelsel):  # vul aan
    aantalRijen = len(stelsel)

    for k in range(0, aantalRijen):
        if stelsel[k][k] == 0:
            #Nieuwe rij zoeken waar er een niet-nulelement is
            nieuwe_rij = niet_nul_element(stelsel, k)

            #Rijen verwisselen
            verwissel(stelsel, k, nieuwe_rij)

        #Indien eerste element niet nul is => rij delen door zichzelf
        deel_door(stelsel[k], stelsel[k])

        for r in range(0, aantalRijen):
            if r != k:
                trek_veelvoud_af(stelsel[r], stelsel[k], stelsel[r][k])

    print(stelsel)

# test Gauss_jordan methode
stelsel = [
    [1, 1/3, 0, 0],
    [0, 1, -2, 2],
    [-1, 0, 1, 7]
]

#Testen

#nieuwe_rij = niet_nul_element(stelsel, 0)
#verwissel(stelsel, 0, nieuwe_rij)
#deel_door(0, stelsel[0][0])
#trek_veelvoud_af(stelsel[2], stelsel[0], stelsel[2][0])

#Finale functie uitvoeren
Gauss_jordan(stelsel)