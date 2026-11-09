# Question-11
rows = 3
columns = 6

for i in range(rows):
    for j in range(1, columns + 1):
        if j % 2 == 0:
            print(j, end=" ")
    print()

# Question-12
N = 7

for i in range(N):
    for j in range(1, N + 1):
        if j % 2 != 0:
            print(j, end=" ")
    print()

# Question-13
for i in range(1, 5):
    for j in range(1, 5):
        if (i + j) % 2 == 0:
            print("E", end=" ")
        else:
            print("O", end=" ")
    print()

# Question-14
N = 3

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            print("Same", end=" ")
        else:
            print("Different", end=" ")
    print()

# Question-15
N = 4

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()

# Question-16
for i in range(1, 6):
    for j in range(1, 6):
        if i % j == 0:
            print("X", end=" ")
        else:
            print("-", end=" ")
    print()

# Question-17
N = 4

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if j % i == 0:
            print(j, end=" ")
    print()

# Question-18
N = 4

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i + j > N:
            print(i, j)

# Question-19
N = 3

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i * j % 2 == 0:
            print(i, j, i * j)

# Question-20
N = 4

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            print("SPECIAL", end=" ")
        elif i + j == N:
            print("PAIR", end=" ")
        else:
            print("NORMAL", end=" ")
    print()