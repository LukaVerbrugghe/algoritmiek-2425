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
    print(stelsel)



def deel_door(rij, deler):  # vul aan
    teDelenRij = stelsel[rij]
    gedeeldeRij = []

    #Alle elementen binnen de rij gaan delen door de deler
    for element in teDelenRij:
        element = element / deler
        gedeeldeRij.append(element)

    #nieuwe rij in stelsel steken
    stelsel[rij] = gedeeldeRij
    print(gedeeldeRij)
    print()
    print("Nieuw stelsel")
    print(stelsel)

#def trek_veelvoud_af(rij_1, rij_2, factor):  # vul aan


#def niet_nul_element(stelsel, k):  # vul aan


#def Gauss_jordan(stelsel):  # vul aan
    #print(stelsel)


# test Gauss_jordan methode

stelsel = [
    [-3, 1, 0, 0],
    [0, 1, -2, 2],
    [-1, 0, 1, 7]
]

print("Verwisselen")
#verwissel(stelsel, 0, 2)

print()

print("Delen door")
deel_door(0, -3)