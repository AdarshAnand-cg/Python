age=int(input("Enter Your Age:"))
if age>=18 and age<120:
    print("Can Vote")
elif age<=18 and age>0:
    print("Cannot Vote")
elif age>0 and age<18:
    print("Invalid Age")
else :
    print("Unrealistic Age")