choice=int(input("1.Electronics\n2.Clothing\n3.Mobile Data\n4.Aeroplane mode\nExit\nEnter Any Serial Number:-"))
match choice:
    case 1:
        print("Electronics ")
    case 2:
        print("Clothing")
    case 3:
        print("Mobile Data ")
    case 4:
        print("Opening Grocery")
    case 5:
        print("Exit")
    case _:
        print("Invalid Input")