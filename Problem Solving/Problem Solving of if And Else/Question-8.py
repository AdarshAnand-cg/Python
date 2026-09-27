marks=int(input("Enter Your Marks:-"))
if marks>100 or marks<0:
    print("Invalid marks")
elif marks>=40 and marks<100:
    print("Pass")
elif marks<40 :
    print("Fail")