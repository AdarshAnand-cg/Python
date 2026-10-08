# Q23. ATM Withdrawal

account = int(input("Enter account type: "))
amount = float(input("Enter amount: "))

match account:
    case 1:
        if amount > 0:
            print("Savings Account")
            print("Withdrawal Request Accepted")
        else:
            print("Invalid Amount")

    case 2:
        if amount > 0:
            print("Current Account")
            print("Withdrawal Request Accepted")
        else:
            print("Invalid Amount")

    case _:
        print("Invalid Account Type")