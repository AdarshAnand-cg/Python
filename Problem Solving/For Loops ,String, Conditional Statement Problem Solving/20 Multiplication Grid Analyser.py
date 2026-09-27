n=int(input("Enter n:-"))
status=""
for i in range(1,n+1):
    for j in range(1,n+1):
        if i*j%2==0:
            status="E"
        elif i*j%5==0:
            status="F"
        elif i*j%2!=0:
            status="O"
        print(f"{status}",end=" ")
    print()

