choice=int(input("1.Monday\n2.Tuesday\n3.Wednesday\n4.Thursday\n5.Friday\n6.Saturday\n7.Sunday\nEnter The Day:-"))
match choice:
    case 1|2|3|4|5:
        print("Weekday")
    case 6|7:
        print("Weekend")
    case _:
        print("Invalid input")