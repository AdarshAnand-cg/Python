choice=int(input("1.Wi-Fi\n2.Bluetooth\n3.Mobile Data\n4.Aeroplane mode\nExit\nEnter Any Serial Number:-"))
match choice:
    case 1:
        print("Wi-Fi Selected")
    case 2:
        print("Bluetooth Selected")
    case 3:
        print("Mobile Data Selected")
    case 4:
        print("Aeroplane Mode Selected")
    case 5:
        print("Exit")
    case _:
        print("Invalid Input")