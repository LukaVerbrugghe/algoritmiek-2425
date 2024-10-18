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
    #Array aanmaken voor de te delen rij
    teDelenRij = stelsel[rij]
    print("Te delen rij:")
    print(teDelenRij)
    print()

    #Nieuwe array aanmaken voor de gedeelde rij
    gedeeldeRij = []

    #Alle elementen binnen de rij gaan delen door de deler
    for element in teDelenRij:
        element = element / deler

        #Waarde toevoegen aan nieuwe array
        gedeeldeRij.append(element)

    #nieuwe rij in stelsel steken
    print("Gedeelde rij:")
    stelsel[rij] = gedeeldeRij
    print(gedeeldeRij)
    print()

    print("Nieuw stelsel")
    print(stelsel)

#def trek_veelvoud_af(rij_1, rij_2, factor):  # vul aan

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

#def Gauss_jordan(stelsel):  # vul aan
    #print(stelsel)


# test Gauss_jordan methode
stelsel = [
    [-3, 1, 0, 0],
    [0, 1, -2, 2],
    [-1, 0, 1, 7]
]


#nieuwe_rij = niet_nul_element(stelsel, 0)
#verwissel(stelsel, 0, nieuwe_rij)
deel_door(0, stelsel[0][0])