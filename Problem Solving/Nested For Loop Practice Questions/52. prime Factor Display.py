number=int(input("Enter Any Number:-"))
print(f"{number} -> ", end="")
flag=True
for i in range(1,number+1):
    if number%i == 0:
        if flag:
            print(i,end="")
            flag=False
        else:
            print(",",i,sep="",end="")

            