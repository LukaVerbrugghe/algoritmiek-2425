import matplotlib.pyplot as plt

# gedrag op oneindig berekenen

x = []
for i in range(100):
    if i == 0:
        j = 0
        x.append(j)
    else:
        j = i ** 2 - (1/i)
        x.append(j)
    for i in range(len(x)):
        plt.scatter(i, x[i], color='r')
plt.show()

# CONCLUSIE
# De functie gaat steeds verder omhoog en convergeert niet naar een specifieke waarde.