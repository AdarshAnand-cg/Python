n=int(input("Enter Any Number:-"))
i=1

j=1
while i<=10:
    j=1
    while j<=n:
        print(i*j,end="\t")
        j+=1
    print()
    i+=1