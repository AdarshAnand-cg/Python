transport = int(input("Enter transport: "))

match transport:
    case 1:
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Flight Economy Selected")
            case 2:
                print("Flight Business Class Selected")
            case _:
                print("Invalid Option")

    case 2:
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Train Sleeper Selected")
            case 2:
                print("Train AC Selected")
            case _:
                print("Invalid Option")

    case 3:
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Bus Ordinary Selected")
            case 2:
                print("Bus Volvo Selected")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Transport")


