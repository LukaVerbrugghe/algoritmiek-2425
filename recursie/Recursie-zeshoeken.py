def H(n):
    if n ==1:
        return 1
    else:
        return H(n-1) + 6 *(n-1)

print(H(1))
print(H(2))
print(H(3))
print(H(4))
print(H(5))
print(H(6))