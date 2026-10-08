category=int(input("1.Electronics\n2.Clothing\nEnter Category: "))

match category:
    case 1:
        product=int(input("1.Mobile\n2.Laptop\n3.Headphones\nEnter Product: "))

        match product:
            case 1:
                print("Mobile Selected")
            case 2:
                print("Laptop Selected")
            case 3:
                print("Headphones Selected")
            case _:
                print("Invalid Input")

    case 2:
        product=int(input("1.Shirt\n2.Jeans\n3.Shoes\nEnter Product: "))

        match product:
            case 1:
                print("Shirt Selected")
            case 2:
                print("Jeans Selected")
            case 3:
                print("Shoes Selected")
            case _:
                print("Invalid Input")

    case _:
        print("Invalid Input")