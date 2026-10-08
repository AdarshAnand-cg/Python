category=int(input("1.Vegetarian\n2.Non-Vegetarian\nEnter Category: "))

match category:
    case 1:
        food=int(input("1.Paneer\n2.Dal\n3.Veg Biryani\nEnter Food: "))

        match food:
            case 1:
                print("Paneer Selected")
            case 2:
                print("Dal Selected")
            case 3:
                print("Veg Biryani Selected")
            case _:
                print("Invalid Input")

    case 2:
        food=int(input("1.Chicken Biryani\n2.Chicken Curry\n3.Fish Fry\nEnter Food: "))

        match food:
            case 1:
                print("Chicken Biryani Selected")
            case 2:
                print("Chicken Curry Selected")
            case 3:
                print("Fish Fry Selected")
            case _:
                print("Invalid Input")

    case _:
        print("Invalid Input")