banking = int(input("Enter banking type: "))

match banking:
    case 1:
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Personal Banking Balance Selected")
            case 2:
                print("Personal Banking Transfer Selected")
            case 3:
                print("Personal Loan Selected")
            case _:
                print("Invalid Option")

    case 2:
        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Business Banking Balance Selected")
            case 2:
                print("Payroll Selected")
            case 3:
                print("Business Loan Selected")
            case _:
                print("Invalid Option")

    case _:
        print("Invalid Banking Type")


