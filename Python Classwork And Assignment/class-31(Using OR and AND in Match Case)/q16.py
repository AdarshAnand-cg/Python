choice=int(input("1.Student\n2.Teacher"))
match choice:
    case 1:
        status=int(input("1.View Courses\n2.View Marks\nView Attendance\nEnter Any Serial Number"))
        match status:
            case 1:
                print("Opening Courses")
            case 2:
                print("Opening Marks")
            case 3:
                print("Opening Attendence")
            case _:
                print("Invalid Input")
    case 2:
        status=int(input("1.View Students\n2.Enter Marks\nView Attendance\nEnter Any Serial Number"))
        match status:
            case 1:
                print("Opening Students Informance")
            case 2:
                print("Enter Marks")
            case 3:
                print("View Attendance")
            case _:
                print("Invalid Input")
            