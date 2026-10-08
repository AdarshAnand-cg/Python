choice=int(input("1.Account Balance\n2.Mini Statement\n3.Fund Transfer\n4.Aeroplane mode\nCustomer Support\nEnter Any Serial Number:-"))
match choice:
    case 1:
        print("Account Balance")
    case 2:
        print("Mini Statement")
    case 3:
        print("Fund Transfer")
    case 4:
        print("Bill Payment")
    case 5:
        print("Customer Support")
    case _:
        print("Invalid Input")