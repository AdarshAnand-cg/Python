check_number=input("Is the number a non-zero?Yes or NO:-")

if check_number=="Yes" or check_number=="yes":
    number=int(input("Enter the non-zero number:-"))
    if number>0:
        print("Positive")
    elif number<0:
        print("Negative") 
    else :
        print("Invalid Input")
            