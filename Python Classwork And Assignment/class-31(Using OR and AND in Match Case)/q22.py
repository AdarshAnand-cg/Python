choice = int(input("Enter choice: "))
value = float(input("Enter value: "))

match choice:
    case 1:
        meters = value * 1000
        print(meters, "meters")

    case 2:
        kilometers = value / 1000
        print(kilometers, "kilometers")

    case 3:
        grams = value * 1000
        print(grams, "grams")

    case 4:
        kilograms = value / 1000
        print(kilograms, "kilograms")

    case _:
        print("Invalid choice")