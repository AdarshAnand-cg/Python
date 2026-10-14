marks=int(input("Enter Your Marks:-"))
while marks>100 or marks<0:
    print("Invalid Input")
    marks=int(input("Enter Your Marks(It should be between 0 to 100):-"))
if 0<=marks<=100:
    if marks>35:
        print("Pass")
    else:
        if 0<=marks<35:
            print("You Are Failed")
        else:
            True


    