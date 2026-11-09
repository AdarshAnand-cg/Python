N = int(input("Enter Any Number:-"))

for i in range(N):
    for j in range(N):
        if j % 2 == 0:
            print("0", end="")
        else:
            print("1", end="")
    print()