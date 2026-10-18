N = 4

for i in range(N):
    for j in range(N):
        if j % 2 == 0:
            print("0", end="")
        else:
            print("1", end="")
    print()