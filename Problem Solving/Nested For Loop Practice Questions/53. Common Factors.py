num1=int(input("Enter The First Number:-"))
num2=int(input("Enter The Second Number:-"))
for i in range(1,num1+1):
    for j in range(1,num2+1):
        if i == j:
            if (num1%i == 0) and (num2%i == 0):
                print(i,end=" ")