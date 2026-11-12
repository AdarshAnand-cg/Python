n = int(input("Enter N: "))

for i in range(n):
    for j in range(n):
        if i == j:
            print("A", end=" ")
        elif i+j == n-1:
            print("B", end=" ")
        else:
            print("-", end=" ")
    print()
