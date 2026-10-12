subject = int(input("Enter subject: "))

match subject:
    case 1:
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Python Course Selected")
            case 2:
                print("Java Course Selected")
            case 3:
                print("C++ Course Selected")
            case _:
                print("Invalid Option")

    case 2:
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Algebra Course Selected")
            case 2:
                print("Calculus Course Selected")
            case 3:
                print("Statistics Course Selected")
            case _:
                print("Invalid Option")

    case 3:
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("English Course Selected")
            case 2:
                print("Presentation Course Selected")
            case 3:
                print("Interview Skills Course Selected")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Subject")


