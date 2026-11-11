num1=int(input("Enter The First Number:-"))
num2=int(input("Enter The Second Number:-"))
limit=int(input("Enter Limit:-"))
for i in range(1, limit):
    for j in range(1, limit):
        if num1*i == num2*j and num1*i < limit:
            print(num1*i,end=" ")
    