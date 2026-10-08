ticket = int(input("Enter ticket type: "))
age = int(input("Enter age: "))

match ticket:
    case 1:
        if age < 5:
            print("Free Entry")
        else:
            print("Regular Ticket")

    case 2:
        if age < 5:
            print("Free Entry")
        else:
            print("Premium Ticket")

    case 3:
        if age < 5:
            print("Free Entry")
        else:
            print("VIP Ticket")

    case _:
        print("Invalid Ticket Type")