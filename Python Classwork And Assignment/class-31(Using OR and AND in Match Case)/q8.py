choice=int(input("1.Morning Show\n2.Afternoon Show\n3.Evening Show\n4.Night Show\nEnter Any Serial Number:-"))
match choice:
    case 1:
        print("Morning Show")
    case 2:
        print("Afternoon Show")
    case 3:
        print("Evening Show")
    case 4:
        print("Night Show")
    case _:
        print("Invalid Input")