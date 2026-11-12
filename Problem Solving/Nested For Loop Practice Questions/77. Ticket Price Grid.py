rows = int(input("Enter Rows: "))
seats = int(input("Enter Seats: "))

for i in range(rows):
    for j in range(1, seats+1):
        if j % 2 == 0:
            print(150, end=" ")
        else:
            print(100, end=" ")

    print()










