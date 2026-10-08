choice=int(input("1.Check Balance\n2.Withdraw Money\n3.Deposit Money\n4.Change PIN\nExit\nEnter Any Serial Number:-"))
match choice:
    case 1:
        print("Check Balance")
    case 2:
        print("Withdraw money")
    case 3:
        print("Deposit Money")
    case 4:
        print("Change PIN")
    case 5:
        print("Exit")
    case _:
        print("Invalid Input")