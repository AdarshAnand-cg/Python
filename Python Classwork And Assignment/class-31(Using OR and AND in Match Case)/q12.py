choice=int(input("1.Admin\n2.Teacher\n3.Student\n4.Guest\nEnter Your Response:-"))
match choice:
    case 1:
        print("Full Access")
    case 2:
        print("Teacher Dashboard")
    case 3:
        print("Student Dashboard")
    case 4:
        print("Limited Access")
    case _:
        print("Invalid Role")