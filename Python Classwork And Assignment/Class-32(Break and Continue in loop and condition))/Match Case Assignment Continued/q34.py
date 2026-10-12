choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Starting Game")
    case 2:
        print("Loading Game")
    case 3:
        option = int(input("Enter setting: "))

        match option:
            case 1:
                print("Sound Settings Opened")
            case 2:
                print("Graphics Settings Opened")
            case 3:
                print("Controls Settings Opened")
            case _:
                print("Invalid Setting")
    case 4:
        print("Exiting Gaming Console")
    case _:
        print("Invalid Choice")

