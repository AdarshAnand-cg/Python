role = int(input("Enter role: "))

match role:
    case 1:
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Opening Student Marks")
            case 2:
                print("Opening Student Attendance")
            case 3:
                print("Opening Student Homework")
            case _:
                print("Invalid Option")

    case 2:
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Opening Enter Marks")
            case 2:
                print("Opening Teacher Attendance")
            case 3:
                print("Opening Assign Homework")
            case _:
                print("Invalid Option")

    case 3:
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Opening Child Marks")
            case 2:
                print("Opening Child Attendance")
            case 3:
                print("Opening Contact Teacher")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Role")


