a = int(input("Enter your number: "))
b = int(input("Enter your number: "))
c = int(input("Enter your number: "))

if a>b and a>c:
    print(a)
elif b>c and b>a:
    print(b)
else:
    print(c)  