password = input("Enter Your password(atleast 8 Chararcters):-").strip()
count=password.isspace()
while len(password) < 8 or count>0:
    print("Error!\nInvalid password\nPlease Enter Your Correct password")
    password = input("Enter Your password(Atleast 8 Chararcters):- ")
print(f"Your Password Is Saved As:{password}")
        
    


