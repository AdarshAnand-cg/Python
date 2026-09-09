marks=int(input("Enter Your Marks:-"))
if marks>=90 and marks<100:
    print("A")
elif marks>=80 and marks<90:
    print("B")
elif marks>=70 and marks<80:
    print("C")
elif marks>=60 and marks<70:
    print("D")
elif marks>=40 and marks<60:
    print("E")
elif marks>=0 and marks<40 :
    print("Fail")
else:
    print("Invalid Input")