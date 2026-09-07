# Task-19
status=input('Are You 17+ ?\n Enter Yes or No:-')

if status=="Yes":
    age=int(input("Enter Your Age:-"))
    if age<=60:
        print("You Are the person who is considered as active citizen of any couuntry")
    elif age>60:
        print("Take care of your Health.life is precious")
elif status=="No":
    print("you are underage")
else :
    print("Oops!!Invalid Input\nChoose your Answer in Yes or No")
