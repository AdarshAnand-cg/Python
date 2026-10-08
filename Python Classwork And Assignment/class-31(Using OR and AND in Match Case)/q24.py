choice = int(input("Enter choice: "))
match choice:
    case 1:
        age = int(input("Enter age: "))

        if age >= 18:
            print("You can start the exam")
        else:
            print("You cannot start the exam")

    case 2:
        print("View Result Selected")

    case 3:
        print("Exit Selected")

    case _:
        print("Invalid choice")