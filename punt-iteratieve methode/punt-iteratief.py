# initial guess
x_1 = 0
x_2 = 0
x_3 = 0

#     functievoorschriften per punt
def bereken_x_1():
    return (7 - x_2 - x_3) / 2

def bereken_x_2():
    return (2 + x_1 + x_3) / 3

def bereken_x_3():
    return (5 - x_1 + x_2) / 2


# checken van de voorschriften
def check_x_1():
    return (7 - x_2 - x_3) / 2 == x_1

def check_x_2():
    return (2 + x_1 + x_3) / 3 == x_2

def check_x_3():
    return (5 - x_1 + x_2) / 2 == x_3


while(not check_x_1() or not check_x_2() or not check_x_3()):
    x_1 = bereken_x_1()
    print(x_1)
    x_2 = bereken_x_2()
    print(x_2)
    x_3 = bereken_x_3()
    print(x_3)


print("Eindwaarden:")
print("")
print(x_1)
print(x_2)
print(x_3)