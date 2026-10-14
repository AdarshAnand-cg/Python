marks=int(input("Enter Your Marks:"))
while marks>100 or marks<0:
    print("Invalid Marks")
    marks=int(input("Enter Your Marks:"))
if marks>75:
    print("Distinction")
elif marks>=60:
    print("First Class")
elif marks>=35:
    print("Pass")
else:
    print("Fail")

