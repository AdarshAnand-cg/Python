a=int(input("Enter The First Number:"))
b=int(input("Enter The Second Number:"))
if a<b:
    for i in range(1,b+1):
        if a%i==0 and b%i==0:
            hcf=i
    print(f"L.C.M of {a} and {b} is  {(a*b)/hcf}")
else:
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
            hcf=i
    print(f"L.C.M of {a} and {b} is {int((a*b)//hcf)}")