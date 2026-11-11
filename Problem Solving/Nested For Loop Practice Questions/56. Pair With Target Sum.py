n = int(input("Enter Number:-"))
target = int(input("Enter Target:-"))

for i in range(1, n+1):
    for j in range(1, n+1):
        if i+j == target:
            print(i, j)