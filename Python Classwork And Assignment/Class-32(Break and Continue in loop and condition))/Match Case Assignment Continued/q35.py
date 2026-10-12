category = int(input("Enter category: "))

match category:
    case 1:
        item = int(input("Enter item: "))

        match item:
            case 1:
                print("Soup Selected")
            case 2:
                print("Spring Roll Selected")
            case 3:
                print("Garlic Bread Selected")
            case _:
                print("Invalid Item")

    case 2:
        item = int(input("Enter item: "))

        match item:
            case 1:
                print("Pizza Selected")
            case 2:
                print("Pasta Selected")
            case 3:
                print("Biryani Selected")
            case _:
                print("Invalid Item")

    case 3:
        item = int(input("Enter item: "))

        match item:
            case 1:
                print("Ice Cream Selected")
            case 2:
                print("Cake Selected")
            case 3:
                print("Gulab Jamun Selected")
            case _:
                print("Invalid Item")

    case 4:
        item = int(input("Enter item: "))

        match item:
            case 1:
                print("Coffee Selected")
            case 2:
                print("Tea Selected")
            case 3:
                print("Juice Selected")
            case _:
                print("Invalid Item")

    case _:
        print("Invalid Category")