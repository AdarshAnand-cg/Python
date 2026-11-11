num=int(input("Enter Any Number:-"))
for i in range(1,num+1):
    print(f"{i} -> ",end="")
    for j in range(1,i+1):
        if i % j == 0:
            print(f"{j} ",end=" ")
    print()