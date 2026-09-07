Operation=int(input("Choose Any Serial Number For Following Operation:-\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division \nChoose Your Option:-"))

if Operation==1 or Operation==2 or Operation==3 or Operation==4:
    A=float(input("Enter First Integer:"))
    B=float(input("Enter Second Integer:"))
    if Operation==1:
        print("The addition of the choosen value =",A+B )
    elif Operation==2:
        print("The subtraction of the choosen value =",A-B)
    elif Operation==3:
        print("The mutiplication of the choosen value =",A*B)
    elif Operation==4:
        print("The Division of the choosen value =",A/B)
else:
    print("Oops!Please select The Correct Value")
    


