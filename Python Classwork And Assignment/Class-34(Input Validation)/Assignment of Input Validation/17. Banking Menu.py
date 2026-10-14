balance = 10000
choice = 0
while choice != 4:
   choice = int(input("1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Exit\nEnter your choice: "))
   while choice < 1 or choice > 4:
        print("Invalid Choice!")
        choice = int(input("Enter your choice: "))
   if choice == 1:
        print("Current Balance: Rs", balance)
   elif choice == 2:
        amount = int(input("Enter deposit amount: Rs"))
        while amount <= 0:
            print("Amount must be greater than zero!")
            amount = int(input("Enter deposit amount: Rs"))
        balance += amount
        print("Deposit Successful!")
        print("New Balance: Rs", balance)
   elif choice == 3:
        amount = int(input("Enter withdrawal amount: Rs"))
        while amount <= 0 or amount > balance:
            print("Invalid Withdrawal Amount!")
            amount = int(input("Enter withdrawal amount: Rs"))
        balance -= amount
        print("Withdrawal Successful!")
        print("Remaining Balance: Rs", balance)
   elif choice == 4:
        print("Thank you for using our banking service!")