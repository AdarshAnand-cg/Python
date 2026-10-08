account=int(input("1.Savings\n2.Current\nEnter Account Type: "))

match account:
    case 1:
        operation=int(input("1.Check Balance\n2.Deposit\n3.Withdraw\nEnter Operation: "))

        match operation:
            case 1:
                print("Savings Account")
                print("Check Balance Selected")
            case 2:
                print("Savings Account")
                print("Deposit Selected")
            case 3:
                print("Savings Account")
                print("Withdraw Selected")
            case _:
                print("Invalid Input")

    case 2:
        operation=int(input("1.Check Balance\n2.Deposit\n3.Withdraw\nEnter Operation: "))

        match operation:
            case 1:
                print("Current Account")
                print("Check Balance Selected")
            case 2:
                print("Current Account")
                print("Deposit Selected")
            case 3:
                print("Current Account")
                print("Withdraw Selected")
            case _:
                print("Invalid Input")

    case _:
        print("Invalid Input")