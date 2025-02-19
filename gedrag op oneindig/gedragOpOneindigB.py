import matplotlib.pyplot as plt

# gedrag op oneindig berekenen

# we hebben met deze code gecheckt of de functie convergerend is. Dat is het geval
# for i in range(100):
#     if i == 0:
#         j = 0
#         x.append(j)
#     else:
#         j = (-5*i) / (1+25*i)
#         x.append(j)
#     for i in range(len(x)):
#         plt.scatter(i, x[i], color='r')
# plt.show()

def xx(n):
    return (-5*n) / (1+25*n)

x = []

x1 = xx(0)
x2 = xx(1)
tol = 0.000001
x.append(x1)
x.append(x2)
i = 2
residual = abs(x2 - x1)
residualArray = []
residualArray.append(residual)
while abs(residual) > tol:
    print(x1)
    x1 = x2
    x2 = xx(i)
    i+=1
    x.append(x2)
    residual = abs(x2 - x1)
    residualArray.append(residual)
for i in range(len(x)):
    plt.scatter(i, x[i], color='r')
plt.show()
for i in range(len(residualArray)):
    plt.scatter(i, residualArray[i], color='b')
plt.yscale('log')
plt.show()

