choice=int(input("1. sunny\n2.rainy\n3.cloudy\n4.snowy\nEnter Any Serial Number:-"))
match choice:
    case 1:
        print("Wear sunglasses")
    case 2:
        print("Carry an umbrella")
    case 3:
        print("Weather may change")
    case 4:
        print("Wear warm clothes")
    case _:
        print("Unknown Weather")