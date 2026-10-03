day=int(input("Enter any Number:-"))
match day:
    case 1|2|3|4|5:
        print("Working Day")
    case 6|7:
        print("Holiday")
    case _:
        print("Invalid Input")

marks=int(input("Enter Your Marks:-"))
match marks:
    case x if x>=90:
        print("A")
    case x if x>=75:
        print("B")
    case x if x>=50:
        print("c")
    case _:
        print("Fail")