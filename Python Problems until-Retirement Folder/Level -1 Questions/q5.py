age = int(input("Enter your age: "))

if age >= 0 and age <= 12:
    print("child")
elif age >= 13 and age <= 19:
    print("Teenager")
elif age>=20:
    print("Adult")
else:
    print("Enter a valid age")