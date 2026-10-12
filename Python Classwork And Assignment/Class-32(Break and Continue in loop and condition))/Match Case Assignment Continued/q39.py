role = int(input("Enter role: "))

match role:
    case 1:
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Opening Employee Profile")
            case 2:
                days = int(input("Enter leave days: "))

                if days > 0:
                    print("Leave Request Submitted")
                else:
                    print("Invalid Leave Days")

            case 3:
                print("Opening Employee Salary")
            case _:
                print("Invalid Option")

    case 2:
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Viewing Team")
            case 2:
                print("Approving Leave")
            case 3:
                print("Viewing Reports")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Role")

