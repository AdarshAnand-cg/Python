check_min_age=(input("Are You 18+ (Yes or No):"))

if check_min_age=="Yes" or check_min_age=="yes":
    age=int(input("Enter Your age:"))
    if age<=60:
        print(f"Your Age is :{age}")
    else :
        print("Sorry!!! The age must be less than 60")    
else :
    print("Oops!! You Are UnderAge")        