choice=int(input("1.UPI\n2.Card\n3.Cash\n4.Wallet\nEnter Your Payment Method:-"))
match choice:
    case 1:
        print("UPI")
    case 2:
        print("Card")
    case 3:
        print("Cash")
    case 4:
        print("Wallet")
    case _:
        print("Invalid Payment Method")