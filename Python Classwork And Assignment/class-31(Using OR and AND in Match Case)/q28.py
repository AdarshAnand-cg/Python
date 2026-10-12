choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Book Ticket Selected")

    case 2:
        print("Cancel Ticket Selected")

    case 3:
        print("Check PNR Selected")

    case 4:
        print("Train Schedule Selected")

    case 5:
        print("Exiting Railway System")

    case _:
        print("Invalid Choice")