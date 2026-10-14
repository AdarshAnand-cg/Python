amount = int(input("Enter Withdrawl Amount:Rs"))
while amount>5000:
    print("Error!\nInvalid Amount")
    amount = int(input("Please Enter Withdrawl Amount Again:Rs"))
print(f"Withdrawl Amount=Rs{amount}/-\nYour Balance is Rs{5000-amount}/-")
