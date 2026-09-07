is_indian=input("Are you Indian:Yes or No:-")

if is_indian=="Yes":
    age=int(input("Enter Your Age:-"))
    if age>=18:
        Status=input("Are you available at Voting Booth:Yes or No:-")
        if Status=="Yes":
            party=input("Choose Your Party: BJP or Congress or AAP;--")
            if party=="BJP":
                print("You are the real Andh-Bhakt.Only Because of you,Modi become God.You are the greatest Of All Time. ")
        if Status=="No":
            statement=input("Can you tell us the reason behind it? Ans:-")
            print("No Worries,Your Own Life is Also Important.Take Your Own Time.Thanks for Responding")
    if age<=18:
        print("Wait till You become 18 years old and eligible to take vote.our wishes are with You")
if is_indian=="No":
    print("Sorry!!!,for giving vote to any party in India.You must have Indian Citizenship")
else :
    print("Please Give Your Answer in 'Yes' or 'No' only")

