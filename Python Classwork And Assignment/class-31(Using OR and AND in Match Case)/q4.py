choice=int(input("1.Red\n2.Yellow\n3.Green\nEnter Any Traffic Signal Number:-"))
match choice:
    case 1:
        print("Stop")
    case 2:
        print("Wait")
    case 3:
        print("Go")
    case _:
        print("Invalid Input")