rows = int(input("Enter Rows: "))
seats = int(input("Enter Seats in Each Row: "))

total_open = 0
total_booked = 0
highest = -1
best_row = 0

for i in range(rows):
    open_seats = 0

    for j in range(seats):
        status = input("Enter O for Open and B for Booked: ").upper()

        if status == "O":
            open_seats += 1
            total_open += 1
        else:
            total_booked += 1

    print("Row", i+1, "Open Seats =", open_seats)

    if open_seats > highest:
        highest = open_seats
        best_row = i+1

print("Total Open Seats =", total_open)
print("Total Booked Seats =", total_booked)
print("Row With Most Open Seats =", best_row)
