for i in range(3):
    total=0
    average=0
    marks=(input("The Marks should be written as <80 56 89 93>\nEnter Marks of All Your Subject:-")).split()
    for ch in marks:
        total+=int(ch)
        average=total/4
    print(f"Total:-{total}\nAverage:-{average}")

    