choice=int(input("1.Low\n2.Medium\n3.High\n4.Critical\nEnter Any Number:-"))
match choice:
    case 1|2:
        print("Normal Priority")
    case 3|4:
        print("Urgent priority")
    case _:
        print("Invalid Input")