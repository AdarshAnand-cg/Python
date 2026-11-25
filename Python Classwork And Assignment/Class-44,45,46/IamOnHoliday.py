for i in range(1,5):
    for j in range(1,5):
        print(f"{i,j}",end=" ")
    print()
print(f"\n")
for i in range(1,5):
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()