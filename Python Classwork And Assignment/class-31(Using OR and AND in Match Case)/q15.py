choice=int(input("1.Bronze\n2.Silver\n3.Gold\n4.Platinum\nEnter Your Membership Level:-"))
match choice:
    case 1|2:
        print("Basic Membership")
    case 3|4:
        print("Premium Membership")
    case _:
        print("Invalid Payment Method")