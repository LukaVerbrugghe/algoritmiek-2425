def H(n):
    if n == 1:
        return 1
    else:
        return H(n-1) + 6*(n-1)

for i in range(1, 7):
    print(i, ": ", H(i))