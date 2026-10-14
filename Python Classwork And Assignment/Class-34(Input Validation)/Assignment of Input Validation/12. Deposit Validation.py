# Question-1

balance = 2000

amount = int(input("Enter deposit amount: Rs"))

while amount <= 0:
    print("Invalid Amount! Please enter a positive amount.")
    amount = int(input("Enter deposit amount: Rs"))

balance += amount

print("New Balance: Rs", balance)