choice=int(input("1. View Profile\n2.View Courses\n3.View Marks\n4.View Attendance\nLogout\nEnter Any Serial Number:-"))
match choice:
    case 1:
        print("Opening Profile")
    case 2:
        print("Opening Courses")
    case 3:
        print("Opening Marks")
    case 4:
        print("Opening Attendance")
    case 5:
        print("Logout")
    case _:
        print("Invalid Input")