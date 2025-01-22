import matplotlib.pyplot as plt

#opdracht 1
def rij(n):
    x= []

    #algoritme voor alle waarden te berekenen
    for l in range(n):
        #als de eerste term 0 is, dan gebruiken we U1
        if l == 0:
            #startwaarde gebruiken
            uitkomst = 2
        else:
            #uitkomst berekenen met voorschrift
            uitkomst = (-2*(x[l-1]**2) + (x[l-1] + 4)) / 2

        x.append(uitkomst)
    print(x)

    #lijst plotten
    for h in range(len(x)):
        plt.scatter(h,x[h],color = 'r')
    plt.xlabel('Index')
    plt.ylabel('Waarde')
    plt.title('Rij')
    plt.show()

#functie uitvoeren
rij(10)

#opdracht 2
#data structuur = een array

#opdracht 3
#We gebruiken deze datastructuur omdat het makkelijk is om met de vorige waarden te werken en deze dan op te slaan. Selectie van elementen binnen de array is ook heel eenvoudig.

#opdracht 4
#We zien dat dezelfde waarden constant terugkomen (2; -1; 0.5), we zouden dus besluiten dat dit oneindig ver zal doorlopen
